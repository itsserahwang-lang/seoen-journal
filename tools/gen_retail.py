import html, json, re, sys, os
from urllib.parse import quote
R = sys.argv[1]
e = lambda t: html.escape(t, quote=True)
prev = open(os.path.join(R,'retail/2026-11-11.html'),encoding='utf-8').read()
tpl = prev[prev.find('<template class="pf-lib">'):]
SH = {m.group(1): m.group(2) for m in re.finditer(r'<svg class="pf" data-shape="(\w+)" viewBox="0 0 48 64">(.*?)</svg>', tpl)}
def bi(en, ko): return f'<span class="l-en">{e(en)}</span><span class="l-ko">{e(ko)}</span>'
TONE = dict(skin='205,181,138', make='255,61,139', hair='179,38,58', body='245,240,230')
SEARCH = dict(tiktok='https://www.tiktok.com/search?q=', amazon='https://www.amazon.com/s?k=',
  oliveyoung='https://www.oliveyoung.co.kr/store/search/getSearchMain.do?query=', hwahae='https://www.hwahae.co.kr/search?q=', ulta='https://www.ulta.com/search?search=')
CHN = dict(tiktok=('TikTok','틱톡'), amazon=('Amazon','아마존'), oliveyoung=('Olive Young','올리브영'), hwahae=('Hwahae','화해'), ulta='Ulta')
def rk(ch, no, br, name, shape, tone, specs=(), ft=None, promo=None):
    q = quote(f'{br} {name}')
    cn = CHN[ch] if isinstance(CHN[ch], tuple) else (CHN[ch], CHN[ch])
    sp = ''.join(f'<div><dt>{bi(a,b)}</dt><dd>{e(v)}</dd></div>' for a,b,v in specs)
    return (f'<li class="rk"><span class="no">{no:02d}</span><a class="pfl" href="{SEARCH[ch]}{q}" target="_blank" rel="noopener" aria-label="{e(br+" "+name)} — open on {cn[0]} / {cn[1]}에서 보기">'
            f'<svg class="pf" data-shape="{shape}" viewBox="0 0 48 64" style="--t:{TONE[tone]}" role="img" aria-label="{e(name)}">{SH[shape]}</svg><span class="go">↗</span></a>'
            f'<div class="rb"><span class="br">{e(br)}</span><h4>{e(name)}</h4>' + (f'<dl class="rspec">{sp}</dl>' if sp else '')
            + (f'<p class="ft">{bi(*ft)}</p>' if ft else '') + (f'<p class="promo"><b>%</b>{bi(*promo)}</p>' if promo else '') + '</div></li>')
def gap(no, en, ko): return f'<li class="rk gap"><span class="no">{no}</span><p>{bi(en,ko)}</p></li>'
def rl(title, basis, per, items): return f'<div class="rl"><div class="rl-h"><h4>{bi(*title)}</h4><span class="bs">{bi(*basis)}</span><span class="per">{bi(*per)}</span></div><ol class="rks">{"".join(items)}</ol></div>'
def ch(sub, name, rg, note, lists, src):
    return (f'<div class="ch" data-sub="{sub}"><div class="ch-h"><h3>{e(name)}</h3><span class="rg">{rg}</span></div><p class="ch-note">{bi(*note)}</p>' + ''.join(lists)
            + ''.join(f'<a class="read" href="{e(u)}" target="_blank" rel="noopener">{bi("Source · "+t, "출처 · "+t)} ↗</a>' for u,t in src) + '</div>')
P = lambda v: ('Price','가격',v); V = lambda v: ('Size','용량',v); RV = lambda v: ('Rating · reviews','평점 · 리뷰',v)
U = lambda v: ('Units','판매량',v); G = lambda v: ('GMV','매출',v)

tiktok = ch('tiktok','TikTok Shop','US',("No official ranking; FastMoss estimates. No newer public week than Oct 19–25 at writing, so this list is unchanged from the last issue.","공식 랭킹이 없어 FastMoss 추정치를 써요. 작성 시점 기준 10/19~25보다 새로운 공개 주간이 없어 지난 호와 같은 리스트예요."),
 [rl(("Weekly best sellers · Beauty & Personal Care","주간 베스트셀러 · 뷰티·퍼스널케어"),("Sales rank","판매량순"),("Oct 19–25, 2026 (latest public week)","2026.10.19–25 (공개된 최신 주)"),[
   rk('tiktok',1,'medicube','Smooth & Clear Body Care Set','set','body',[U('37,967'),G('$1,176,977'),P('≈$31 avg')]),
   rk('tiktok',2,'Nature x Science','Rosemary Water and Rice Water','spray','hair',[U('28,579'),G('$357,552'),P('≈$12 list')]),
   rk('tiktok',3,'EPAIS','Essential Eyelash Growth Serum','dropper','make',[U('21,933'),G('$468,765')]),
   rk('tiktok',4,'QAWAFI','Voyage Nova Extrait De Parfum','perfume','body',[U('20,644'),G('$536,512')]),
   rk('tiktok',5,'PHOFAY','Sensitive Skin Hair Removal Spray','spray','body',[U('17,568'),G('$1,053,904'),P('≈$59.99 avg')]),
   gap('06–10',"Not disclosed — the source publishes only the Top 5 for beauty.","확인 불가 — 출처가 뷰티 Top 5만 공개")])],
 [('https://www.fastmoss.com/blog/best-selling-products-by-category/','FastMoss')])

