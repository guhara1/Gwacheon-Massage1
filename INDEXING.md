# 색인(인덱싱) 빠르게 하기 — 운영 가이드

생성물(빌드 시 자동):
- `sitemap.xml` — `lastmod`·`changefreq` 포함, 색인 허용 페이지만(현재 30개)
- `rss.xml` — 네이버/구글/빙 피드 발견용, 모든 `<head>` 에 `alternate` 링크
- `robots.txt` — 모든 크롤러 허용 + Googlebot/Yeti(네이버)/bingbot 명시 + Sitemap 위치
- `7e3b9c1d4a8f42e6b05c9d2f1a6e8b3c.txt` — IndexNow 키 파일(루트)
- 메인 `<head>` 에 네이버 사이트 인증 메타 태그

## 1) IndexNow — 빙·네이버 즉시 통보 (핵심)

빙(Bing)과 네이버(Naver)는 IndexNow 참여 엔진이라 **한 번 통보로 함께 반영**됩니다.

> 먼저 사이트를 배포해서 키 파일이 실제로 열려야 합니다:
> `https://gwacheon-massage1.pages.dev/7e3b9c1d4a8f42e6b05c9d2f1a6e8b3c.txt`
> (이 파일이 200으로 열려야 IndexNow 가 키를 검증합니다.)

첫 일괄 통보(모든 URL):
```bash
python build.py            # 산출물 갱신
python tools/indexnow.py   # sitemap.xml 전체를 빙·네이버에 통보
```

글/페이지를 새로 올리거나 수정할 때마다(해당 URL만):
```bash
python tools/indexnow.py /hometai/ /jungang-dong/
```

키를 바꾸려면 `content/site.py` 의 `INDEXNOW_KEY` 수정 후 `python build.py` 재실행.

## 2) 구글 — 가장 확실한 방법

구글은 IndexNow 미참여입니다. 순서대로 하세요.
1. **Google Search Console** 속성 등록 → `sitemap.xml` 제출(1회). 이후 `lastmod` 로 재크롤 유도.
2. 급할 때 URL 검사 → "색인 생성 요청".
3. (선택) **Indexing API** 자동화: `tools/google_indexing.py`
   - 공식적으론 JobPosting/BroadcastEvent 전용이라 일반 페이지는 보장 안 됨(보조 수단).
   - `pip install google-auth requests`, 서비스 계정 JSON + Search Console 소유자 등록 필요.
   - `export GOOGLE_APPLICATION_CREDENTIALS=...` 후 `python tools/google_indexing.py`

## 3) 네이버 — 서치어드바이저

1. 네이버 서치어드바이저에 사이트 등록(메인 `<head>` 인증 메타는 이미 추가됨).
2. `sitemap.xml`, `rss.xml` 제출.
3. 위 IndexNow 통보가 네이버에도 함께 적용됩니다.

## 참고 — sitemap ping 자동화는?

구글(2023년)과 빙은 인증 없는 `?sitemap=` ping 엔드포인트를 **폐지**했습니다.
따라서 즉시 통보는 IndexNow(빙·네이버)로, 구글은 Search Console 제출 + Indexing API 로 대체합니다.
