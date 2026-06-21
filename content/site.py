# 사이트 공통 설정
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://www.barogo-gwacheon.example.com"

BRAND = "바로GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 텔레그램 문의 채널 (푸터 오렌지 버튼)
TELEGRAM_BUILD = "https://t.me/googleseolab"   # 웹사이트 제작문의
TELEGRAM_PARTNER = "https://t.me/googleseolab"  # 제휴문의

# 과천 메인 경로 — 광역(경기) 구조 안에서 과천시를 둔다.
GWACHEON_HOME = "/"

# 상단 메뉴 — 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명만 표시한다.
NAV = [
    ("과천 홈", "/", []),
    ("지역별 안내", "/#dongs", [
        ("중앙동", "/jungang-dong/"),
        ("갈현동", "/galhyeon-dong/"),
        ("원문동", "/wonmun-dong/"),
        ("별양동", "/byeoryang-dong/"),
        ("부림동", "/burim-dong/"),
        ("과천동", "/gwacheon-dong/"),
        ("문원동", "/munwon-dong/"),
    ]),
    ("역세권 안내", "/station/", [
        ("역 전체", "/station/"),
        ("정부과천청사역", "/station/government-complex-gwacheon-station/"),
        ("과천역", "/station/gwacheon-station/"),
        ("대공원역", "/station/seoul-grand-park-station/"),
        ("경마공원역", "/station/seoul-racecourse-park-station/"),
        ("선바위역", "/station/seonbawi-station/"),
        ("인덕원역 인접 생활권", "/station/indeogwon-nearby-area/"),
    ]),
    ("생활권 안내", "/area/", [
        ("생활권 전체", "/area/"),
        ("정부과천청사·중앙동", "/area/government-complex-jungang/"),
        ("과천역·별양동", "/area/gwacheon-station-byeoryang/"),
        ("갈현동·지식정보타운", "/area/galhyeon-knowledge-town/"),
        ("원문동·과천대로", "/area/wonmun-gwacheon-daero/"),
        ("부림동·관문체육공원", "/area/burim-gwanmun-park/"),
        ("과천동·선바위", "/area/gwacheon-seonbawi/"),
        ("서울대공원·문원동", "/area/seoul-grand-park-munwon/"),
        ("경마공원·주암동", "/area/racecourse-juam/"),
        ("인덕원·갈현 인접", "/area/indeogwon-galhyeon-nearby/"),
    ]),
    ("예약 안내", "/reservation/", [
        ("예약 가능 지역 확인", "/reservation/#area"),
        ("예약 가능 시간 안내", "/reservation/#hours"),
        ("추가 이동비 안내", "/reservation/#move"),
        ("결제 방식 안내", "/reservation/#payment"),
        ("예약 변경 안내", "/reservation/#change"),
        ("취소 기준 안내", "/reservation/#cancel"),
    ]),
    ("이용 전 확인사항", "/guide/", [
        ("방문 가능 주소 확인", "/guide/#address"),
        ("자택 이용 전 확인사항", "/guide/#home"),
        ("숙소 이용 전 확인사항", "/guide/#stay"),
        ("사무실 인근 이용 전 확인", "/guide/#office"),
        ("개인정보 처리 기준", "/guide/#privacy"),
        ("고객 안전 안내", "/guide/#safety"),
        ("불법·선정적 서비스 불가", "/guide/#prohibited"),
    ]),
    ("홈타이 이용 가이드", "/hometai/", [
        ("홈타이란?", "/hometai/#what"),
        ("출장마사지와 홈타이 차이", "/hometai/#diff"),
        ("과천시 홈타이 이용 전 기준", "/hometai/#standard"),
        ("지역별 이동 기준", "/hometai/#move"),
        ("추가 비용 확인 기준", "/hometai/#cost"),
        ("처음 이용하는 고객 안내", "/hometai/#first"),
    ]),
    ("고객센터", "/support/", [
        ("문의하기", "/support/#contact"),
        ("자주 묻는 질문", "/support/#faq"),
        ("운영 기준", "/support/#policy"),
        ("사이트 소개", "/about/"),
        ("개인정보 처리방침", "/support/privacy/"),
        ("이용약관", "/support/terms/"),
    ]),
]
