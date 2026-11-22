import os, sys, json
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'helpers.py'),encoding='utf-8').read())
U=dict(st='https://www.cosinkorea.com/news/article.html?no=58772',ch='https://www.cmn.co.kr/sub/news/news_view.asp?news_idx=51644',tt='https://www.cmn.co.kr/sub/news/news_view.asp?news_idx=51645',
 ak='https://www.cmn.co.kr/sub/news/news_view.asp?news_idx=51647',tm='https://www.cmn.co.kr/sub/news/news_view.asp?news_idx=51643')
top=[
 dict(t=("Beauty stocks hold up in a 'Black Friday' week","AI 거품론 '검은 금요일'에도 화장품주 선방"),
      s=("KOSPI and KOSDAQ each fell more than 7% on the week — KOSPI to 4,869.96 and KOSDAQ to 645.68, with sell sidecars triggered on Nov 20 — yet 20 of 30 tracked beauty stocks rose.","코스피·코스닥이 한 주 동안 각각 7% 넘게 빠져 코스피 4,869.96, 코스닥 645.68으로 마감했고 20일엔 매도 사이드카까지 발동됐지만, 주요 화장품주 30곳 중 20곳이 올랐어요."),
      why="AI·반도체에서 빠진 돈이 실적이 확인된 소비재로 옮겨가고 있어요 — 화장품이 '방어 업종'으로 읽히기 시작했어요.",url=U['st'],src='코스인코리아닷컴'),
 dict(t=("Chanel opens a St. Moritz-inspired holiday pop-up in Seongsu","샤넬, 2년 만에 성수 '홀리데이 팝업'…생모리츠 콘셉트"),
      s=("Running Nov 21–Dec 31 in Seongsu, the pop-up draws on Gabrielle Chanel's winter retreat in St. Moritz and sells limited holiday items; visits are booked through the Chanel Beauty KakaoTalk channel, with walk-ins also allowed.","11월 21일부터 12월 31일까지 성수에서 열리며, 가브리엘 샤넬의 겨울 휴양지 생모리츠에서 영감을 받았고 홀리데이 한정 제품을 선보여요. 샤넬 뷰티 카카오톡 채널로 사전 예약하고 현장 방문도 가능해요."),
      why="럭셔리 브랜드도 '장소의 이야기'(겨울 휴양지)로 경험을 팔아요 — 호텔 시즌 콘셉트에 그대로 쓸 수 있어요.",url=U['ch'],src='CMN'),
 dict(t=("TIRTIR's Seongsu flagship wins a Red Dot award","티르티르 성수 플래그십, 레드닷 디자인 어워드 수상"),
      s=("The 'Shade Valley' store, designed with studio Labotory, won in Red Dot's Brands & Communication Design category; visitors can test the brand's full range of shades.","디자인 스튜디오 라보토리와 만든 '셰이드 밸리' 콘셉트 매장이 레드닷 브랜드&커뮤니케이션 디자인 부문에서 수상했어요. 전 제품과 모든 셰이드를 직접 테스트할 수 있어요."),
      why="'모든 색을 다 바를 수 있는' 공간이 곧 브랜드 메시지(셰이드 다양성)가 됐어요.",url=U['tt'],src='CMN')]
def top3():
    o='<div class="top3">'
    for i,t in enumerate(top,1): o+=f'<div class="t"><span class="n">{i}</span><div>{bi(t["t"][0],t["t"][1],"h3")}{sum_(*t["s"])}<p class="ko">{e(t["why"])}</p>{read(t["url"],t["src"])}</div></div>'
    return o+'</div>'
glob=[]
launch=[]
mkt=[dict(kw='Pharmacy Shelf',srcl='CMN · RETAIL',art='store',meta='CMN — Seoul · Nov 21',c1='gold',c2='ivory',
  t=("TONYMOLY enters the pharmacy inside Musinsa Beauty Hongdae","토니모리, 무신사 뷰티 홍대 '온누리약국' 입점"),
  s=("Products are now at Beauty Onnuri Pharmacy on B1 of Musinsa Beauty Hongdae, led by the Ceramide Mochi Toner (ceramide, panthenol).","무신사 뷰티 홍대점 지하 1층 뷰티온누리약국에 입점했고, 세라마이드·판테놀을 담은 세라마이드 모찌 토너가 대표 제품이에요."),
  why=("Pharmacy shelves inside fashion-beauty stores lend 'derma' credibility to mass brands.","패션·뷰티 매장 속 약국 매대는 대중 브랜드에 '더마' 신뢰를 더해요."),url=U['tm'],src='CMN')]
