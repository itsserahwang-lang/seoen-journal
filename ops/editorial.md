# editorial/ — 월간 Editorial Monthly · VOGUE · ELLE (매월 24일 10:41 KST)

개별 뉴스 기사가 아니라 그달 호의 '매거진 자료'(커버 스토리, 화보·에디토리얼, 트렌드 리포트·에디터 픽)를 정리해 Magazine 탭 맨 위에 실습니다. 공통 규칙은 ops/README.md.

## 1. 대상과 출처
- VOGUE — 직접 읽기: VOGUE Korea(vogue.co.kr), VOGUE Australia(vogue.com.au), VOGUE Scandinavia(voguescandinavia.com)
- ELLE — 직접 읽기: ELLE Korea(elle.co.kr), ELLE Australia(elle.com.au), ELLE Singapore(elle.com.sg), ELLE Japan(elle.co.jp)
- VOGUE Korea와 ELLE Korea는 매달 반드시, 그 밖에 화제가 큰 판 1~2개를 더해 총 3~5개 판.
- 미국·영국·프랑스판 등 차단된 판은 열지 않고, 큰 화제면 다른 매체 보도로만 "VOGUE US via 매체명".
- WebSearch로 그달 호를 찾고("보그 코리아 2026년 12월호 커버", "ELLE Korea December 2026 cover"), 쓰는 내용은 WebFetch로 확인. 표지 인물·크레딧·제품명은 확인한 것만.

## 2. 판마다
- A. Cover Story — 표지 인물, 커버라인 2~4개, 인터뷰 핵심 2~3문장(인용 15단어 미만), 뷰티·브랜드 관련 발언.
- B. Editorial — 대표 화보 1~2개: 콘셉트, 크레딧(포토·스타일링·메이크업·헤어), 메이크업·헤어 룩 포인트 3개(컬러·텍스처·기법), 크레딧의 뷰티 제품. 사진은 링크로만.
- C. Trend Report & Editor's Picks — 트렌드 리포트, 뷰티 어워즈, 에디터 픽 3~5개(브랜드 — 제품 — 이유). 협찬 콘텐츠 제외.
- 마지막: This Month's Takeaways / 이달의 기획 포인트 3개(뷰티 상품기획·SEOEN 브랜드 시사점, 사실 기반).

## 3. editorial/YYYY-MM-DD.html
```html
<section class="ed-sec">
<header class="fr-mast"><span class="fr-kick">Editorial Monthly · VOGUE · ELLE · Vol. NNN</span><h2 class="fr-title"><span class="l-en">The December Issues</span><span class="l-ko">12월호 에디토리얼</span></h2><p class="fr-dek"><span class="l-en">이달 흐름</span><span class="l-ko">번역</span></p><span class="fr-date">December 2026</span></header>
<div class="chips" role="group" aria-label="Magazine / 매거진"><button data-f="all" aria-pressed="true">All</button><button data-f="vogue" aria-pressed="false">VOGUE</button><button data-f="elle" aria-pressed="false">ELLE</button></div>
<article class="ed-issue" data-sub="vogue|elle">
 <div class="ed-cover" data-art="lips|frame|flacon|rose|sun|arch|wave|sprig|drop|dots" data-tone="…"><div><span class="ed-ed">Vogue Korea</span><div class="ed-mo">December 2026</div></div><div><span class="ed-star">표지 인물</span><ul class="ed-lines"><li>커버라인</li></ul></div></div>
 <div class="ed-body"><h3>VOGUE Korea · December</h3><span class="ed-meta">발매일 · 출처</span>
 <div class="ed-block"><h4><span class="l-en">Cover Story</span><span class="l-ko">커버 스토리</span></h4><div class="sum"><p class="en">…</p><p class="kot">…</p></div><p class="ko"><b>↳</b>…</p></div>
 <div class="ed-block"><h4><span class="l-en">Editorial</span><span class="l-ko">화보 분석</span></h4><dl class="ed-credits"><div><dt><span class="l-en">Photo</span><span class="l-ko">포토</span></dt><dd>이름</dd></div>…</dl><ul class="ed-points"><li>…</li></ul></div>
 <div class="ed-block"><h4><span class="l-en">Trend Report &amp; Editor's Picks</span><span class="l-ko">트렌드 리포트·에디터 픽</span></h4><ul class="ed-picks"><li><b>브랜드 — 제품</b> 이유</li></ul></div>
 <div class="ed-links"><a class="read" href="URL" target="_blank" rel="noopener">Cover story / 커버 스토리 ↗</a> <a class="read" href="URL" target="_blank" rel="noopener">Editorial / 화보 ↗</a></div></div></article>
<div class="note-box"><h4><span class="l-en">This Month's Takeaways</span><span class="l-ko">이달의 기획 포인트</span></h4><ol><li>…</li></ol></div>
</section>
```
- ed-ed 는 판 이름을 평범한 글자로만(로고·마스트헤드 서체 흉내 금지).
- editorial/index.json 맨 앞: `{"date":"YYYY-MM-DD","issue":"YYYY-MM","label":"Dec 2026"}`. Vol. 번호 = 항목 수 + 1.

## 알림
"📖 Editorial Monthly Vol. NNN — [호 월] VOGUE · ELLE" + 판별 표지 인물 + 기획 포인트 3줄 + https://itsserahwang-lang.github.io/seoen-journal/#mag
