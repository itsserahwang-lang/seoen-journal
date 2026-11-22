# tools/

SEOEN Journal 발행용 Python 스크립트 모음입니다. 사용법과 규칙은 `ops/HANDOFF.md` 를 보세요.

각 스크립트는 마지막으로 발행한 호를 그대로 담은 템플릿이에요. 날짜와 데이터만 바꾼 뒤 저장소 루트에서 실행합니다.

```bash
python3 tools/gen_issue.py .      # issues/
python3 tools/gen_econ.py .       # econ/
python3 tools/gen_momentum.py .   # momentum/
python3 tools/gen_retail.py .     # retail/
python3 tools/gen_fragrance.py .  # fragrance/
```