hotel=[]
brand=[]
empty_brand='<p class="empty"><span class=" l-en">Sulwhasoo · Hera · d\'Alba · Sisley · Numbuzin · SKIN1004 · Torriden · Anua · Beauty of Joseon — No new updates</span><span class=" l-ko">설화수 · 헤라 · 달바 · 시슬리 · 넘버즈인 · 스킨1004 · 토리든 · 아누아 · 조선미녀 — 새 소식 없음</span></p>'
insight=[("Beauty as a defensive sector.","하락장에서도 화장품주 30곳 중 20곳이 올랐어요. 실적이 확인된 소비재는 불황에도 버틴다는 사실을 브랜드 사업계획서에 근거로 쓰세요."),
         ("Borrow a destination.","샤넬은 '생모리츠'라는 장소를 빌려 겨울 팝업을 만들었어요. SEOEN 호텔의 계절 패키지도 '어디의 겨울'이라는 이야기로 설계해 보세요."),
         ("Let people try everything.","티르티르처럼 전 셰이드를 체험하게 하는 공간 자체가 디자인 상을 받는 시대예요.")]
srcs=[(U['st'],"[11월 4주 화장품 주가] 검은 금요일",'코스인코리아닷컴'),(U['ch'],'샤넬 홀리데이 팝업','CMN'),(U['tt'],'티르티르 성수 레드닷 수상','CMN'),(U['tm'],'토니모리 무신사 뷰티 온누리약국 입점','CMN'),(U['ak'],'애경산업 에코바디스 실버 메달','CMN')]
news=('<div class="panel" data-p="news">'+sec('Top 3 Today','오늘의 핵심',top3())+sec('K-Beauty Global','K-뷰티 글로벌 시장',empty())+sec('Wellness Hotels & Spas','웰니스 호텔·스파',empty())
 +sec('Skincare & Launches','스킨케어·신제품',empty())+sec('Marketing & Influencers','마케팅·인플루언서',cards(mkt))+sec('Hotel × Beauty & Travel','호텔 × 뷰티 & 트래블',empty())
 +sec('Brand Watch','브랜드 워치',empty_brand)
 +sec('Insight for Seojin','서진님 인사이트','<div class="ins">'+''.join(f'<div class="row"><h3>{e(a)}</h3><p class="ko" style="border:0;padding:0">{e(b)}</p></div>' for a,b in insight)+'</div>')
 +sec('Sources','출처','<ul class="src">'+''.join(f'<li><a href="{e(u)}" target="_blank" rel="noopener">{e(t)}</a> — {e(s)}</li>' for u,t,s in srcs)+'</ul>')+'</div>')
mag=('<div class="panel" data-p="mag"><section><div class="sh"><h2>Magazine</h2><small>패션 · 뷰티 · 기술 산업</small></div>'+empty()+'</section></div>')
econslot='<div class="panel" data-p="econ"><div class="econ-slot"></div></div>'
prev=open(os.path.join(R,'issues/2026-11-21.html'),encoding='utf-8').read()
macro=prev[prev.find('<div class="panel" data-p="macro">'):prev.find('<div class="panel" data-p="stocks">')]
stocks=('<div class="panel" data-p="stocks"><section><div class="sh"><h2>Stocks</h2><small>K-뷰티 주가 · 주간</small></div>'
 '<div class="disc"><span class=" l-en">Information only, not investment advice. Check your brokerage app before any decision.</span><span class=" l-ko">투자 권유가 아닌 정보 정리예요. 결정 전에는 증권사 앱의 실시간 시세를 확인하세요.</span></div>'
 '<div class="tbl"><table><thead><tr><th>'+bi('Item','항목')+'</th><th>'+bi('Close / result','종가·결과')+'</th><th>'+bi('Week','주간')+'</th><th>'+bi('Note','비고')+'</th></tr></thead><tbody>'
 '<tr><td>'+bi('KOSPI','코스피')+'</td><td>4,869.96</td><td>'+bi('down 7%+','7% 이상 하락')+'</td><td>'+bi('Sell sidecar on Nov 20','20일 매도 사이드카')+'</td></tr>'
 '<tr><td>'+bi('KOSDAQ','코스닥')+'</td><td>645.68</td><td>'+bi('down 7%+','7% 이상 하락')+'</td><td>'+bi('Sell sidecar on Nov 20','20일 매도 사이드카')+'</td></tr>'
 '<tr><td>'+bi('30 beauty stocks tracked','주요 화장품주 30곳')+'</td><td>'+bi('20 up · 10 down','상승 20 · 하락 10')+'</td><td>11/16→11/20</td><td>'+bi('Defensive rotation','방어주로 자금 이동')+'</td></tr>'
 '</tbody></table></div>'+f'<div class="links"><a href="{e(U["st"])}" target="_blank" rel="noopener">코스인코리아닷컴 ↗</a></div><div class="mom-slot"></div></section></div>')
