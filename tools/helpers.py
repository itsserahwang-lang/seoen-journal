import html, json, sys, os
R = sys.argv[1]  # repo root
SP = os.path.dirname(os.path.abspath(__file__))
e = lambda t: html.escape(t, quote=True)
def bi(en, ko, tag='span'): return f'<{tag} class=" l-en">{e(en)}</{tag}><{tag} class=" l-ko">{e(ko)}</{tag}>'
def sum_(en, ko): return f'<div class="sum"><p class="en">{e(en)}</p><p class="kot">{e(ko)}</p></div>'
def read(url, src): return f'<a class="read" href="{e(url)}" target="_blank" rel="noopener"><span class=" l-en">Read the article</span><span class=" l-ko">원문 기사 보기</span> · {e(src)} ↗</a>'
POS = [(72,38,30,75),(28,30,74,72),(64,62,24,28),(36,70,78,30)]
PAL = {'pink':'255,61,139','gold':'205,181,138','red':'179,38,58','ivory':'245,240,230'}
n = [0]
def card(c):
    n[0]+=1; x1,y1,x2,y2 = POS[n[0]%4]
    c1 = PAL[c.get('c1','gold')]; c2 = PAL[c.get('c2','pink')]
    sub = f' data-sub="{c["sub"]}"' if c.get('sub') else ''
    badge = f'<span class="badge b-{c["badge"][0].lower()}">{e(c["badge"][0])} · {e(c["badge"][1])}</span>' if c.get('badge') else ''
    art = f' data-art="{c["art"]}"' if c.get('art') else ''
    return (f'<article class="card"{sub}><div class="th"{art} style="--c1:{c1};--c2:{c2};--x1:{x1}%;--y1:{y1}%;--x2:{x2}%;--y2:{y2}%" role="img" aria-label="{e(c["kw"])}">'
            f'<div class="ov">{badge}<span class="src">{e(c["srcl"])}</span><span class="kw">{e(c["kw"])}</span></div></div>'
            f'<div class="body"><span class="meta">{e(c["meta"])}</span>{bi(c["t"][0],c["t"][1],"h3")}{sum_(*c["s"])}'
            f'<p class="ko"><b>↳</b>{bi(c["why"][0],c["why"][1])}</p>{read(c["url"],c["src"])}</div></article>')
def sec(en, ko, inner): return f'<section><div class="sh"><h2>{e(en)}</h2><small>{e(ko)}</small></div>{inner}</section>'
def cards(lst): return '<div class="cards">' + ''.join(card(c) for c in lst) + '</div>'
def empty(): return '<p class="empty"><span class=" l-en">No new updates</span><span class=" l-ko">새 소식 없음</span></p>'
