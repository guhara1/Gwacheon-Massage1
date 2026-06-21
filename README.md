# 바로GO — 과천 출장마사지·홈타이 안내 사이트

경기도 과천시 전지역 방문형 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
상호: **바로GO** / 전화예약: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함
- 도메인 루트 `/` 는 과천 메인 `/gyeonggi/gwacheon/` 으로 리다이렉트(noindex)

```
build.py            # 빌드 스크립트 (레이아웃·글자수 검사·디스크립션 80자 검사·sitemap)
content/
  site.py           # 상호·전화·BASE_URL·텔레그램·메뉴 구조
  main.py           # 과천 메인 (/gyeonggi/gwacheon/) + WebPage/Organization/FAQ JSON-LD
  areas.py          # 대표동 7개 (중앙·갈현·원문·별양·부림·과천·문원)
  stations.py       # 역세권 허브 + 역 6개
  districts.py      # 생활권 허브 + 생활권 9개
  info.py           # 예약 안내·이용 전 확인사항·홈타이 가이드·고객센터·개인정보·약관
  about.py          # 사이트 소개 (E-E-A-T)
assets/             # CSS(프리미엄 팔레트 토큰), 모바일 내비 JS
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수와 디스크립션 80자 초과 여부가 출력됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- **메타 디스크립션 80자 이내** (초과 시 빌드 로그에 경고)
- 메뉴명·URL에 "출장마사지" 반복 금지 — Title·H1·첫 문단에서만 자연스럽게 사용
- 대표동은 7개만, 법정동(관문·주암·막계)은 대표동·생활권 페이지에서 보조 설명
- 역은 역명 기준 1 URL — 출구별·예정역 페이지 없음, 인덕원은 인접 생활권으로만 처리
- 같은 본문에서 지역명만 바꾼 복붙 금지 — 모든 페이지 고유 작성

## 푸터

- 오렌지 CTA 버튼: **웹사이트 제작문의**, **제휴문의** — 텔레그램 링크
  (`content/site.py` 의 `TELEGRAM_BUILD`, `TELEGRAM_PARTNER` 에서 변경)

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. `content/site.py`의 `TELEGRAM_BUILD`, `TELEGRAM_PARTNER` 텔레그램 채널 확인
3. `python3 build.py` 재실행 (canonical·sitemap·robots.txt에 반영됨)
4. Google Search Console에 `sitemap.xml` 제출
