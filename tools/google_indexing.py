#!/usr/bin/env python3
"""(선택) 구글 Indexing API 통보 — 구글은 IndexNow 미참여이므로 별도 제공.

주의: 구글 Indexing API 는 공식적으로 JobPosting / BroadcastEvent 구조화 데이터
페이지에만 지원됩니다. 일반 페이지는 색인이 보장되지 않으며, 가장 확실한 방법은
Google Search Console 에 sitemap.xml 을 제출하는 것입니다. 이 스크립트는 보조 수단입니다.

사전 준비:
  1) Google Cloud 프로젝트에서 Indexing API 사용 설정
  2) 서비스 계정 생성 → JSON 키 다운로드
  3) Search Console 속성에 서비스 계정 이메일을 "소유자"로 추가
  4) pip install google-auth requests
  5) 환경변수: export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json

사용법:
  python tools/google_indexing.py                 # sitemap.xml 전체
  python tools/google_indexing.py /hometai/       # 특정 경로(들)
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from content.site import BASE_URL  # noqa: E402

BASE = BASE_URL.rstrip("/")
SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

try:
    from google.oauth2 import service_account
    from google.auth.transport.requests import AuthorizedSession
except ImportError:
    sys.exit("의존성 필요: pip install google-auth requests")


def normalize(arg: str) -> str:
    if arg.startswith("http"):
        return arg
    return BASE + "/" + arg.lstrip("/")


def urls_from_sitemap() -> list:
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python build.py` 실행.")
    with open(path, encoding="utf-8") as f:
        return re.findall(r"<loc>(.*?)</loc>", f.read())


def main() -> None:
    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        sys.exit("GOOGLE_APPLICATION_CREDENTIALS 환경변수에 서비스 계정 JSON 경로를 지정하세요.")
    creds = service_account.Credentials.from_service_account_file(cred_path, scopes=SCOPES)
    session = AuthorizedSession(creds)

    args = sys.argv[1:]
    urls = [normalize(a) for a in args] if args else urls_from_sitemap()
    ok = 0
    for url in urls:
        r = session.post(ENDPOINT, json={"url": url, "type": "URL_UPDATED"})
        status = "✓" if r.status_code == 200 else f"✗({r.status_code})"
        print(f"  {status} {url}")
        ok += r.status_code == 200
    print(f"\n{ok}/{len(urls)} 통보 완료.")


if __name__ == "__main__":
    main()
