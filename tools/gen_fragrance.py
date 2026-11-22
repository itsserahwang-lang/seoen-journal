import os,sys,json,html
R=sys.argv[1]; e=lambda t: html.escape(t,quote=True)
def bi(en,ko): return f'<span class="l-en">{e(en)}</span><span class="l-ko">{e(ko)}</span>'
def look(no,flip,sub,bottle,tone,notes,cap,house,name,meta,pyr,s,why,specs,url,src):
    p=''.join(f'<div><dt>{bi(*a)}</dt><dd>{bi(*b)}</dd></div>' for a,b in pyr)
    sp=('<dl class="lk-spec">'+''.join(f'<div><dt>{bi(*a)}</dt><dd>{e(v)}</dd></div>' for a,v in specs)+'</dl>') if specs else ''
    return (f'<article class="look{" flip" if flip else ""}" data-sub="{sub}"><figure class="lk-art" data-bottle="{bottle}" data-tone="{tone}" data-notes="{e(notes)}" aria-hidden="true"><span class="no">{no:02d}</span><span class="cap">{e(cap)}</span></figure>'
            f'<div class="lk-body"><span class="lk-house">{e(house)}</span><h3 class="lk-name">{e(name)}</h3><span class="lk-meta">{e(meta)}</span><dl class="pyr">{p}</dl>'
            f'<div class="sum"><p class="en">{e(s[0])}</p><p class="kot">{e(s[1])}</p></div>{sp}<p class="ko"><b>↳</b>{bi(*why)}</p>'
            f'<a class="read" href="{e(url)}" target="_blank" rel="noopener">Source / 출처 · {e(src)} ↗</a></div></article>')
def sh(sub,en,ko): return f'<div class="sh sub" data-sub="{sub}"><h2>{bi(en,ko)}</h2></div>'
def cn(term,en,ko,url=None): return f'<article class="cn" data-sub="notes"><span class="cn-term">{e(term)}</span><p>{bi(en,ko)}</p>'+(f'<a class="read" href="{e(url)}" target="_blank" rel="noopener">Source ↗</a>' if url else '')+'</article>'
TF='https://www.tomfordbeauty.com/products/tobacco-vanille-eau-de-parfum'; LL='https://www.lelabofragrances.com/th-noir-29.html'; BV='https://eyesmag.com/posts/165143/bottega-veneta-alta-fragrance'
MM='https://www.cmn.co.kr/sub/news/news_view.asp?news_idx=51577'; EB='https://www.newspim.com/news/view/20261118000096'
KN=('Key notes','주요 노트')
o='<div class="panel" data-p="fragrance"><section class="fragrance"><header class="fr-mast"><span class="fr-kick">Fragrance Lookbook · Vol. 003</span>'
o+='<h2 class="fr-title">'+bi('Velvet After Dark','밤의 벨벳')+'</h2><p class="fr-dek">'+bi('Tobacco, black tea, leather and vanilla — scents that read best after sunset, from duty-free icons to this week’s launches. Prices and stockists only where confirmed.','토바코, 블랙티, 레더, 바닐라 — 해가 진 뒤에 가장 잘 어울리는 향들. 면세점 아이콘부터 이번 주 신작까지 담았어요. 가격과 판매처는 확인된 경우에만 적었어요.')+'</p><span class="fr-date">Nov 16 — Nov 22, 2026</span></header>'
o+='<div class="chips" role="group" aria-label="Filter / 분류"><button data-f="all" aria-pressed="true">All</button><button data-f="dutyfree" aria-pressed="false">'+bi('Duty-free','면세점')+'</button><button data-f="launch" aria-pressed="false">'+bi('Launches','신제품')+'</button><button data-f="korea" aria-pressed="false">'+bi('Korean niche','한국 니치')+'</button><button data-f="notes" aria-pressed="false">'+bi("Collector's notes",'컬렉터 노트')+'</button></div>'
o+=sh('dutyfree','Duty-free Lineup · Evening Icons','면세점 라인업 · 저녁의 아이콘')
o+=look(1,False,'dutyfree','cube','bordeaux','tobacco, vanilla, tonka','Tobacco Leaf · Spice · Tonka','Tom Ford','Tobacco Vanille','Eau de Parfum · Private Blend',
 [(KN,('Tobacco leaf, ginger, spice notes, tonka bean, cocoa, fruit accord','토바코 리프, 진저, 스파이스, 통카빈, 코코아, 프루트 어코드'))],
 ('The brand calls it a warm blend of tobacco, vanilla and sweet wood sap — a winter classic that reads like a leather armchair by the fire.','브랜드는 토바코·바닐라·달콤한 나무 수액의 따뜻한 조합이라고 소개해요. 벽난로 옆 가죽 의자 같은 겨울의 클래식이에요.'),
 ('Spice + sweetness is the template many newer gourmand-ambers still follow.','스파이스 + 단맛 구조는 지금도 많은 구르망 앰버가 따르는 공식이에요.'),
 [(('Price','가격'),'$300 · 50ml · Tom Ford Beauty US · 11/21 기준')],TF,'Tom Ford Beauty')
