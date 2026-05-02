f = open(r'c:\Users\priest\Desktop\rerenwangzhan\index.html', 'r', encoding='utf-8')
content = f.read()
f.close()

old_section = '''<section class="section works orbit-works" id="works" aria-labelledby="works-title">
<div class="container">
<div class="orbit-header reveal">
<div class="orbit-header__left">
<p class="badge">&#9679; VISUAL ARCHIVE</p>
<h2 id="works-title">&#22810;&#32500;&#35270;&#35273;&#20316;&#21697;&#24402;&#26723;</h2>
<p>A <em>multidimensional</em> archive for AI experiments, graphic studies, <em>visual</em> systems, and 3D modeling works.</p>
</div>
<div class="orbit-header__tabs">
<button class="orbit-tab is-active" data-filter="all">&#20840;&#37096; ALL</button>
<button class="orbit-tab" data-filter="graphic">&#24179;&#38754; GRAPHIC</button>
<button class="orbit-tab" data-filter="visual">&#35270;&#35273;&#31995;&#32479; VISUAL</button>
<button class="orbit-tab" data-filter="3d">3D&#24314;&#27169; 3D MODELING</button>
<button class="orbit-tab" data-filter="ai">AI&#23454;&#39564; AI EXPERIMENT</button>
</div>
</div>
</div>
<div class="orbit-carousel reveal">
<div class="orbit-carousel__viewport">
<div class="orbit-carousel__track" data-orbit-track>
<figure class="orbit-card orbit-card--hero" data-cat="graphic"><img src="./pinmian/5.jpg" alt="Visual experiment" loading="lazy"><figcaption><span>FEATURED</span><strong>&#35270;&#35273;&#23454;&#39564;&#32452;</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/6.jpg" alt="Layout study" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#29256;&#24335;&#30740;&#31350;</strong></figcaption></figure>
<figure class="orbit-card" data-cat="ai"><img src="./pinmian/7.jpg" alt="Prompt log" loading="lazy"><figcaption><span>PROMPT</span><strong>&#25552;&#31034;&#35789;&#26085;&#24535;</strong></figcaption></figure>
<figure class="orbit-card" data-cat="3d"><img src="./pinmian/8.jpg" alt="Model study" loading="lazy"><figcaption><span>MODEL</span><strong>&#26448;&#36136;&#30740;&#31350;</strong></figcaption></figure>
<figure class="orbit-card" data-cat="visual"><img src="./pinmian/9.jpg" alt="Visual system" loading="lazy"><figcaption><span>SYSTEM</span><strong>&#35270;&#35273;&#31995;&#32479;</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/10.jpg" alt="Process sample" loading="lazy"><figcaption><span>PROCESS</span><strong>&#36807;&#31243;&#26679;&#26412;</strong></figcaption></figure>
<figure class="orbit-card" data-cat="visual"><img src="./pinmian/11.jpg" alt="Visual work" loading="lazy"><figcaption><span>VISUAL</span><strong>&#35270;&#35273;&#20316;&#21697;</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/12.jpg" alt="Graphic work" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697;</strong></figcaption></figure>
<figure class="orbit-card" data-cat="ai"><img src="./pinmian/14.jpg" alt="AI experiment" loading="lazy"><figcaption><span>AI</span><strong>AI&#23454;&#39564;</strong></figcaption></figure>
<figure class="orbit-card" data-cat="visual"><img src="./pinmian/15.jpg" alt="Visual study" loading="lazy"><figcaption><span>VISUAL</span><strong>&#35270;&#35273;&#30740;&#31350;</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/16.jpg" alt="Design work" loading="lazy"><figcaption><span>DESIGN</span><strong>&#35774;&#35745;&#20316;&#21697;</strong></figcaption></figure>
<figure class="orbit-card" data-cat="ai"><img src="./pinmian/17.jpg" alt="AI output" loading="lazy"><figcaption><span>AI</span><strong>AI&#36755;&#20986;</strong></figcaption></figure>
<figure class="orbit-card" data-cat="visual"><img src="./pinmian/18.jpg" alt="Archive item" loading="lazy"><figcaption><span>ARCHIVE</span><strong>&#24402;&#26723;&#39033;&#30446;</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/img_v3_02pv_3679e745-d15f-4062-96ea-432d1677889g_MIDDLE_WEBP.webp" alt="Visual archive" loading="lazy"><figcaption><span>FEATURED</span><strong>&#35270;&#35273;&#26723;&#26696;</strong></figcaption></figure>
</div>
</div>
<div class="orbit-carousel__controls">
<div class="orbit-counter"><strong data-orbit-current>01</strong> <span>/ <span data-orbit-total>14</span></span></div>
<div class="orbit-arrows"><button class="orbit-arrow" data-orbit-prev aria-label="Previous">&lsaquo;</button><button class="orbit-arrow" data-orbit-next aria-label="Next">&rsaquo;</button></div>
</div>
</div>
<div class="container orbit-bottom reveal">
<div class="orbit-explore">
<p class="badge">EXPLORE</p>
<h3>&#22810;&#32500;&#25506;&#32034;&#26041;&#24335;</h3>
<p>&#36890;&#36807;&#19981;&#21516;&#32500;&#24230;&#36827;&#20837;&#35270;&#35273;&#26723;&#26696;&#65292;&#21457;&#29616;&#26356;&#22810;&#21487;&#33021;&#24615;&#12290;</p>
<div class="orbit-explore__grid"><span>&#38543;&#26426;&#25506;&#32034;</span><span>&#33394;&#24425;&#25506;&#32034;</span><span>&#26102;&#38388;&#32447;&#25506;&#32034;</span><span>&#26631;&#31614;&#25506;&#32034;</span></div>
</div>
<div class="orbit-planet" aria-hidden="true">
<div class="orbit-planet__ring"></div>
<div class="orbit-planet__core"></div>
</div>
<div class="orbit-recommend">
<p class="badge">AI RECOMMEND</p>
<h3>AI &#26234;&#33021;&#25512;&#33616;</h3>
<p>&#22522;&#20110;&#20320;&#30340;&#27983;&#35272;&#34892;&#20026;&#65292;&#20026;&#20320;&#25512;&#33616;&#30456;&#20851;&#20316;&#21697;&#12290;</p>
<div class="orbit-trending">
<p class="badge badge--sm">TRENDING &#36235;&#21183;&#20851;&#38190;&#35789;</p>
<div class="orbit-tags"><span>&#31185;&#25216;&#24863;</span><span>&#26410;&#26469;&#20027;&#20041;</span><span>&#31354;&#38388;&#35774;&#35745;</span><span>&#21697;&#29260;&#25645;&#24314;</span><span>&#24037;&#19994;&#35774;&#35745;</span><span>AI&#29983;&#25104;</span><span>UI/UX</span><span>&#20809;&#24433;&#34920;&#29616;</span></div>
</div>
</div>
</div>
</section>'''