amazon = ch('amazon','Amazon','US',("Sales rank could not be verified — the Best Sellers page returned a server error. Shown: beauty offers Amazon announced for Black Friday Week (brand-level, no product prices; not a sales rank).","판매 순위 확인 불가 — 베스트셀러 페이지가 서버 오류를 냈어요. 대신 아마존이 발표한 블랙프라이데이 위크 뷰티 할인(브랜드 단위·제품 가격 없음, 판매 순위 아님)을 실었어요."),
 [rl(("Black Friday Week beauty offers (announced)","블랙프라이데이 위크 뷰티 할인 (발표)"),("Promotion","프로모션"),("Runs Nov 19–30, 2026 · announced Nov 9","2026.11.19–30 · 11/9 발표"),[
   gap('01',"Up to 40% off select medicube and Color Wow","메디큐브·컬러와우 일부 최대 40%"),
   gap('02',"Up to 40% off select ANUA and REDKEN","아누아·레드켄 일부 최대 40%"),
   gap('03',"Up to 30% off skin & body care: OLAY, First Aid Beauty, Native, Mario Badescu, Cremo","스킨·바디케어 최대 30%: 올레이·퍼스트에이드뷰티·네이티브·마리오바데스쿠·크레모"),
   gap('04',"Up to 30% off makeup: Revolution Beauty London, KIKO Milano, Maybelline","메이크업 최대 30%: 레볼루션 뷰티·키코 밀라노·메이블린"),
   gap('05',"Up to $90 off select ghd and Braun beauty tools","ghd·브라운 뷰티 기기 최대 $90 할인"),
   gap('06–10',"Not verified — no product-level beauty prices were announced.","확인 불가 — 제품별 뷰티 가격은 발표되지 않았어요.")])],
 [('https://press.aboutamazon.com/2026/11/amazons-black-friday-week-and-cyber-monday-return-november-19-30-with-millions-of-deals-to-deliver-joy-this-holiday-season','Amazon press release')])

oy = [('Canmake','Creamy Touch Liner','liner','make','0.1g','₩13,000','4.69 · 146'),('Kiss Me','Heroine Make Speedy Mascara Remover','bottle','make','6.6ml','₩13,000','4.64 · 1,143'),
      ('Sofy','Cooling Fresh Sleep Panty','pack','body','5ea','₩11,100','4.61 · 130'),('Peripera','Speedy Skinny Brow Mascara','brush','make','3g','₩8,000','4.58 · 702'),
      ('Vaseline','Gluta-Hya Dewy Radiance Body Serum Lotion','pump','body','300ml','₩13,900','4.42 · 77'),('medicube','EGF NAD Elastic Ampoule','dropper','skin','30ml','₩58,500','4.54 · 55'),
      ('Peripera','Sunshine Cheek (Bread Rusher)','compact','make','4.2g','₩8,000','4.59 · 73'),('Dr.Florinus','Jet Pore Mist','spray','skin','95ml','₩27,000','4.37 · 63'),
      ('espoir','Easy Wear Eye Palette','compact','make','8g','₩32,000','4.55 · 55'),('Dove','Beauty Nourishing Body Wash','pump','body','1000ml','₩14,900','4.59 · 1,036')]
olive = ch('oliveyoung','Olive Young','KR',("Olive Young's sales ranking blocks automated reading; this is Glowpick's ranking of Olive Young products — popularity, not sales.","올리브영 판매 랭킹은 자동 열람이 막혀 있어 글로우픽의 올리브영 입점 제품 랭킹을 실었어요 — 판매량이 아닌 인기 기준이에요."),
 [rl(("Glowpick ranking · Olive Young products","글로우픽 랭킹 · 올리브영 입점 제품"),("Popularity","인기순"),("Update label on page: Nov 23, 2026","페이지 표기: 2026.11.23 업데이트"),
   [rk('oliveyoung',i,b,n,s,t,[V(v),P(p),RV(r)]) for i,(b,n,s,t,v,p,r) in enumerate(oy,1)])],[('https://www.glowpick.com/stores/21','Glowpick')])

