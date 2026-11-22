# SEOEN Journal — 인수인계 (ChatGPT·다른 AI·사람용)

이 저장소만 있으면 누구든 이어서 발행할 수 있어요. 사이트는 GitHub Pages(main / root)로 자동 공개됩니다.

- 공개 주소: https://itsserahwang-lang.github.io/seoen-journal/
- 저장소: https://github.com/itsserahwang-lang/seoen-journal
- 규칙(필독): `ops/README.md`(공통 발행 절차 G0–G5) + 폴더별 사양 `ops/issues.md`, `ops/econ.md`, `ops/momentum.md`, `ops/retail.md`, `ops/fragrance.md`, `ops/editorial.md`

## 1. 사이트 구조 한눈에

| 폴더 | 내용 | 주기 | 사양 |
|---|---|---|---|
| `issues/` | 데일리 뷰티 브리핑(11개 패널) | 매일 | ops/issues.md |
| `econ/` | Economy 탭(공개용 경제 브리핑) | 평일 | ops/econ.md |
| `momentum/` | Stocks 탭 아래 모멘텀 브리핑 | 평일 | ops/momentum.md |
| `retail/` | Retail Rank(5개 채널) | 일요일 | ops/retail.md |
| `fragrance/` | Fragrance Lookbook | 토요일 | ops/fragrance.md |
| `editorial/` | VOGUE·ELLE 월간 에디토리얼 | 매월 24일 | ops/editorial.md |

- 각 폴더 = `YYYY-MM-DD.html`(조각 HTML, doctype·style·script 없음) + `index.json`(맨 앞에 최신 항목).
- `index.html`(디자인·스크립트)은 고정. 콘텐츠 작업에서는 건드리지 않습니다.
- 그림은 사이트가 자동으로 그리는 라인 아트(`data-art`, `data-bottle`, `data-shape` 키). 사진·로고는 넣지 않습니다.

## 2. 발행 순서 (매번 동일)

1. `git pull` 로 최신 받기
2. 해당 폴더의 직전 파일을 열어 마크업을 그대로 따라 새 날짜 파일 작성 (또는 `tools/` 스크립트 사용)
3. `index.json` 맨 앞에 새 항목 추가
4. 그 폴더만 `git add` → 커밋 → `git pull --rebase` → `git push origin main`
5. 1~3분 뒤 `https://itsserahwang-lang.github.io/seoen-journal/<폴더>/<날짜>.html` 이 200인지 확인

## 3. tools/ — 지금까지 쓴 생성 스크립트 (Python 3, 외부 라이브러리 없음)

| 파일 | 만드는 것 | 쓰는 법 |
|---|---|---|
| `tools/gen_issue.py` (+ `helpers.py`) | issues/ 하루치 | 날짜·기사 데이터(top, cards 등)를 새로 채우고 `python3 tools/gen_issue.py .` |
| `tools/gen_econ.py` | econ/ | 같은 방식 |
| `tools/gen_momentum.py` | momentum/ | 같은 방식 |
| `tools/gen_retail.py` | retail/ | 순위 데이터 리스트만 교체 |
| `tools/gen_fragrance.py` | fragrance/ | look()/cn() 호출 내용만 교체 |

- 스크립트는 '마지막으로 발행한 호'가 그대로 들어 있는 템플릿이에요. 날짜(파일명·index.json·제목)와 내용 데이터만 바꿔서 실행하세요.
- 인자 `.` = 저장소 루트. 실행하면 해당 폴더의 html과 index.json이 갱신됩니다.
- 실행 후 브라우저에서 `python3 -m http.server` 로 열어 "이 호를 불러오지 못했어요" 문구가 없는지 확인하세요.

## 4. 반드시 지킬 것

- 숫자·가격·노트는 **원문을 열어 확인한 값만**. 확인 못 하면 "확인 불가/N/A" 또는 "새 소식 없음".
- 출처 링크 필수, 인용은 출처당 15단어 미만.
- vogue.com·elle.com·allure.com·harpersbazaar.com·wwd.com·businessoffashion.com·fragrantica·basenotes 는 열지 않음 → 다른 매체 보도로만 "via" 표기.
- 공개 사이트: 개인 일정·연락처·이메일·보유 종목·계좌 등 개인 정보 금지. 경제 탭에는 '내 집 마련 관점'·면접 대비·일정 내용 금지.
- 투자 정보는 "규칙 기반 정보 정리, 투자 권유 아님" 문구 유지. 화장품 효능 과장 금지.
- 다른 폴더·`index.html`·`ops/`는 콘텐츠 작업 중 수정하지 않기. 강제 푸시 금지.

## 5. 모멘텀 현재 상태 (11/20 기준)

- 신호등 🟡, 편입: 코스맥스(기준가 ₩280,500), 일라이 릴리($1,443.50), 코스트코($1,106.21) — 모두 11/16 편입, 각 20%, 현금 40%.
- 교체선: 기준가 대비 −8% (LLY $1,328.02). 11/19 종가 기준 LLY −6.4% '주의'.
- 대기 후보: JNJ, KO.

## 6. ChatGPT에 붙여 넣을 시작 프롬프트 (예시)

> 너는 내 GitHub 저장소 itsserahwang-lang/seoen-journal 의 정적 사이트 'SEOEN Journal'을 이어서 발행하는 편집자야. 먼저 ops/HANDOFF.md, ops/README.md, 그리고 오늘 작업 폴더의 ops/<폴더>.md 를 읽고 규칙을 그대로 따라. 직전 호 파일의 마크업을 그대로 따라서 오늘 날짜(한국 시간) 새 파일과 index.json 항목을 만들어. 숫자·가격은 원문을 직접 확인한 값만 쓰고, 확인 못 한 칸은 비워. 완성되면 그 폴더만 main 에 커밋·푸시하고, 결과를 ops/<폴더>.md 의 '알림' 형식으로 요약해 줘.