o+=look(2,True,'dutyfree','column','noir','black tea, bergamot, hay','Black Tea · Leaf · Wood','Le Labo','Thé Noir 29','Eau de Parfum',
 [(('Description','설명'),('A dense black-tea infusion between softness and strength','부드러움과 강함 사이를 오가는 진한 블랙티 인퓨전'))],
 ('An ode to the tea leaf rather than a sweet tea: dry, slightly smoky and calm — evening without the sugar.','달콤한 차가 아니라 찻잎 자체에 바친 향이에요. 건조하고 살짝 스모키하며 차분해요 — 설탕 없는 저녁.'),
 ('A good counterweight when the rest of the shelf is vanilla.','선반이 바닐라로 가득할 때 균형을 잡아주는 향이에요.'),[],LL,'Le Labo')
o+=look(3,False,'dutyfree','stout','champagne','vanilla, chocolate, resin','Milky Vanilla · Woods · Resin','Bottega Veneta','Alta — Collection of 10','Eau de Parfum · 50ml / 100ml · since Sep 1, 2026',
 [(('Collection notes','컬렉션 노트'),('Citrus, aromatics, woods, resins; a stracciatella-like milky vanilla and chocolate','시트러스, 아로마틱, 우디, 레진; 스트라차텔라 같은 밀키 바닐라와 초콜릿'))],
 ('Ten eau de parfums built as pairs inspired by the house’s intrecciato weave, mixing Italian and world-sourced materials.','하우스의 인트레치아토(엮기) 기법에서 영감을 받아 짝을 이루도록 설계한 오 드 퍼퓸 10종으로, 이탈리아와 세계 각지의 원료를 섞었어요.'),
 ('Collections designed to pair encourage layering — and buying two.','짝을 이루도록 만든 컬렉션은 레이어링을, 그리고 두 병 구매를 이끌어요.'),[],BV,'Eyesmag')
o+=sh('launch','New Launches & Perfumers','신제품·조향사')
o+=look(4,True,'launch','bell','rose','blackberry, gardenia, vanilla','Blackberry Liqueur · Gardenia · Vanilla','Miu Miu','Miutine Intense','Eau de Parfum (30% concentration) · Dominique Ropion · 2026',
 [(('Top','탑'),('Ripe blackberry liqueur accord','잘 익은 블랙베리 리큐어 어코드')),(('Heart','미들'),('Gardenia accord','가드니아 어코드')),(('Base','베이스'),('Madagascar vanilla, patchouli','마다가스카르 바닐라, 패촐리'))],
 ('A richer, darker flanker of Miutine: boozy berry over creamy gardenia, landing on vanilla and patchouli; bottled in retro brown matelassé glass.','미우틴의 더 짙고 어두운 플랭커예요. 리큐어 같은 베리가 크리미한 가드니아 위에 흐르고, 바닐라와 패촐리로 내려앉아요. 레트로 브라운 마틀라세 유리병에 담겼어요.'),
 ('Dominique Ropion on a fashion flanker signals perfumery-first ambitions.','패션 하우스 플랭커에 도미니크 로피온 — 향 자체로 승부하겠다는 신호예요.'),[],MM,'CMN · Nov 16')
