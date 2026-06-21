# 페이지별 롱테일 내부링크 강화 — 모든 페이지 하단에 "함께 보면 좋은 안내" 블록을 붙인다.
# 키(key)는 page["path"] 와 동일(루트는 "").  앵커는 롱테일(지역명+서비스) 형태로 작성한다.

RELATED = {
    # 메인
    "": [
        ("중앙동 출장마사지 안내", "/jungang-dong/"),
        ("정부과천청사역 출장마사지 안내", "/station/government-complex-gwacheon-station/"),
        ("과천역·별양동 생활권 안내", "/area/gwacheon-station-byeoryang/"),
        ("과천 홈타이 이용 가이드", "/hometai/"),
        ("과천 출장마사지 예약 안내", "/reservation/"),
    ],
    # 대표동
    "jungang-dong/": [
        ("정부과천청사역 출장마사지 안내", "/station/government-complex-gwacheon-station/"),
        ("정부과천청사·중앙동 생활권 안내", "/area/government-complex-jungang/"),
        ("별양동 출장마사지 안내", "/byeoryang-dong/"),
        ("부림동 출장마사지 안내", "/burim-dong/"),
        ("과천 홈타이 이용 가이드", "/hometai/"),
    ],
    "galhyeon-dong/": [
        ("갈현동·지식정보타운 생활권 안내", "/area/galhyeon-knowledge-town/"),
        ("인덕원·갈현 인접 생활권 안내", "/area/indeogwon-galhyeon-nearby/"),
        ("인덕원역 인접 생활권 안내", "/station/indeogwon-nearby-area/"),
        ("원문동 출장마사지 안내", "/wonmun-dong/"),
        ("과천 출장마사지 이용 전 확인사항", "/guide/"),
    ],
    "wonmun-dong/": [
        ("원문동·과천대로 생활권 안내", "/area/wonmun-gwacheon-daero/"),
        ("갈현동 출장마사지 안내", "/galhyeon-dong/"),
        ("별양동 출장마사지 안내", "/byeoryang-dong/"),
        ("과천역 출장마사지 안내", "/station/gwacheon-station/"),
        ("과천 출장마사지 예약 가능 지역 확인", "/reservation/#area"),
    ],
    "byeoryang-dong/": [
        ("과천역 출장마사지 안내", "/station/gwacheon-station/"),
        ("정부과천청사역 출장마사지 안내", "/station/government-complex-gwacheon-station/"),
        ("과천역·별양동 생활권 안내", "/area/gwacheon-station-byeoryang/"),
        ("중앙동 출장마사지 안내", "/jungang-dong/"),
        ("부림동 출장마사지 안내", "/burim-dong/"),
    ],
    "burim-dong/": [
        ("과천역 출장마사지 안내", "/station/gwacheon-station/"),
        ("부림동·관문체육공원 생활권 안내", "/area/burim-gwanmun-park/"),
        ("별양동 출장마사지 안내", "/byeoryang-dong/"),
        ("중앙동 출장마사지 안내", "/jungang-dong/"),
        ("과천 출장마사지 예약 안내", "/reservation/"),
    ],
    "gwacheon-dong/": [
        ("선바위역 출장마사지 안내", "/station/seonbawi-station/"),
        ("경마공원역 출장마사지 안내", "/station/seoul-racecourse-park-station/"),
        ("과천동·선바위 생활권 안내", "/area/gwacheon-seonbawi/"),
        ("경마공원·주암동 인접 생활권 안내", "/area/racecourse-juam/"),
        ("과천 출장마사지 예약 가능 지역 확인", "/reservation/#area"),
    ],
    "munwon-dong/": [
        ("대공원역 출장마사지 안내", "/station/seoul-grand-park-station/"),
        ("서울대공원·문원동 생활권 안내", "/area/seoul-grand-park-munwon/"),
        ("과천동 출장마사지 안내", "/gwacheon-dong/"),
        ("과천 출장마사지 이용 전 확인사항", "/guide/"),
        ("과천 홈타이 이용 가이드", "/hometai/"),
    ],
    # 역세권
    "station/": [
        ("정부과천청사역 출장마사지 안내", "/station/government-complex-gwacheon-station/"),
        ("과천역 출장마사지 안내", "/station/gwacheon-station/"),
        ("선바위역 출장마사지 안내", "/station/seonbawi-station/"),
        ("과천 생활권별 안내", "/area/"),
        ("과천 대표동 지역 안내", "/#dongs"),
    ],
    "station/government-complex-gwacheon-station/": [
        ("중앙동 출장마사지 안내", "/jungang-dong/"),
        ("별양동 출장마사지 안내", "/byeoryang-dong/"),
        ("정부과천청사·중앙동 생활권 안내", "/area/government-complex-jungang/"),
        ("과천 출장마사지 예약 가능 시간 안내", "/reservation/#hours"),
    ],
    "station/gwacheon-station/": [
        ("별양동 출장마사지 안내", "/byeoryang-dong/"),
        ("부림동 출장마사지 안내", "/burim-dong/"),
        ("과천역·별양동 생활권 안내", "/area/gwacheon-station-byeoryang/"),
        ("과천 출장마사지 이용 전 확인사항", "/guide/"),
    ],
    "station/seoul-grand-park-station/": [
        ("문원동 출장마사지 안내", "/munwon-dong/"),
        ("서울대공원·문원동 생활권 안내", "/area/seoul-grand-park-munwon/"),
        ("과천동 출장마사지 안내", "/gwacheon-dong/"),
        ("과천 홈타이 이용 가이드", "/hometai/"),
    ],
    "station/seoul-racecourse-park-station/": [
        ("과천동 출장마사지 안내", "/gwacheon-dong/"),
        ("경마공원·주암동 인접 생활권 안내", "/area/racecourse-juam/"),
        ("선바위역 출장마사지 안내", "/station/seonbawi-station/"),
        ("과천 출장마사지 예약 안내", "/reservation/"),
    ],
    "station/seonbawi-station/": [
        ("과천동 출장마사지 안내", "/gwacheon-dong/"),
        ("과천동·선바위 생활권 안내", "/area/gwacheon-seonbawi/"),
        ("경마공원역 출장마사지 안내", "/station/seoul-racecourse-park-station/"),
        ("과천 홈타이 이용 가이드", "/hometai/"),
    ],
    "station/indeogwon-nearby-area/": [
        ("갈현동 출장마사지 안내", "/galhyeon-dong/"),
        ("갈현동·지식정보타운 생활권 안내", "/area/galhyeon-knowledge-town/"),
        ("인덕원·갈현 인접 생활권 안내", "/area/indeogwon-galhyeon-nearby/"),
        ("과천 출장마사지 예약 가능 지역 확인", "/reservation/#area"),
    ],
    # 생활권
    "area/": [
        ("정부과천청사·중앙동 생활권 안내", "/area/government-complex-jungang/"),
        ("과천역·별양동 생활권 안내", "/area/gwacheon-station-byeoryang/"),
        ("갈현동·지식정보타운 생활권 안내", "/area/galhyeon-knowledge-town/"),
        ("과천 역세권별 안내", "/station/"),
        ("과천 대표동 지역 안내", "/#dongs"),
    ],
    "area/government-complex-jungang/": [
        ("중앙동 출장마사지 안내", "/jungang-dong/"),
        ("정부과천청사역 출장마사지 안내", "/station/government-complex-gwacheon-station/"),
        ("별양동 출장마사지 안내", "/byeoryang-dong/"),
        ("과천 출장마사지 예약 안내", "/reservation/"),
    ],
    "area/gwacheon-station-byeoryang/": [
        ("별양동 출장마사지 안내", "/byeoryang-dong/"),
        ("과천역 출장마사지 안내", "/station/gwacheon-station/"),
        ("부림동 출장마사지 안내", "/burim-dong/"),
        ("과천 출장마사지 이용 전 확인사항", "/guide/"),
    ],
    "area/galhyeon-knowledge-town/": [
        ("갈현동 출장마사지 안내", "/galhyeon-dong/"),
        ("인덕원역 인접 생활권 안내", "/station/indeogwon-nearby-area/"),
        ("인덕원·갈현 인접 생활권 안내", "/area/indeogwon-galhyeon-nearby/"),
        ("원문동 출장마사지 안내", "/wonmun-dong/"),
    ],
    "area/wonmun-gwacheon-daero/": [
        ("원문동 출장마사지 안내", "/wonmun-dong/"),
        ("갈현동 출장마사지 안내", "/galhyeon-dong/"),
        ("별양동 출장마사지 안내", "/byeoryang-dong/"),
        ("과천 출장마사지 이용 전 확인사항", "/guide/"),
    ],
    "area/burim-gwanmun-park/": [
        ("부림동 출장마사지 안내", "/burim-dong/"),
        ("과천역 출장마사지 안내", "/station/gwacheon-station/"),
        ("별양동 출장마사지 안내", "/byeoryang-dong/"),
        ("과천 출장마사지 예약 안내", "/reservation/"),
    ],
    "area/gwacheon-seonbawi/": [
        ("과천동 출장마사지 안내", "/gwacheon-dong/"),
        ("선바위역 출장마사지 안내", "/station/seonbawi-station/"),
        ("경마공원·주암동 인접 생활권 안내", "/area/racecourse-juam/"),
        ("과천 홈타이 이용 가이드", "/hometai/"),
    ],
    "area/seoul-grand-park-munwon/": [
        ("문원동 출장마사지 안내", "/munwon-dong/"),
        ("대공원역 출장마사지 안내", "/station/seoul-grand-park-station/"),
        ("과천동 출장마사지 안내", "/gwacheon-dong/"),
        ("과천 출장마사지 이용 전 확인사항", "/guide/"),
    ],
    "area/racecourse-juam/": [
        ("과천동 출장마사지 안내", "/gwacheon-dong/"),
        ("경마공원역 출장마사지 안내", "/station/seoul-racecourse-park-station/"),
        ("선바위역 출장마사지 안내", "/station/seonbawi-station/"),
        ("과천 출장마사지 예약 안내", "/reservation/"),
    ],
    "area/indeogwon-galhyeon-nearby/": [
        ("갈현동 출장마사지 안내", "/galhyeon-dong/"),
        ("인덕원역 인접 생활권 안내", "/station/indeogwon-nearby-area/"),
        ("갈현동·지식정보타운 생활권 안내", "/area/galhyeon-knowledge-town/"),
        ("과천 출장마사지 예약 가능 지역 확인", "/reservation/#area"),
    ],
    # 정보 페이지
    "reservation/": [
        ("과천 출장마사지 이용 전 확인사항", "/guide/"),
        ("과천 홈타이 이용 가이드", "/hometai/"),
        ("과천역 출장마사지 안내", "/station/gwacheon-station/"),
        ("과천동 출장마사지 안내", "/gwacheon-dong/"),
    ],
    "guide/": [
        ("과천 출장마사지 예약 안내", "/reservation/"),
        ("과천 홈타이 이용 가이드", "/hometai/"),
        ("개인정보 처리방침", "/support/privacy/"),
        ("정부과천청사역 출장마사지 안내", "/station/government-complex-gwacheon-station/"),
    ],
    "hometai/": [
        ("과천 출장마사지 예약 안내", "/reservation/"),
        ("과천 출장마사지 이용 전 확인사항", "/guide/"),
        ("서울대공원·문원동 생활권 안내", "/area/seoul-grand-park-munwon/"),
        ("과천동 출장마사지 안내", "/gwacheon-dong/"),
    ],
    "support/": [
        ("사이트 소개", "/about/"),
        ("개인정보 처리방침", "/support/privacy/"),
        ("이용약관", "/support/terms/"),
        ("과천 출장마사지 예약 안내", "/reservation/"),
    ],
    "about/": [
        ("과천 출장마사지 지역 안내", "/"),
        ("과천 출장마사지 예약 안내", "/reservation/"),
        ("고객센터", "/support/"),
        ("과천 홈타이 이용 가이드", "/hometai/"),
    ],
    "support/privacy/": [
        ("이용약관", "/support/terms/"),
        ("고객센터", "/support/"),
        ("사이트 소개", "/about/"),
    ],
    "support/terms/": [
        ("개인정보 처리방침", "/support/privacy/"),
        ("고객센터", "/support/"),
        ("사이트 소개", "/about/"),
    ],
}


def render_related(path: str) -> str:
    links = RELATED.get(path)
    if not links:
        return ""
    items = "".join(f'<li><a href="{href}">{anchor}</a></li>' for anchor, href in links)
    return (
        '<section class="related" aria-label="관련 안내">'
        '<h2>함께 보면 좋은 안내</h2>'
        f'<ul class="related-grid">{items}</ul></section>'
    )
