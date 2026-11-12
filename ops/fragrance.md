# fragrance/ — 주간 Fragrance Lookbook (토요일 10:23 KST)

향수 매니아·컬렉터를 위한 주간 룩북. 면세점·백화점에 입점한 니치/하이엔드 하우스와 한국 니치 브랜드 중심, 패션 매거진 룩북처럼 정제된 톤. 공통 규칙은 ops/README.md.

## 1. 조사
- 새 소식은 지난 7일, 라인업 소개는 기간 제한 없음(현재 판매 중인 제품만).
- 하우스 예: Frédéric Malle, Maison Francis Kurkdjian, Byredo, Le Labo, Diptyque, Kilian Paris, Creed, Serge Lutens, Penhaligon's, Maison Margiela Replica, Acqua di Parma, Jo Malone London, Tom Ford Private Blend, Guerlain L'Art & la Matière, Hermès Hermessence. 한국 니치: Tamburins, Nonfiction, Granhand 등.
- 읽어도 되는 출처: 브랜드 공식 사이트·보도자료, 롯데·신라·신세계·현대 면세점·백화점 공개 페이지, Now Smell This, CaFleureBon, FashionNetwork, 한국·호주판 매거진의 향수 기사, 신뢰할 만한 언론. Fragrantica·Basenotes는 열지 않습니다.
- 노트·조향사·출시 연도·농도·가격은 확인한 값만. 가격은 통화·용량·판매처·확인 날짜와 함께(예: "₩—,000 · 100ml · 신라면세점 · 11/14 기준").
- 직전 4개 호에 실린 향수는 다시 싣지 않습니다(새 소식이 있는 경우 예외).

## 2. 구성 — 이번 주 테마 하나(예: "The Rose, Reconsidered")
- A. Duty-free Lineup / 면세점 라인업 — 3~4개 (`data-sub="dutyfree"`)
- B. New Launches & Perfumers / 신제품·조향사 — 2~3개 (`launch`)
- C. Korean Niche / 한국 니치 — 2개 (`korea`)
- D. Collector's Notes / 컬렉터 노트 — 노트·어코드 해설, 리포뮬레이션, 레이어링 2~3개 (`notes`)

## 3. fragrance/YYYY-MM-DD.html
```html
<div class="panel" data-p="fragrance"><section class="fragrance">
<header class="fr-mast"><span class="fr-kick">Fragrance Lookbook · Vol. NNN</span><h2 class="fr-title"><span class="l-en">테마</span><span class="l-ko">테마</span></h2><p class="fr-dek"><span class="l-en">서문</span><span class="l-ko">번역</span></p><span class="fr-date">Nov 9 — Nov 15, 2026</span></header>
<div class="chips" role="group" aria-label="Filter / 분류"><button data-f="all" aria-pressed="true">All</button><button data-f="dutyfree" aria-pressed="false"><span class="l-en">Duty-free</span><span class="l-ko">면세점</span></button><button data-f="launch" aria-pressed="false"><span class="l-en">Launches</span><span class="l-ko">신제품</span></button><button data-f="korea" aria-pressed="false"><span class="l-en">Korean niche</span><span class="l-ko">한국 니치</span></button><button data-f="notes" aria-pressed="false"><span class="l-en">Collector's notes</span><span class="l-ko">컬렉터 노트</span></button></div>
<div class="sh sub" data-sub="dutyfree"><h2><span class="l-en">Duty-free Lineup</span><span class="l-ko">면세점 라인업</span></h2></div>
<article class="look" data-sub="dutyfree">   <!-- 2·4번째 룩은 class="look flip" -->
 <figure class="lk-art" data-bottle="flacon|round|column|cube|bell|stout" data-tone="champagne|rose|bordeaux|ivory|noir|sage|iris" data-notes="rose, patchouli, incense" aria-hidden="true"><span class="no">01</span><span class="cap">Rose · Patchouli · Incense</span></figure>
 <div class="lk-body"><span class="lk-house">하우스</span><h3 class="lk-name">향수명(원어)</h3><span class="lk-meta">농도 · 조향사 · 연도</span>
 <dl class="pyr"><div><dt><span class="l-en">Top</span><span class="l-ko">탑</span></dt><dd><span class="l-en">notes</span><span class="l-ko">노트</span></dd></div>(Heart/미들, Base/베이스)</dl>
 <div class="sum"><p class="en">인상·무드 2문장</p><p class="kot">번역</p></div>
 <dl class="lk-spec"><div><dt><span class="l-en">Price</span><span class="l-ko">가격</span></dt><dd>값</dd></div><div><dt><span class="l-en">Where</span><span class="l-ko">판매처</span></dt><dd>…</dd></div></dl>
 <p class="ko"><b>↳</b><span class="l-en">컬렉터·기획 관점</span><span class="l-ko">번역</span></p>
 <a class="read" href="출처URL" target="_blank" rel="noopener">Source / 출처 · 매체 ↗</a></div></article>
<article class="cn" data-sub="notes"><span class="cn-term">Chypre</span><p><span class="l-en">설명</span><span class="l-ko">번역</span></p><a class="read" href="출처URL" target="_blank" rel="noopener">Source ↗</a></article>
</section></div>
```
- data-bottle은 실제 병과 비율이 가장 가까운 일반 실루엣(실제 패키지 재현 아님). data-notes는 대표 노트 3개 영어. .no 는 01부터, .cap 은 노트 3개를 " · "로.
- 향 묘사는 주관적 인상으로, 효능·건강 효과 주장 금지. 광고·제휴 링크 금지.
- fragrance/index.json 맨 앞: `{"date":"YYYY-MM-DD","week":"월/일","title":"영어 테마","title_ko":"한국어 테마"}`. Vol. 번호 = 항목 수 + 1.

## 알림
"🌹 Fragrance Lookbook Vol. NNN — [테마]" + 실린 향수 목록(하우스 — 향수명) + https://itsserahwang-lang.github.io/seoen-journal/#fragrance
