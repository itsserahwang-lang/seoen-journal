# retail/ — 주간 유통 랭킹 Retail Rank (일요일 22:41 KST)

틱톡샵(미국)·아마존(미국)·올리브영·화해·얼타 5개 채널, 뷰티 전체(스킨케어·선케어·메이크업·헤어·바디·향수), 채널마다 Top 10. 공통 규칙은 ops/README.md.

## 1. 데이터 수집 (WebFetch 우선, 보조 WebSearch)
- 먼저 공식 랭킹 페이지를 엽니다: 아마존 https://www.amazon.com/Best-Sellers-Beauty-Personal-Care/zgbs/beauty · 올리브영 https://www.oliveyoung.co.kr/store/main/getBestList.do · 화해 https://www.hwahae.co.kr/rankings?english_name=trending&theme_id=5102 와 https://www.hwahae.co.kr/rankings?english_name=category&theme_id=2 · 얼타 https://www.ulta.com/promotion/all. 읽히면 그 순위가 1순위.
- 막혀 있으면 우회하지 않고(다른 도구·미러·캐시 금지) 공개 대체 출처를 쓰며 순위 기준을 정확히 표시:
  - 틱톡샵: FastMoss 블로그(https://www.fastmoss.com/blog/), EchoTik 주간 리포트 — 공개 기간 그대로 표기.
  - 아마존: 최근 7~14일 기사·공식 발표의 뷰티 순위·기획전 딜. 순위가 없으면 "이번 주 판매 순위 확인 불가" + 확인된 딜만 '프로모션' 기준.
  - 올리브영: 글로우픽 올리브영 입점 랭킹(https://www.glowpick.com/stores/21) — '인기순(소비자 랭킹, 판매량 아님)'. 올영세일 등은 공식 공지·기사로 확인되면 프로모션 칸.
  - 얼타: 공개 순위가 없으면 promotion 페이지의 리뷰 많은 제품(편집 기준) + 이번 주 프로모션.
- 제품마다: 브랜드, 제품명, 가격(통화), 용량, 특징(출처의 사실만, 효능 과장 금지), 프로모션, 판매량·매출·평점·리뷰 수. 없는 값은 비움. 평균가는 "≈… avg". Top 10을 못 채우면 '확인 불가 — 이유'.

## 2. retail/YYYY-MM-DD.html (직전 호를 그대로 따름)
- `<div class="panel" data-p="retail"><section class="retail">` 안에 머리글(.sh: "Retail Rank · Weekly / 유통 랭킹 · 주간", 해당 주 월~일), .lead, 채널 칩(.chips `data-f="all|tiktok|amazon|oliveyoung|hwahae|ulta"`, All만 pressed), .note-box(이번 주 기획 포인트 3개, 영·한), .disc(그림은 제품 형태 일러스트·실제 패키지 아님 + 그림을 누르면 채널 검색), 채널 순서대로 `<div class="ch" data-sub="…">`.
- 채널 블록: .ch-h(채널명·지역) → .ch-note(출처와 한계) → 리스트마다 .rl(.rl-h 안에 h4, .bs 순위 기준 배지: Sales rank 판매량순 / Revenue rank 매출순 / Popularity 인기순 / Trending 급상승 / Promotion 프로모션, .per 기간) + `<ol class="rks">` → 출처 `<a class="read">`.
- 제품 행: `<li class="rk"><span class="no">01</span><a class="pfl" href="채널 검색 URL" target="_blank" rel="noopener" aria-label="브랜드 제품명 — open on 채널 / 채널에서 보기"><svg class="pf" data-shape="…" …></svg><span class="go">↗</span></a><div class="rb"><span class="br">브랜드</span><h4>제품명</h4><dl class="rspec"><div><dt>(영·한)</dt><dd>값</dd></div>…</dl><p class="ft">특징</p><p class="promo"><b>%</b>프로모션</p></div></li>`. 값 없는 항목은 빼고, 확인 불가는 `<li class="rk gap">`.
- 채널 검색 URL(검색어 "브랜드 제품명" URL 인코딩): 틱톡 https://www.tiktok.com/search?q= / 아마존 https://www.amazon.com/s?k= / 올리브영 https://www.oliveyoung.co.kr/store/search/getSearchMain.do?query= / 화해 https://www.hwahae.co.kr/search?q= / 얼타 https://www.ulta.com/search?search=
- 제품 그림: 직전 호 끝 `<template class="pf-lib">` 의 16가지 SVG(bottle pump jar tube dropper mask liner compact perfume spray brush set lip patch pack tool) 중 고르고 `style="--t:R,G,B"`(스킨케어 205,181,138 / 메이크업 255,61,139 / 헤어 179,38,58 / 바디·향수 245,240,230). 이 template 은 새 호 `</section>` 뒤에 그대로 복사.
- retail/index.json 맨 앞: `{"date":"YYYY-MM-DD","week":"월요일날짜/일요일날짜"}`

## 알림
"🛍️ 주간 유통 랭킹 — [주간 날짜]" + 채널별 1위 5줄 + 기획 포인트 3줄 + https://itsserahwang-lang.github.io/seoen-journal/#retail. 확인 못 한 채널은 이유 한 줄.