o+=look(5,False,'launch','flacon','noir','leather, wood, citrus','Woody · Floral · Leather · Citrus','Edward Bess','7 Eaux de Parfum — Korea debut','Eau de Parfum · Shinsegae International exclusive · Nov 2026',
 [(('Families','향조'),('Woody, floral, leather, citrus — genderless','우디, 플로럴, 레더, 시트러스 — 젠더리스'))],
 ('The New York beauty house (founded 2006; fragrances with master perfumer Carlos Benaim since 2016) arrives in Korea with seven EDPs and a pop-up showing the founder’s paintings.','2006년 뉴욕에서 시작해 2016년부터 마스터 조향사 카를로스 베나임과 향수를 만든 하우스가 오 드 퍼퓸 7종으로 한국에 들어왔어요. 팝업에서는 창립자의 그림도 볼 수 있어요.'),
 ('Ultra-premium pricing (₩540k+) tests how far Korea’s niche boom stretches.','54만 원대 이상의 초고가는 한국 니치 붐이 어디까지 갈지 시험해요.'),
 [(('Price','가격'),'₩540,000–570,000 · 100ml · 11/18 기준'),(('Where','판매처'),'분더샵 청담 1F 팝업(~12/15, 10% 할인) · 신세계V')],EB,'Newspim · Nov 18')
o+=sh('korea','Korean Niche','한국 니치')
o+='<p class="empty" data-sub="korea">'+bi('Brand pages for this week’s Korean picks were unavailable, so no notes or prices could be confirmed — back next week.','이번 주 한국 니치 후보의 공식 페이지에 접속할 수 없어 노트·가격을 확인하지 못했어요 — 다음 주에 이어서 소개할게요.')+'</p>'
o+=sh('notes',"Collector's Notes",'컬렉터 노트')
o+=cn('Tonka bean','A seed with a sweet, almond-hay and vanilla-like smell (from coumarin). It sits under Tobacco Vanille and many modern ambers, adding warmth without sugar-candy sweetness.','아몬드·건초·바닐라 같은 달콤한 향(쿠마린)을 지닌 씨앗이에요. 토바코 바닐과 요즘 앰버 향의 바탕에서 사탕 같지 않은 따뜻한 단맛을 줘요.',TF)
o+=cn('Tobacco accord','Perfume tobacco is a built accord of honeyed, hay-like and dried-fruit facets — not cigarette smoke. Spice and cocoa push it toward a cosy, cognac-like warmth.','향수 속 토바코는 담배 연기가 아니라 꿀·건초·말린 과일 느낌을 조합한 어코드예요. 스파이스와 코코아가 더해지면 아늑한 코냑 같은 온기가 돼요.',TF)
o+=cn('Layering idea','For a less sweet evening, wear a black-tea scent first and a single spray of a vanilla-tobacco on the wrists only: the tea keeps the trail dry and calm.','덜 달콤한 저녁을 원한다면 블랙티 향을 먼저 뿌리고, 바닐라·토바코 향은 손목에만 한 번 더해 보세요. 차 향이 잔향을 건조하고 차분하게 잡아줘요.')
o+='</section></div>'
open(os.path.join(R,'fragrance/2026-11-21.html'),'w',encoding='utf-8').write(o)
p=os.path.join(R,'fragrance/index.json'); a=json.load(open(p,encoding='utf-8')); a=[x for x in a if x['date']!='2026-11-21']
a.insert(0,{"date":"2026-11-21","week":"2026-11-16/2026-11-22","title":"Velvet After Dark","title_ko":"밤의 벨벳"}); open(p,'w',encoding='utf-8').write(json.dumps(a,ensure_ascii=False)+'\n'); print('ok',len(o))