hw_t = [("It's Skin",'Power 10 Licorice Jelly Pad','pack','skin','4.65 · 7,332'),('Dr.ecua','NMN 1% Niacinamide 2% Energizing Glow Serum','dropper','skin','4.70 · 128'),
        ('Rejuexcel','Vita B3 Cream','jar','skin','4.49 · 395'),('Illiyoon','Multi-Barrier Facial Repair Cream','jar','skin','4.92 · 36'),
        ('Rejuexcel','Revital Advanced Cream','jar','skin','4.58 · 401'),('Rejuexcel','Calming Clear Cream','jar','skin','4.57 · 389'),
        ('AESTURA','Atobarrier365 Cream','tube','skin','4.68 · 19,447'),('innisfree','Green Tea Butter Moisture Cream','jar','skin','4.57 · 150'),
        ('Torriden','DIVE-IN Low Molecular Hyaluronic Serum','dropper','skin','4.72 · 87,477'),('eSnature','Aqua Squalane Moisture Cream','jar','skin','4.58 · 44,308')]
hw_c = [('TONYMOLY','Ceramide Mochi Toner','bottle','skin','4.72 · 19,691'),('AESTURA','Atobarrier365 Cream','tube','skin','4.68 · 19,447'),
        ('Abib','Hyaluronic Boom Serum Water Drop','dropper','skin','4.64 · 3,471'),('Beplain','Mung Bean Acidic Cleansing Foam','tube','skin','4.63 · 51,673'),
        ('eSnature','Aqua Oasis Toner','bottle','skin','4.75 · 29,866'),('Wellage','Real Hyaluronic Blue 100 Ampoule','dropper','skin','4.65 · 34,728'),
        ('Clarike','Face and Body Lotion for Baby','pump','body','4.81 · 1,216'),('Sion','Kelp Ampoule Cleansing Foam','tube','skin','4.58 · 7,254'),
        ('eSnature','Aqua Squalane Moisture Cream','jar','skin','4.58 · 44,308'),('Lagom','Oat Micella Cleansing Milk','pump','skin','4.69 · 1,201')]
hwahae = ch('hwahae','Hwahae','KR',("Trending updated Nov 22, category ranking Nov 19. Ranking pages show no prices or sizes, so those are omitted; brand names are read from product titles.","급상승은 11/22, 카테고리 랭킹은 11/19 업데이트예요. 랭킹 페이지에 가격·용량이 없어 뺐고, 브랜드명은 제품명 앞부분에서 읽었어요."),
 [rl(("Trending · All categories","급상승 · 전체 카테고리"),("Trending","급상승"),("Updated Nov 22, 2026","2026.11.22 업데이트"),[rk('hwahae',i,b,n,s,t,[RV(r)]) for i,(b,n,s,t,r) in enumerate(hw_t,1)]),
  rl(("Category ranking · All","카테고리 랭킹 · 전체"),("Popularity","인기순"),("Updated Nov 19, 2026","2026.11.19 업데이트"),[rk('hwahae',i,b,n,s,t,[RV(r)]) for i,(b,n,s,t,r) in enumerate(hw_c,1)])],
 [('https://www.hwahae.co.kr/rankings?english_name=trending&theme_id=5102','Hwahae Trending'),('https://www.hwahae.co.kr/rankings?english_name=category&theme_id=2','Hwahae Category')])

def ud(no,br,n,s,t,sale,orig,pct): return rk('ulta',no,br,n,s,t,[P(sale)],None,(f"{pct}% off ({orig})",f"{pct}% 할인 (정가 {orig})"))
ulta = ch('ulta','Ulta','US',("Ulta has no public ranked list. Shown: product-level prices from its Black Friday page's online-only gift deals (page order, not a sales rank); the sale runs through Nov 28.","얼타는 공개 순위가 없어요. 블랙프라이데이 페이지의 온라인 전용 기프트 딜 중 가격이 표시된 제품을 페이지 순서대로 실었어요(판매 순위 아님). 세일은 11/28까지예요."),
 [rl(("Black Friday · online-only gift deals","블랙프라이데이 · 온라인 전용 기프트 딜"),("Promotion","프로모션"),("Through Nov 28, 2026","2026.11.28까지"),[
   ud(1,'Aramore','NAD+ Cell Energizing Treatment','dropper','skin','$77.00','$110.00',30),
   ud(2,'Sweet July Skin','Pineapple Punch Hydrating Face Mask','jar','skin','$19.20','$24.00',20),
   ud(3,'PRAI Beauty','Ageless Throat & Décolletage Crème','jar','skin','$23.00','$39.00',41),
   ud(4,'Onekind','Gold Rush Revitalizing Body Oil','dropper','body','$30.80','$44.00',30),
   ud(5,'JudyDoll','Ultra-Fine Liquid Eyeliner','liner','make','$9.59','$11.99',20),
   ud(6,'Unicorn Snot','SPF 35 Glitter Spritz','spray','skin','$14.40','$24.00',40),
   ud(7,'Tree To Tub','Copper Peptides+ Night Plumping Face Serum','dropper','skin','$18.65','$26.65',30),
   ud(8,'Superegg','Vitamin Collective Vitality Elixir','dropper','skin','$45.50','$65.00',30),
   ud(9,'Ginger Milk','Intensive Hair Repair Kit','set','hair','$52.50','$105.00',50),
   gap('10',"Brand-level offers include 25% off all ANUA, up to 25% off select medicube skin care and up to 50% off select Lancôme.","브랜드 단위 할인: 아누아 전 제품 25%, 메디큐브 일부 최대 25%, 랑콤 일부 최대 50%")])],
 [('https://www.ulta.com/promotion/black-friday','Ulta Black Friday')])