ingr=('<div class="panel" data-p="ingredients">'+sec('Ingredients','새로 뜨는 원료',empty())+'</div>')
makers=('<div class="panel" data-p="makers"><section><div class="sh"><h2>Makers</h2><small>제조사·원료사 최신 자료</small></div>'
 '<div class="legend"><p><span class="badge b-odm">ODM</span>'+bi('Develops the formula and manufactures it.','처방 개발부터 생산까지 맡아요.','span')+'</p><p><span class="badge b-oem">OEM</span>'+bi("Manufactures to the brand's own formula.",'브랜드가 준 처방대로 생산만 해요.','span')+'</p><p><span class="badge b-raw">RAW</span>'+bi('Supplies ingredients.','원료를 공급해요.','span')+'</p></div>'
 +cards([dict(badge=('ODM','Cosmax · Kolmar · Cosmecca'),kw='Q3 Profit Gap',srcl='COSINKOREA · MAKERS',art='chart',meta='코스인코리아닷컴 — Korea · Nov 21',c1='gold',c2='pink',
  t=("ODM Q3 profit growth: +95%, +40.5%, +0.1%","ODM 3분기 이익 증가율: +95%·+40.5%·+0.1%"),
  s=("Cosmax's operating profit rose about 95%, Kolmar Korea's 40.5% and Cosmecca Korea's just 0.1% year on year.","3분기 영업이익은 코스맥스 약 95%, 한국콜마 40.5% 늘었고, 코스메카코리아는 0.1% 증가에 그쳤어요."),
  why=("Same boom, very different margins — utilization and client mix decide ODM profits.","같은 호황에도 이익은 크게 달라요 — 가동률과 고객 구성이 ODM 수익을 갈라요."),url=U['st'],src='코스인코리아닷컴')])+'</section></div>')
marketing=('<div class="panel" data-p="marketing">'+sec('Marketing by Country','국가별 마케팅 동향',cards([dict(kw='Korea · Seongsu',srcl='CMN · KOREA',art='arch',meta='CMN — Seoul · Nov 21',c1='gold',c2='ivory',
  t=("Korea: Seongsu is the luxury pop-up stage","한국: 성수는 럭셔리 팝업의 무대"),
  s=("Chanel's holiday pop-up (Nov 21–Dec 31) and TIRTIR's award-winning flagship both sit in Seongsu.","샤넬 홀리데이 팝업(11/21~12/31)과 수상한 티르티르 플래그십이 모두 성수에 있어요."),
  why=("One district now hosts luxury, indie and tourist traffic together.","한 동네에 럭셔리·인디·관광객 유동이 모여 있어요."),url=U['ch'],src='CMN')]))+'</div>')