new_section = '''<section class="section works orbit-works" id="works" aria-labelledby="works-title">
<div class="container">
<div class="orbit-header reveal">
<div class="orbit-header__left">
<p class="badge">&#9679; VISUAL ARCHIVE</p>
<h2 id="works-title">&#22810;&#32500;&#35270;&#35273;&#20316;&#21697;&#24402;&#26723;</h2>
<p>A multidimensional archive for AI experiments, graphic studies, visual systems, and 3D modeling works.</p>
</div>
<div class="orbit-header__right">
<div class="orbit-header__tabs">
<button class="orbit-tab is-active" data-filter="all">&#20840;&#37096; ALL</button>
<button class="orbit-tab" data-filter="graphic">&#24179;&#38754; GRAPHIC</button>
<button class="orbit-tab" data-filter="visual">&#35270;&#35273;&#31995;&#32479; VISUAL</button>
<button class="orbit-tab" data-filter="3d">3D&#24314;&#27169; 3D MODELING</button>
<button class="orbit-tab" data-filter="ai">AI&#23454;&#39564; AI EXPERIMENT</button>
</div>
<div class="orbit-view-mode">
<button class="orbit-view-btn is-active" data-view="grid" aria-label="Grid view">
<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><rect x="1" y="1" width="5" height="5" rx="1" stroke="currentColor" stroke-width="1.5"/><rect x="10" y="1" width="5" height="5" rx="1" stroke="currentColor" stroke-width="1.5"/><rect x="1" y="10" width="5" height="5" rx="1" stroke="currentColor" stroke-width="1.5"/><rect x="10" y="10" width="5" height="5" rx="1" stroke="currentColor" stroke-width="1.5"/></svg>
</button>
<button class="orbit-view-btn" data-view="list" aria-label="List view">
<svg width="16" height="16" viewBox="0 0 16 16" fill="none"><rect x="1" y="2" width="14" height="2" rx="1" stroke="currentColor" stroke-width="1.5"/><rect x="1" y="7" width="14" height="2" rx="1" stroke="currentColor" stroke-width="1.5"/><rect x="1" y="12" width="14" height="2" rx="1" stroke="currentColor" stroke-width="1.5"/></svg>
</button>
</div>
</div>
</div>
</div>
<div class="orbit-carousel reveal">
<div class="orbit-carousel__viewport">
<div class="orbit-carousel__track" data-orbit-track>
<figure class="orbit-card orbit-card--far" data-cat="graphic"><img src="./pinmian/1.jpg" alt="Work 1" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 01</strong></figcaption></figure>
<figure class="orbit-card orbit-card--near" data-cat="graphic"><img src="./pinmian/2.jpg" alt="Work 2" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 02</strong></figcaption></figure>
<figure class="orbit-card orbit-card--side" data-cat="visual"><img src="./pinmian/3.jpg" alt="Work 3" loading="lazy"><figcaption><span>VISUAL</span><strong>&#35270;&#35273;&#31995;&#32479; 03</strong></figcaption></figure>
<figure class="orbit-card orbit-card--hero" data-cat="graphic"><img src="./pinmian/5.jpg" alt="Featured work" loading="lazy"><figcaption><span>FEATURED</span><strong>&#35270;&#35273;&#23454;&#39564;&#32452;</strong></figcaption></figure>
<figure class="orbit-card orbit-card--side" data-cat="3d"><img src="./pinmian/8.jpg" alt="Work 5" loading="lazy"><figcaption><span>3D MODEL</span><strong>&#51D&#24314;&#27169; 05</strong></figcaption></figure>
<figure class="orbit-card orbit-card--near" data-cat="ai"><img src="./pinmian/7.jpg" alt="Work 6" loading="lazy"><figcaption><span>AI</span><strong>AI&#23454;&#39564; 06</strong></figcaption></figure>
<figure class="orbit-card orbit-card--far" data-cat="visual"><img src="./pinmian/9.jpg" alt="Work 7" loading="lazy"><figcaption><span>VISUAL</span><strong>&#35270;&#35273;&#20316;&#21697; 07</strong></figcaption></figure>
<figure class="orbit-card orbit-card--far" data-cat="graphic"><img src="./pinmian/10.jpg" alt="Work 8" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 08</strong></figcaption></figure>
<figure class="orbit-card orbit-card--near" data-cat="ai"><img src="./pinmian/14.jpg" alt="Work 9" loading="lazy"><figcaption><span>AI</span><strong>AI&#23454;&#39564; 09</strong></figcaption></figure>
<figure class="orbit-card orbit-card--side" data-cat="visual"><img src="./pinmian/11.jpg" alt="Work 10" loading="lazy"><figcaption><span>VISUAL</span><strong>&#35270;&#35273;&#20316;&#21697; 10</strong></figcaption></figure>
<figure class="orbit-card orbit-card--hero" data-cat="graphic"><img src="./pinmian/12.jpg" alt="Work 11" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 11</strong></figcaption></figure>
<figure class="orbit-card orbit-card--side" data-cat="3d"><img src="./pinmian/15.jpg" alt="Work 12" loading="lazy"><figcaption><span>3D MODEL</span><strong>3D&#24314;&#27169; 12</strong></figcaption></figure>
<figure class="orbit-card orbit-card--near" data-cat="ai"><img src="./pinmian/17.jpg" alt="Work 13" loading="lazy"><figcaption><span>AI</span><strong>AI&#23454;&#39564; 13</strong></figcaption></figure>
<figure class="orbit-card orbit-card--far" data-cat="graphic"><img src="./pinmian/16.jpg" alt="Work 14" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 14</strong></figcaption></figure>
</div>
</div>
<div class="orbit-carousel__reflection" aria-hidden="true"></div>
<div class="orbit-carousel__controls">
<div class="orbit-progress">
<strong data-orbit-current>03</strong>
<span class="orbit-progress__divider">/</span>
<span data-orbit-total>36</span>
<div class="orbit-progress__bar"><div class="orbit-progress__fill"></div></div>
</div>
<div class="orbit-arrows"><button class="orbit-arrow" data-orbit-prev aria-label="Previous">&lsaquo;</button><button class="orbit-arrow" data-orbit-next aria-label="Next">&rsaquo;</button></div>
</div>
</div>
<div class="container orbit-bottom reveal">
<div class="orbit-explore">
<p class="badge">EXPLORE</p>
<h3>&#22810;&#32500;&#25506;&#32034;&#26041;&#24335;</h3>
<p>&#36890;&#36807;&#19981;&#21516;&#32500;&#24230;&#36827;&#20837;&#35270;&#35273;&#26723;&#26696;&#65292;&#21457;&#29616;&#26356;&#22810;&#21487;&#33021;&#24615;&#12290;</p>
<div class="orbit-explore__grid">
<div class="explore-card">
<div class="explore-card__icon">&#128269;</div>
<strong>&#38543;&#26426;&#25506;&#32034;</strong>
<small>&#27599;&#27425;&#37117;&#26377;&#26032;&#21457;&#29616;</small>
</div>
<div class="explore-card">
<div class="explore-card__icon">&#127912;</div>
<strong>&#33394;&#24425;&#25506;&#32034;</strong>
<small>&#25353;&#33394;&#24425;&#31579;&#36873;&#20316;&#21697;</small>
</div>
<div class="explore-card">
<div class="explore-card__icon">&#128336;</div>
<strong>&#26102;&#38388;&#32447;&#25506;&#32034;</strong>
<small>&#25353;&#26102;&#38388;&#26597;&#30475;&#28388;&#21457;</small>
</div>
<div class="explore-card">
<div class="explore-card__icon">&#127991;</div>
<strong>&#26631;&#31614;&#25506;&#32034;</strong>
<small>&#25353;&#26631;&#31614;&#25628;&#32034;&#20316;&#21697;</small>
</div>
</div>
</div>
<div class="orbit-system" aria-hidden="true">
<div class="orbit-system__core"></div>
<div class="orbit-system__ring orbit-system__ring--1">
<div class="orbit-system__satellite"><img src="./pinmian/5.jpg" alt="satellite"></div>
<div class="orbit-system__satellite"><img src="./pinmian/6.jpg" alt="satellite"></div>
<div class="orbit-system__satellite"><img src="./pinmian/7.jpg" alt="satellite"></div>
<div class="orbit-system__satellite"><img src="./pinmian/8.jpg" alt="satellite"></div>
</div>
<div class="orbit-system__ring orbit-system__ring--2">
<div class="orbit-system__satellite"><img src="./pinmian/9.jpg" alt="satellite"></div>
<div class="orbit-system__satellite"><img src="./pinmian/10.jpg" alt="satellite"></div>
<div class="orbit-system__satellite"><img src="./pinmian/11.jpg" alt="satellite"></div>
</div>
<div class="orbit-system__label">&#25318;&#25305;&#26059;&#36716;</div>
</div>
<div class="orbit-recommend">
<p class="badge">AI RECOMMEND</p>
<h3>AI &#26234;&#33021;&#25512;&#33616;</h3>
<p>&#22522;&#20110;&#20320;&#30340;&#27983;&#35272;&#34892;&#20026;&#65292;&#20026;&#20320;&#25512;&#33616;&#30456;&#20851;&#20316;&#21697;&#12290;</p>
<div class="orbit-recommend__card">
<img src="./pinmian/12.jpg" alt="Recommended work" loading="lazy">
<div class="orbit-recommend__info">
<strong>Coolbina Villa Estate</strong>
<span>&#26597;&#30475;&#26356;&#22810; &rarr;</span>
</div>
</div>
<div class="orbit-trending">
<p class="badge badge--sm">TRENDING &#36235;&#21183;&#20851;&#38190;&#35789;</p>
<div class="orbit-tags">
<span>&#31185;&#25216;&#24863;</span>
<span>&#26410;&#26469;&#20027;&#20041;</span>
<span>&#31354;&#38388;&#35774;&#35745;</span>
<span>&#21697;&#29260;&#35270;&#35273;</span>
<span>&#24037;&#19994;&#35774;&#35745;</span>
<span>AI&#29983;&#25104;</span>
<span>UI/UX</span>
<span>&#20809;&#24433;&#34920;&#29616;</span>
</div>
</div>
</div>
</div>
</section>'''

content = content.replace(old_section, new_section)

f = open(r'c:\Users\priest\Desktop\rerenwangzhan\index.html', 'w', encoding='utf-8')
f.write(content)
f.close()

print('HTML Done')
