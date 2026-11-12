# issues/ — SEOEN Journal · Daily Beauty Briefing (매일 08:07 KST)

매일 아침 뷰티 업계 매거진을 새 호로 발행합니다. 영어는 고급 업계·비즈니스 표현, 모든 항목에 자연스러운 한국어 번역을 함께 둡니다. 공통 규칙은 ops/README.md.

## 1. 조사 범위 (WebSearch, 필요 시 WebFetch)
- 기본은 지난 24시간 안에 발행된 기사·발표. news·mag 외 탭은 지난 7일까지 허용(최신 순, 날짜 표기).
- 기사로 쓰는 항목은 반드시 WebFetch로 열어 발행일·내용을 확인하고 원문 URL을 붙입니다.
- 국내 + 해외. 해외는 북미·남미, 두바이(UAE·중동), 싱가포르 우선. 주제·지역별로 한국어·영어로 나눠 여러 번 검색.
- 직전 호(issues/ 가장 최근 파일)에 실은 기사는 다시 쓰지 않습니다.

## 2. 11개 패널 — `<div class="panel" data-p="…">`, 이 순서
1. **news** — Beauty News: Top 3 Today + K-Beauty Global(아마존·틱톡샵·세포라·얼타·올리브영 등 유통, 북남미·두바이·싱가포르) + Wellness Hotels & Spas + Skincare & Launches + Marketing & Influencers + Hotel × Beauty & Travel(호텔×뷰티 협업 / 트래블 키트·항공 어메니티 / 스파·웰니스 프로그램; 7일 허용, 해설은 "서진님 웰니스 호텔·브랜드에 어떻게 접목할지" 한 문장) + Brand Watch(설화수·헤라·달바·시슬리 / 넘버즈인·스킨1004·토리든·아누아·조선미녀) + Insight for Seojin(2~3줄) + Sources
2. **mag** — Magazine: 패널 맨 위의 월간 'Editorial Monthly — VOGUE · ELLE'는 사이트가 editorial/ 에서 자동으로 붙이니 만들지 않습니다. 개별 패션 매거진 기사는 싣지 않고 산업 소식만: 필터 칩 `<div class="chips">` (All / Fashion / Beauty / Tech, `data-f="all|fashion|beauty|tech"`, All만 `aria-pressed="true"`), 카드마다 `data-sub="fashion|beauty|tech"`. 각 1~2개.
3. **econ** — 정확히 `<div class="panel" data-p="econ"><div class="econ-slot"></div></div>` 만(평일 경제 브리핑이 자동으로 채움).
4. **macro** — Industry Macro: 바이오·화장품 거시경제(최신 월 화장품 수출액·증감률, 국가·권역별 수출, 업계 지표, 주요 기업 실적·M&A). '한눈에 보기 → 그래프 → 표' 순서, 직전 호 macro 마크업을 따름:
   - `<p class="lead">` 한 줄 요약
   - 카드 4장: `<div class="kpis">` 안에 `<div class="kpi"><span class="k">라벨</span><span class="v">큰 숫자</span><span class="d">기간·증감(<b>강조)</span></div>` ×4
   - 막대 그래프 2~3개: `<div class="chart"><h3>제목</h3><p class="cs">단위</p><ul class="hb"><li title="툴팁"><span class="lb">항목</span><span class="tr"><span class="fl" style="width:NN%"></span></span><span class="vl">값</span></li>…</ul></div>` — width는 그래프 안 최댓값 대비(최댓값 90~95%), 한 그래프엔 같은 단위만, 역산 추정치는 `class="fl est"` + `<p class="fn">` 추정 방법. 막대 2~6개.
   - 표: `<div class="sh sub"><h2>At a glance — … / 한눈에 보는 표 — …</h2></div>` + `<div class="tbl"><table class="mini">` (지표 | 수치 | 기간, 기간은 "26.10", 증감은 `<small>`) — 수출 표와 기업·딜 표
   - `<p class="note">` 해설 + `<div class="links">` 출처
5. **stocks** — 상단 "투자 권유 아님"(.disc) + K-뷰티·바이오 주요 종목 표(종목, 주가, 등락, 기준일·시각, 출처) + 반드시 `<div class="mom-slot"></div>`(모멘텀 브리핑이 자동으로 붙음).
6. **ingredients** — 새로 뜨는 원료: 신원료·화제 성분, 효능 근거 수준과 광고 표현 주의점.
7. **makers** — 제조사·원료사: 맨 위 범례(.legend: ODM/OEM/RAW 정의) + 카드마다 배지(`<span class="badge b-odm|b-oem|b-raw">ODM · 회사</span>`). 탭 맨 위 회사 배너는 사이트가 자동으로 붙임.
8. **marketing** — 국가별 마케팅/퍼포먼스 동향: 한국 맨 앞, 그다음 미국·일본·동남아·중동.
9. **product** — 상품 기획·개발: 소비자 조사, 신제품 포맷, 패키지·제형 트렌드, 기획 시사점.
10. **ra** — RA·규제: 식약처, FDA(MoCRA), EU, 중국, 아세안의 표시·안전·기능성 규제 변화와 시행일.
11. **english** — English Corner: Word of the Day ×5, Caption Lab(데일리 럭셔리 톤 캡션 1~2개+번역), Sentence Breakdown(해외 기사 한 곳의 15단어 미만 구절 하나, 구조·표현·뉘앙스 풀이).

- 새 소식이 없으면 `<p class="empty">No new updates / 새 소식 없음</p>`.
- SEOEN 탭(index.html 고정), retail/·fragrance/·editorial/ 은 만들거나 건드리지 않습니다.

## 3. 마크업
- 제목은 `<h3 class=" l-en">` / `<h3 class=" l-ko">` 쌍.
- 기사 카드: `<article class="card"(mag는 data-sub)><div class="th" data-art="그림키" style="--c1:R,G,B;--c2:R,G,B;--x1:..%;--y1:..%;--x2:..%;--y2:..%" role="img" aria-label="키워드"><div class="ov">(makers는 배지)<span class="src">출처 · 섹션</span><span class="kw">2~3단어 키워드</span></div></div><div class="body"><span class="meta">출처 — 지역 · 날짜</span>제목쌍, sum, 해설, <a class="read" href="원문URL" target="_blank" rel="noopener">Read the article / 원문 기사 보기 · 출처 ↗</a></div></article>`. 모든 카드·Top 3 항목 아래 기사 링크 필수.
- 표: `<div class="tbl"><table>…</table></div>`, 머리글·지표명도 l-en/l-ko 쌍.
- issues/index.json 맨 앞: `{"date":"YYYY-MM-DD","weekday":"Wed","headline":"Top 3의 1번 영어 제목","headline_ko":"그 한국어 제목"}`

## 알림
- 성공: "🌿 SEOEN Journal — [날짜] 오늘 호가 발행됐어요" + Top 3 한국어 제목 3줄 + https://itsserahwang-lang.github.io/seoen-journal/
- 실패: 실패 단계·이유 한 줄 + Top 3와 원문 링크.