product=('<div class="panel" data-p="product">'+sec('Product Planning','상품 기획·개발',cards([dict(kw='Shade Valley',srcl='CMN · PRODUCT',art='lips',meta='CMN — Seoul · Nov 21',c1='pink',c2='gold',
  t=("Plan the full shade range as an experience","셰이드 라인업을 '경험'으로 기획하기"),
  s=("TIRTIR's flagship is built so visitors can test every product and shade in one space.","티르티르 플래그십은 모든 제품과 셰이드를 한 공간에서 테스트하도록 설계됐어요."),
  why=("A wide shade range is a product decision and a store-design decision at once.","넓은 셰이드 구성은 제품 결정이자 매장 설계 결정이에요."),url=U['tt'],src='CMN')]))+'</div>')
ra=('<div class="panel" data-p="ra">'+sec('RA · Regulation','RA·규제',cards([dict(kw='EcoVadis Silver',srcl='CMN · ESG',art='frame',meta='CMN — Korea · Nov 21',c1='ivory',c2='gold',
  t=("Aekyung earns EcoVadis Silver on its first rating","애경산업, 에코바디스 첫 평가 '실버'"),
  s=("Silver places it in the top 15% of rated companies; it also holds a KCGS integrated A grade for six straight years (2021–2026).","실버는 평가 기업 상위 15%예요. 한국ESG기준원 통합 A등급도 6년 연속(2021~2026) 받았어요."),
  why=("Global retailers increasingly ask suppliers for ESG ratings during onboarding.","해외 유통사는 입점·거래 단계에서 ESG 등급을 점점 더 요구해요."),url=U['ak'],src='CMN')]))+'</div>')
words=[("sidecar","n.","사이드카(프로그램 매매 일시 정지)","Sell sidecars were triggered on Nov 20."),("defensive sector","n.","경기 방어 업종","Beauty acted as a defensive sector."),
       ("pop-up","n.","팝업 스토어","Chanel opened a holiday pop-up."),("flagship","n.","플래그십(대표 매장)","TIRTIR's flagship won a design award."),("rating","n.","등급·평가","Aekyung earned an EcoVadis Silver rating.")]
english=('<div class="panel" data-p="english"><section><div class="sh"><h2>English Corner</h2><small>Word of the Day ×5</small></div><div class="words">'
 +''.join(f'<article class="card w"><div><span class="term">{e(a)}</span><span class="pos">{e(b)}</span></div><span class="kr">{e(c)}</span><p class="ex">{e(d)}</p></article>' for a,b,c,d in words)
 +'</div></section><section><div class="sh"><h2>Caption Lab</h2><small>인스타 캡션</small></div>'
 '<article class="card"><p class="cap">An Alpine kind of Sunday — wool, warm light, and nothing on the calendar.</p><p class="ko">알프스 같은 일요일 — 울, 따뜻한 빛, 그리고 비어 있는 캘린더.</p></article>'
 '<article class="card"><p class="cap">Every shade, every story.</p><p class="ko">모든 색에는 모든 이야기가 있어요.</p></article></section>'
 '<section><div class="sh"><h2>Sentence Breakdown</h2><small>원문 핵심 문장 해석</small></div><article class="card"><blockquote>"Brands &amp; Communication Design"</blockquote><span class="meta">Red Dot award category — CMN</span><dl class="bd">'
 '<dt>Structure 구조</dt><dd>Brands(명사) &amp; Communication(명사 수식) + Design(핵심 명사)</dd><dt>Key phrase 핵심 표현</dt><dd><i>communication design</i> — 브랜드 메시지를 시각·공간으로 전달하는 디자인</dd>'
 '<dt>Nuance 뉘앙스</dt><dd>매장 디자인이 \'제품 디자인\'이 아니라 \'커뮤니케이션\' 부문에서 상을 받았다는 점 — 공간이 곧 광고라는 뜻이에요.</dd></dl></article></section></div>')
issue=news+mag+econslot+macro+stocks+ingr+makers+marketing+product+ra+english
open(os.path.join(R,'issues/2026-11-22.html'),'w',encoding='utf-8').write(issue)
p=os.path.join(R,'issues/index.json'); a=json.load(open(p,encoding='utf-8')); a=[x for x in a if x.get('date')!='2026-11-22']
a.insert(0,{"date":"2026-11-22","weekday":"Sun","headline":top[0]['t'][0],"headline_ko":top[0]['t'][1]}); open(p,'w',encoding='utf-8').write(json.dumps(a,ensure_ascii=False,indent=1)+'\n'); print('ok',len(issue))
