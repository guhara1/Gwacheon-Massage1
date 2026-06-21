# 메인 페이지 — 과천시 허브. 키워드를 한곳에 몰지 않고 상세 페이지로 연결한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_JSONLD = f"""<meta name="naver-site-verification" content="3223f1b1ae524607d19471d218fbfc5836b19aec">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "과천시 출장마사지 · 홈타이 지역별 예약 안내",
  "url": "{BASE_URL}/",
  "description": "과천시 출장마사지·홈타이 예약 전 정부과천청사, 과천역, 별양동, 갈현동, 선바위 생활권을 확인하세요.",
  "inLanguage": "ko",
  "primaryImageOfPage": {{
    "@type": "ImageObject",
    "url": "{BASE_URL}/assets/og-image.png",
    "width": 1200,
    "height": 630
  }},
  "isPartOf": {{
    "@type": "WebSite",
    "name": "{BRAND}",
    "url": "{BASE_URL}/"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "url": "{BASE_URL}/",
  "image": "{BASE_URL}/assets/og-image.png",
  "telephone": "{PHONE}",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "경기도 과천시"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "홈", "item": "{BASE_URL}/" }},
    {{ "@type": "ListItem", "position": 2, "name": "과천시", "item": "{BASE_URL}/" }}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "과천시 어느 지역까지 방문할 수 있나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "중앙동, 갈현동, 원문동, 별양동, 부림동, 과천동, 문원동 일곱 개 대표동을 기준으로 안내합니다. 관문동·주암동·막계동은 관련 대표동과 생활권 페이지에서 함께 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "정부과천청사역이나 과천역 근처도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "정부과천청사역, 과천역, 대공원역, 경마공원역, 선바위역 역세권은 각 역 페이지에서 인접 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 주소 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "출장마사지와 홈타이는 어떻게 다른가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "두 가지 모두 방문형 관리 서비스이며, 홈타이는 자택·숙소 중심의 이용 방식을 가리키는 표현입니다. 차이와 이용 기준은 홈타이 이용 가이드에서 정리해 두었습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "추가 이동비가 붙나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "과천동, 문원동, 막계동 인접권처럼 차량 이동 기준이 달라지는 위치는 예약 시 추가 이동비 발생 여부를 미리 안내해 드립니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Care · 경기도 과천시 전지역</p>
    <h1>과천시 출장마사지 · 홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">정부과천청사·과천역·별양동·선바위까지, 계신 곳에서 받는 방문형 관리 서비스.<br>자택·숙소·사무실 인근 어디든 전화 한 통이면 예약 가능 여부를 바로 확인해 드립니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/reservation/">예약 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>7개</strong><span>대표동 안내</span></li>
      <li><strong>6개</strong><span>역세권 안내</span></li>
      <li><strong>9개</strong><span>생활권 안내</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<p class="lead">과천시 출장마사지를 찾는 분들은 보통 현재 위치에서 가까운 방문 가능 지역을 먼저 확인합니다. 이 페이지는 과천시 전체 구조를 설명하는 허브로, 대표동·역세권·생활권 안내와 예약 전 확인사항을 한곳에 정리했습니다.</p>

<section id="standard">
<h2>과천시에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
<p>과천시는 규모가 크지는 않지만 성격이 다른 생활권이 모여 있는 지역입니다. 정부과천청사와 과천역을 중심으로 한 행정·중심 생활권, 갈현동과 과천지식정보타운 주변의 신흥 생활권, 선바위역과 과천동을 중심으로 한 남부 생활권, 서울대공원과 문원동 주변의 외곽 생활권이 함께 있습니다. 그래서 과천시 홈타이를 예약할 때는 단순히 "과천 전지역 가능"만 보고 연락하기보다, 본인 위치가 어느 생활권에 속하는지 먼저 확인하는 편이 빠릅니다. 방문 가능 여부와 추가 이동비, 예약 가능 시간이 생활권마다 조금씩 다르기 때문입니다. {BRAND}는 대표동과 역세권을 나누어 안내해, 처음 이용하시는 분도 본인에게 맞는 페이지를 쉽게 찾을 수 있도록 구성했습니다. 과천시 공식 행정 구역 정보는 <a href="https://www.gccity.go.kr/" target="_blank" rel="noopener">과천시청 누리집</a>에서도 확인하실 수 있습니다.</p>
</section>

<section id="diff">
<h2>중앙동·별양동·갈현동·과천동 생활권 차이</h2>
<p>중앙동과 별양동은 과천시 안에서도 검색 의도가 가장 넓은 중심 생활권입니다. <a href="/jungang-dong/">중앙동 출장마사지</a> 안내는 정부과천청사역과 과천시청, 관문동 인접권을 중심으로 행정·업무 생활권을 다루고, <a href="/byeoryang-dong/">별양동 출장마사지</a> 안내는 과천역과 중심상권, 부림동 인접권을 중심으로 상권·역세권 성격을 다룹니다. 두 지역은 가깝지만 역할을 다르게 잡아 같은 설명이 반복되지 않게 했습니다. <a href="/galhyeon-dong/">갈현동 출장마사지</a> 안내는 과천지식정보타운과 인덕원 인접권 중심으로, <a href="/gwacheon-dong/">과천동 출장마사지</a> 안내는 선바위역·경마공원역·주암동 인접 생활권 중심으로 구성해, 같은 과천시라도 위치마다 이동 기준과 방문 조건이 어떻게 달라지는지 비교해 보실 수 있습니다.</p>
</section>

