import os,sys,json,html
R=sys.argv[1]; e=lambda t: html.escape(t,quote=True)
def bi(en,ko): return f'<span class="l-en">{e(en)}</span><span class="l-ko">{e(ko)}</span>'
def tbl(head,rows): return '<div class="tbl"><table><thead><tr>'+''.join(f'<th>{bi(*h)}</th>' for h in head)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{bi(*c) if isinstance(c,tuple) else e(c)}</td>' for c in r)+'</tr>' for r in rows)+'</tbody></table></div>'
def sh(en,ko): return f'<div class="sh sub"><h2>{bi(en,ko)}</h2></div>'
o=sh('Momentum Rotation Brief · Nov 20, 2026','모멘텀 로테이션 브리핑 · 2026년 11월 20일')
o+='<div class="disc">'+bi('Rule-based information only, not investment advice. Check live quotes and filings before any decision.','규칙 기반 정보 정리이며 투자 권유가 아니에요. 결정 전 실시간 시세와 공시를 확인하세요.')+'</div>'
o+='<p class="lead">'+bi('🟡 Conservative, leaning defensive. U.S. indexes fell over 2% (S&P 500 a fifth straight loss) even as KOSPI rose 1.39%. No new entries; LLY moves to caution at −6.4% from base.','🟡 보수적 유지, 방어 쪽으로 기울어요. 코스피는 1.39% 올랐지만 미국 3대 지수는 2% 넘게 빠졌어요(S&P500 5일 연속 하락). 신규 편입은 없고, LLY는 기준가 대비 −6.4%로 주의 단계예요.')+'</p>'
o+=sh('Market read · Nov 19','시장 흐름 · 11월 19일')
o+=tbl([('Market','시장'),('Move','등락'),('Note','메모')],[
 [('Korea','한국'),'KOSPI 5,137.89 (+1.39%) · KOSDAQ 684.81 (+3.32%)',('Late comeback on Anthropic IPO hopes; foreigners sold ₩403.4bn','앤트로픽 상장 기대에 막판 반등, 외국인 4,034억 원 순매도')],
 [('U.S.','미국'),'Dow −2.20% · S&P −2.03% · Nasdaq −2.23%',('Anthropic +17% on debut failed to lift AI; weak Philly Fed and claims','앤트로픽 첫날 +17%에도 AI주 약세, 필라델피아 지수·실업수당 부진')],
 [('Defensives','방어주'),('Mixed','혼조'),('Cosmax reversed from ₩313,000 intraday; LLY fell for a fourth day','코스맥스 장중 ₩313,000에서 반락, LLY 4일 연속 하락')]])
o+=sh('Selection','선별 종목')
o+=tbl([('Stock (ticker)','종목(티커)'),('Market','시장'),('Sector','섹터'),('Close 11/19','전일 종가 11/19'),('1M · 3M','1M · 3M'),('vs 52w high','신고가 대비'),('Entry · base','편입일·기준가'),('vs base','기준가 대비'),('Status','상태'),('Weight','비중')],[
 [('Cosmax (192820)','코스맥스 (192820)'),'KOSPI',('Beauty ODM','화장품 ODM'),'₩289,000 (−2.36%)',('N/A · N/A','N/A · N/A'),'−9.7% (₩320,000)','11/16 · ₩280,500','+3.0%',('Hold','유지'),'20%'],
 [('Eli Lilly (LLY)','일라이 릴리 (LLY)'),'NYSE',('Health care','헬스케어'),'$1,351.12 (−2.29%)',('N/A · N/A','N/A · N/A'),'−8.4% ($1,475.25)','11/16 · $1,443.50','−6.4%',('Caution · 1.6pp from the −8% line ($1,328.02)','주의 · 교체선(−8%, $1,328.02)까지 1.6%p'),'20%'],
 [('Costco (COST)','코스트코 (COST)'),'NASDAQ',('Consumer staples','필수소비재'),'$1,093.83 (−0.25%)',('N/A · N/A','N/A · N/A'),'−2.7% ($1,123.67)','11/16 · $1,106.21','−1.1%',('Hold · next earnings Dec 10','유지 · 다음 실적 12/10'),'20%']])
