$f = 'c:\Users\priest\Desktop\rerenwangzhan\index.html'
$c = [System.IO.File]::ReadAllText($f, [System.Text.Encoding]::UTF8)

$oldPattern = '<section class="section works" id="works" aria-labelledby="works-title">'
$endPattern = '</div></section><section class="section stage modeling-stage-section" id="stage"'

$startIdx = $c.IndexOf($oldPattern)
$endIdx = $c.IndexOf($endPattern, $startIdx)

if ($startIdx -ge 0 -and $endIdx -ge 0) {
  $newSection = '<section class="section works" id="works" aria-labelledby="works-title"><div class="container"><div class="section-head reveal"><p class="badge">VISUAL ARCHIVE</p><h2 id="works-title">多维视觉作品归档</h2><p>A multidimensional archive for AI experiments, graphic studies, visual systems, and 3D modeling works.</p></div><div class="magazine-grid reveal"><div class="magazine-row magazine-row--one"><div class="magazine-card magazine-card--large"><div class="magazine-card__image"><img src="./pinmian/5.jpg" alt="平面作品" loading="lazy"></div><div class="magazine-card__overlay"><span class="magazine-card__tag">FEATURED</span><h3>视觉实验组</h3></div></div><div class="magazine-card magazine-card--medium"><div class="magazine-card__image"><img src="./pinmian/6.jpg" alt="平面作品" loading="lazy"></div><div class="magazine-card__overlay"><span class="magazine-card__tag">GRAPHIC</span><h3>版式研究</h3></div></div><div class="magazine-card magazine-card--small"><div class="magazine-card__image"><img src="./pinmian/7.jpg" alt="平面作品" loading="lazy"></div><div class="magazine-card__overlay"><span class="magazine-card__tag">PROMPT</span></div></div></div><div class="magazine-row magazine-row--two"><div class="magazine-card magazine-card--small"><div class="magazine-card__image"><img src="./pinmian/8.jpg" alt="平面作品" loading="lazy"></div><div class="magazine-card__overlay"><span class="magazine-card__tag">MODEL</span></div></div><div class="magazine-card magazine-card--medium"><div class="magazine-card__image"><img src="./pinmian/9.jpg" alt="平面作品" loading="lazy"></div><div class="magazine-card__overlay"><span class="magazine-card__tag">SYSTEM</span><h3>视觉系统</h3></div></div><div class="magazine-card magazine-card--large"><div class="magazine-card__image"><img src="./pinmian/10.jpg" alt="平面作品" loading="lazy"></div><div class="magazine-card__overlay"><span class="magazine-card__tag">PROCESS</span><h3>过程样本</h3></div></div></div></div><div class="magazine-carousel reveal"><div class="magazine-carousel__track"><div class="carousel-slide"><img src="./pinmian/11.jpg" alt="" loading="lazy"></div><div class="carousel-slide"><img src="./pinmian/12.jpg" alt="" loading="lazy"></div><div class="carousel-slide"><img src="./pinmian/14.jpg" alt="" loading="lazy"></div><div class="carousel-slide"><img src="./pinmian/15.jpg" alt="" loading="lazy"></div><div class="carousel-slide"><img src="./pinmian/16.jpg" alt="" loading="lazy"></div><div class="carousel-slide"><img src="./pinmian/17.jpg" alt="" loading="lazy"></div><div class="carousel-slide"><img src="./pinmian/18.jpg" alt="" loading="lazy"></div><div class="carousel-slide"><img src="./pinmian/img_v3_02pv_3679e745-d15f-4062-96ea-432d1677889g_MIDDLE_WEBP.webp" alt="" loading="lazy"></div></div></div></div></section>'

  $before = $c.Substring(0, $startIdx)
  $after = $c.Substring($endIdx)
  $newContent = $before + $newSection + $after

  $utf8NoBom = New-Object System.Text.UTF8Encoding $false
  [System.IO.File]::WriteAllText($f, $newContent, $utf8NoBom)
  Write-Output "Done! Replaced works section with UTF8 encoding."
} else {
  Write-Output "Pattern not found. startIdx=$startIdx endIdx=$endIdx"
}