<section id="dongs">
<h2>대표동별 방문 가능 지역 안내</h2>
<p>과천시는 서울 자치구처럼 숫자 행정동이 많은 구조가 아니라, 행정동 기준 일곱 개 대표 지역을 중심으로 안내합니다. 관문동은 중앙동, 주암동은 과천동, 막계동은 문원동 본문과 생활권 페이지에서 보조 설명합니다. 단순히 법정동을 늘려 얇은 페이지를 만들지 않습니다.</p>
<ul class="card-grid">
<li><a href="/jungang-dong/">중앙동</a></li>
<li><a href="/galhyeon-dong/">갈현동</a></li>
<li><a href="/wonmun-dong/">원문동</a></li>
<li><a href="/byeoryang-dong/">별양동</a></li>
<li><a href="/burim-dong/">부림동</a></li>
<li><a href="/gwacheon-dong/">과천동</a></li>
<li><a href="/munwon-dong/">문원동</a></li>
</ul>
<p><a href="/wonmun-dong/">원문동 출장마사지</a> 안내는 과천대로와 갈현동·별양동 인접권을, <a href="/burim-dong/">부림동 출장마사지</a> 안내는 과천역과 관문체육공원 인접권을, <a href="/munwon-dong/">문원동 출장마사지</a> 안내는 대공원역과 서울대공원·막계동 인접 생활권을 중심으로 작성했습니다. 거주하시거나 머무시는 동을 선택해 자세한 방문 조건을 확인해 주세요.</p>
</section>

<section id="stations">
<h2>정부과천청사역·과천역·선바위역 역세권 안내</h2>
<p>역세권 페이지는 과천시 지역 안내에서 중요한 역할을 합니다. 정부과천청사역, 과천역, 대공원역, 경마공원역, 선바위역은 역명 기준 한 개 페이지만 운영하며, 출구별로 나누거나 예정역을 미리 만들지 않습니다. 인덕원역은 안양시 성격이 강해 과천에서는 인접 생활권으로만 안내합니다.</p>
<ul class="card-grid">
<li><a href="/station/government-complex-gwacheon-station/">정부과천청사역</a></li>
<li><a href="/station/gwacheon-station/">과천역</a></li>
<li><a href="/station/seoul-grand-park-station/">대공원역</a></li>
<li><a href="/station/seoul-racecourse-park-station/">경마공원역</a></li>
<li><a href="/station/seonbawi-station/">선바위역</a></li>
<li><a href="/station/indeogwon-nearby-area/">인덕원역 인접 생활권</a></li>
</ul>
<p>생활권 단위로 더 넓게 보고 싶다면 <a href="/area/">과천 생활권 안내</a>에서 정부과천청사·중앙동, 과천역·별양동, 갈현동·지식정보타운 등 아홉 개 생활권을 함께 확인하실 수 있습니다.</p>
</section>

<section id="hometai-check">
<h2>과천시 홈타이 예약 전 확인사항</h2>
<p>과천시 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 확인한 뒤 이용하는 방문형 관리 서비스입니다. 예약 전에는 방문 가능 지역, 예약 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 개인정보 처리 기준을 먼저 확인하는 것이 좋습니다. 정부과천청사역과 과천역처럼 접근성이 좋은 지역도 있지만, 과천동과 주암동 인접권, 문원동과 막계동 인접권은 시간대에 따라 차량 이동 기준이 달라질 수 있습니다. 자세한 절차는 <a href="/reservation/">예약 안내</a>에서, 자택·숙소·사무실 인근 이용 전 점검 항목은 <a href="/guide/">이용 전 확인사항</a>에서 확인하실 수 있습니다. 출장마사지와 홈타이의 차이가 궁금하시면 <a href="/hometai/">홈타이 이용 가이드</a>를 참고해 주세요.</p>
</section>

<section id="policy">
<h2>과천시 페이지 중복 방지 운영 기준</h2>
<p>이 사이트는 같은 본문에서 지역명만 바꾸는 방식으로 페이지를 늘리지 않습니다. 관문동·주암동·막계동 같은 법정동을 각각 얇은 페이지로 만들면 본문이 비슷해질 위험이 크기 때문에, 일곱 개 대표동을 중심으로 만들고 작은 법정동은 관련 대표동과 생활권 페이지에서 보조 설명합니다. 과천역 페이지와 별양동 페이지는 같은 문장을 쓰지 않고 역세권 기준과 지역 기준을 나누어 작성했고, 갈현동 페이지와 지식정보타운 생활권 페이지도 중복 문장을 피했습니다. 예정역이나 미개통역은 단독 색인 페이지로 만들지 않고 본문에서만 보조 설명합니다. 정보형 안내 톤을 유지하며, 허위 후기나 과장된 할인 문구, 선정적 표현은 사용하지 않습니다.</p>
</section>

<section id="how">
<h2>과천시 출장마사지 사이트 이용 방법</h2>
<p>먼저 본인 위치가 어느 대표동 또는 역세권에 가까운지 확인하고, 해당 페이지에서 방문 조건과 예약 가능 시간을 본 뒤 전화로 예약하시면 됩니다. 동 페이지와 역 페이지, 생활권 페이지 중 어느 쪽을 보셔도 예약 기준은 같으니 본인에게 익숙한 기준으로 보시면 됩니다. 위치와 희망 시간만 정해지면 나머지는 예약 상담에서 함께 맞춰 드립니다.</p>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>과천시 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 방문 위치와 희망 시간을 알려주시면 가능 여부와 추가 이동비를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "과천시 출장마사지｜정부과천청사·과천역·별양동 홈타이 지역 안내",
    "desc": "과천시 출장마사지·홈타이 예약 전 정부과천청사, 과천역, 별양동, 갈현동, 선바위 생활권을 확인하세요.",
    "h1": "과천시 출장마사지 · 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [("과천시", None)],
    "hero": _HERO,
}