o+='<p class="note">'+bi('Weights unchanged: 20% each, U.S. 40% / Korea 20%, cash 40%. 20-day and 50-day lines were not shown by accessible sources, so those fences could not be checked today (N/A).','비중 변화 없음: 종목당 20%, 미국 40%·한국 20%, 현금 40%. 20일·50일선은 확인 가능한 출처에 없어 오늘은 해당 울타리를 점검하지 못했어요(N/A).')+'</p>'
o+=sh("Today's action check","오늘의 액션 체크")
o+='<ul class="ins">'+''.join(f'<li>{bi(a,b)}</li>' for a,b in [
 ('No change yet — but LLY is in caution: a close below $1,328.02 (−8% from base) would be a replacement signal.','아직 변경 없음 — 다만 LLY는 주의 단계예요. 종가가 $1,328.02(기준가 −8%) 아래로 내려가면 규칙상 교체 신호예요.'),
 ('Cosmax still +3.0% from base after giving back an intraday high of ₩313,000; Costco −1.1%.','코스맥스는 장중 ₩313,000에서 밀렸지만 기준가 대비 +3.0%, 코스트코는 −1.1%예요.'),
 ('Watch: the S&P 500 is on track for its worst week since April 2025 — waitlist entries stay frozen.','관찰: S&P500이 2025년 4월 이후 최악의 주간을 향하고 있어 대기 후보 편입은 보류해요.')])+'</ul>'
o+=sh('Waitlist','대기 후보')
o+=tbl([('Stock','종목'),('Evidence','근거'),('Why not now','이번에 제외한 이유')],[
 [('Johnson & Johnson (JNJ)','존슨앤드존슨 (JNJ)'),('1M +12.8% · all-time high 11/13','1M +12.8% · 11/13 사상 최고가'),('No new entries today; same sector as LLY','오늘 신규 편입 없음, LLY와 같은 섹터')],
 [('Coca-Cola (KO)','코카콜라 (KO)'),('All-time high 11/13 · 1M +7.9%','11/13 사상 최고가 · 1M +7.9%'),('No new entries today; same sector as COST','오늘 신규 편입 없음, COST와 같은 섹터')]])
o+=sh('Term of the Day','오늘의 투자 용어')
o+='<p class="lead">'+bi('Losing streak — consecutive down days. The S&P 500 has fallen five sessions in a row; streaks test whether rules are followed calmly.','연속 하락 — 며칠 연속 내리는 흐름이에요. S&P500은 5거래일 연속 하락했어요. 이럴 때일수록 정한 규칙을 차분히 지키는 게 중요해요.')+'</p>'
src=[('https://stockanalysis.com/quote/krx/192820/history/','StockAnalysis · Cosmax'),('https://stockanalysis.com/stocks/lly/history/','StockAnalysis · LLY'),('https://stockanalysis.com/stocks/cost/history/','StockAnalysis · COST'),
 ('https://www.fnnews.com/news/202611191701284704','파이낸셜뉴스 · 코스피 11/19'),('https://finance.yahoo.com/markets/stocks/articles/wall-street-ends-sharply-lower-210028386.html','Reuters · markets 11/19')]
o+='<div class="links">'+' '.join(f'<a class="read" href="{e(u)}" target="_blank" rel="noopener">{e(t)} ↗</a>' for u,t in src)+'</div>'
open(os.path.join(R,'momentum/2026-11-20.html'),'w',encoding='utf-8').write(o)
p=os.path.join(R,'momentum/index.json'); x=json.load(open(p,encoding='utf-8')); x=[i for i in x if i['date']!='2026-11-20']; x.insert(0,{"date":"2026-11-20"})
open(p,'w',encoding='utf-8').write(json.dumps(x,ensure_ascii=False,indent=1)+'\n'); print('ok',len(o))
