#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — 빙(Bing)·네이버(Naver) 등 IndexNow 참여 엔진에 한 번에 통보.

사용법:
    python tools/indexnow.py                 # sitemap.xml 의 모든 URL 통보 (첫 일괄 통보)
    python tools/indexnow.py /jungang-dong/  # 특정 경로(들)만 통보 — 글 올릴 때마다
    python tools/indexnow.py https://gwacheon-massage1.pages.dev/hometai/

키 파일은 build.py 가 루트에 "{INDEXNOW_KEY}.txt" 로 생성합니다.
표준 라이브러리만 사용하므로 별도 설치가 필요 없습니다.
"""
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

BASE = BASE_URL.rstrip("/")
HOST = re.sub(r"^https?://", "", BASE).split("/")[0]
KEY_LOCATION = f"{BASE}/{INDEXNOW_KEY}.txt"
ENDPOINT = "https://api.indexnow.org/IndexNow"


def normalize(arg: str) -> str:
    if arg.startswith("http://") or arg.startswith("https://"):
        return arg
    return BASE + "/" + arg.lstrip("/")


def urls_from_sitemap() -> list:
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python build.py` 를 실행하세요.")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def submit(url_list: list) -> None:
    if not url_list:
        sys.exit("통보할 URL 이 없습니다.")
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": url_list,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    print(f"IndexNow → {ENDPOINT}")
    print(f"  host={HOST}  keyLocation={KEY_LOCATION}")
    print(f"  {len(url_list)}개 URL 통보 중...")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            code = resp.getcode()
    except urllib.error.HTTPError as e:
        code = e.code
        body = e.read().decode("utf-8", "ignore")
        print(f"  응답 {code}: {body.strip()}")
        if code in (200, 202):
            return
        sys.exit(f"  실패(코드 {code}). 키 파일 배포 여부를 확인하세요: {KEY_LOCATION}")
    # 200/202 = 접수됨. 빙·네이버 등 참여 엔진에 공유됩니다.
    print(f"  응답 {code} — 접수 완료 ✓ (빙·네이버 등 IndexNow 참여 엔진에 공유)")


if __name__ == "__main__":
    args = sys.argv[1:]
    urls = [normalize(a) for a in args] if args else urls_from_sitemap()
    submit(urls)