amazon = amazon.replace("Runs Nov 19–30, 2026 · announced Nov 9","Live Nov 19–30, 2026 · announced Nov 9").replace("2026.11.19–30 · 11/9 발표","2026.11.19–30 진행 중 · 11/9 발표")

head = ('<div class="panel" data-p="retail"><section class="retail"><div class="sh"><h2>' + bi('Retail Rank · Weekly','유통 랭킹 · 주간') + '</h2><small>' + bi('Week of Nov 16 – 22, 2026','2026년 11월 16–22일 주') + '</small></div>'
 '<p class="lead">' + bi('Black Friday week: Ulta’s sale runs to Nov 28 and Amazon’s Black Friday Week is live (Nov 19–30), so U.S. channels show promotions, not ranks. Hwahae trending refreshed Nov 22.','블랙프라이데이 주간이에요. 얼타 세일은 11/28까지, 아마존 블프 위크는 11/19~30 진행 중이라 미국 채널은 순위 대신 프로모션을 실었어요. 화해 급상승은 11/22 기준이에요.') + '</p>'
 '<div class="chips" role="group" aria-label="Channel"><button data-f="all" aria-pressed="true">All</button><button data-f="tiktok" aria-pressed="false">TikTok Shop</button><button data-f="amazon" aria-pressed="false">Amazon</button><button data-f="oliveyoung" aria-pressed="false">Olive Young</button><button data-f="hwahae" aria-pressed="false">Hwahae</button><button data-f="ulta" aria-pressed="false">Ulta</button></div>'
 '<div class="note-box"><h4>' + bi('Planner’s read this week','이번 주 기획 포인트') + '</h4><ul>'
 '<li>' + bi('A new launch can trend in a week: Illiyoon’s Multi-Barrier Facial Repair Cream (out Nov 16) is #4 on Hwahae trending with a 4.92 rating, while Rejuexcel still holds three of the top six.','신제품도 일주일이면 급상승해요: 11/16 출시된 일리윤 멀티베리어 페이셜 리페어 크림이 평점 4.92로 화해 급상승 4위, 리쥬엑셀은 여전히 Top 6 중 3자리를 지켜요.') + '</li>'
 '<li>' + bi('Winter body care is climbing: Vaseline’s gluta-hya body serum lotion (#5) and Dove’s 1,000ml body wash (#10) entered Glowpick’s Olive Young Top 10.','겨울 바디케어가 올라와요: 바세린 글루타-히야 바디 세럼 로션(5위), 도브 1,000ml 바디워시(10위)가 글로우픽 올리브영 Top 10에 들어왔어요.') + '</li>'
 '<li>' + bi('Neck and décolleté care shows up in U.S. promos too (PRAI’s throat crème, 41% off at Ulta) — the same zone Clarins just renewed.','미국 프로모션에도 목·데콜테 케어가 보여요(얼타 PRAI 넥 크림 41% 할인) — 이번 주 클라랑스가 리뉴얼한 바로 그 부위예요.') + '</li></ul></div>'
 '<p class="disc">' + bi('Illustrations show the product form only, not real packaging. Tap an illustration to open that product on its channel (search results) for official photos and live prices.','그림은 제품 형태만 나타낸 일러스트이며 실제 패키지가 아니에요. 그림을 누르면 해당 채널에서 그 제품(검색 결과)이 열려 공식 사진과 실시간 가격을 볼 수 있어요.') + '</p>')
out = head + tiktok + amazon + olive + hwahae + ulta + '</section>' + tpl
open(os.path.join(R,'retail/2026-11-22.html'),'w',encoding='utf-8').write(out)
p=os.path.join(R,'retail/index.json'); a=json.load(open(p,encoding='utf-8')); a=[x for x in a if x['date']!='2026-11-22']
a.insert(0,{"date":"2026-11-22","week":"2026-11-16/2026-11-22"}); open(p,'w',encoding='utf-8').write(json.dumps(a,ensure_ascii=False)+'\n')
print('ok', len(out), sorted(SH))
