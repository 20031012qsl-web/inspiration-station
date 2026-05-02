f = open(r'c:\Users\priest\Desktop\rerenwangzhan\index.html', 'r', encoding='utf-8')
content = f.read()
f.close()

old_track = '''<div class="orbit-carousel__track" data-orbit-track>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/1.jpg" alt="Work 1" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 01</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/2.jpg" alt="Work 2" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 02</strong></figcaption></figure>
<figure class="orbit-card" data-cat="visual"><img src="./pinmian/3.jpg" alt="Work 3" loading="lazy"><figcaption><span>VISUAL</span><strong>&#35270;&#35273;&#31995;&#32479; 03</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/5.jpg" alt="Featured work" loading="lazy"><figcaption><span>FEATURED</span><strong>&#35270;&#35273;&#23454;&#39564;&#32452;</strong></figcaption></figure>
<figure class="orbit-card" data-cat="3d"><img src="./pinmian/8.jpg" alt="Work 5" loading="lazy"><figcaption><span>3D MODEL</span><strong>&#51D&#24314;&#27169; 05</strong></figcaption></figure>
<figure class="orbit-card" data-cat="ai"><img src="./pinmian/7.jpg" alt="Work 6" loading="lazy"><figcaption><span>AI</span><strong>AI&#23454;&#39564; 06</strong></figcaption></figure>
<figure class="orbit-card" data-cat="visual"><img src="./pinmian/9.jpg" alt="Work 7" loading="lazy"><figcaption><span>VISUAL</span><strong>&#35270;&#35273;&#20316;&#21697; 07</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/10.jpg" alt="Work 8" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 08</strong></figcaption></figure>
<figure class="orbit-card" data-cat="ai"><img src="./pinmian/14.jpg" alt="Work 9" loading="lazy"><figcaption><span>AI</span><strong>AI&#23454;&#39564; 09</strong></figcaption></figure>
<figure class="orbit-card" data-cat="visual"><img src="./pinmian/11.jpg" alt="Work 10" loading="lazy"><figcaption><span>VISUAL</span><strong>&#35270;&#35273;&#20316;&#21697; 10</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/12.jpg" alt="Work 11" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 11</strong></figcaption></figure>
<figure class="orbit-card" data-cat="3d"><img src="./pinmian/15.jpg" alt="Work 12" loading="lazy"><figcaption><span>3D MODEL</span><strong>3D&#24314;&#27169; 12</strong></figcaption></figure>
<figure class="orbit-card" data-cat="ai"><img src="./pinmian/17.jpg" alt="Work 13" loading="lazy"><figcaption><span>AI</span><strong>AI&#23454;&#39564; 13</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/16.jpg" alt="Work 14" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 14</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/1.jpg" alt="Work 1" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 01</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/2.jpg" alt="Work 2" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 02</strong></figcaption></figure>
<figure class="orbit-card" data-cat="visual"><img src="./pinmian/3.jpg" alt="Work 3" loading="lazy"><figcaption><span>VISUAL</span><strong>&#35270;&#35273;&#31995;&#32479; 03</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/5.jpg" alt="Featured work" loading="lazy"><figcaption><span>FEATURED</span><strong>&#35270;&#35273;&#23454;&#39564;&#32452;</strong></figcaption></figure>
<figure class="orbit-card" data-cat="3d"><img src="./pinmian/8.jpg" alt="Work 5" loading="lazy"><figcaption><span>3D MODEL</span><strong>&#51D&#24314;&#27169; 05</strong></figcaption></figure>
<figure class="orbit-card" data-cat="ai"><img src="./pinmian/7.jpg" alt="Work 6" loading="lazy"><figcaption><span>AI</span><strong>AI&#23454;&#39564; 06</strong></figcaption></figure>
<figure class="orbit-card" data-cat="visual"><img src="./pinmian/9.jpg" alt="Work 7" loading="lazy"><figcaption><span>VISUAL</span><strong>&#35270;&#35273;&#20316;&#21697; 07</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/10.jpg" alt="Work 8" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 08</strong></figcaption></figure>
<figure class="orbit-card" data-cat="ai"><img src="./pinmian/14.jpg" alt="Work 9" loading="lazy"><figcaption><span>AI</span><strong>AI&#23454;&#39564; 09</strong></figcaption></figure>
<figure class="orbit-card" data-cat="visual"><img src="./pinmian/11.jpg" alt="Work 10" loading="lazy"><figcaption><span>VISUAL</span><strong>&#35270;&#35273;&#20316;&#21697; 10</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/12.jpg" alt="Work 11" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 11</strong></figcaption></figure>
<figure class="orbit-card" data-cat="3d"><img src="./pinmian/15.jpg" alt="Work 12" loading="lazy"><figcaption><span>3D MODEL</span><strong>3D&#24314;&#27169; 12</strong></figcaption></figure>
<figure class="orbit-card" data-cat="ai"><img src="./pinmian/17.jpg" alt="Work 13" loading="lazy"><figcaption><span>AI</span><strong>AI&#23454;&#39564; 13</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/16.jpg" alt="Work 14" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 14</strong></figcaption></figure>
</div>'''

new_track = '''<div class="orbit-carousel__track" data-orbit-track>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/5.jpg" alt="Work 1" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 01</strong></figcaption></figure>
<figure class="orbit-card" data-cat="visual"><img src="./pinmian/6.jpg" alt="Work 2" loading="lazy"><figcaption><span>VISUAL</span><strong>&#35270;&#35273;&#20316;&#21697; 02</strong></figcaption></figure>
<figure class="orbit-card" data-cat="ai"><img src="./pinmian/7.jpg" alt="Work 3" loading="lazy"><figcaption><span>AI</span><strong>AI&#23454;&#39564; 03</strong></figcaption></figure>
<figure class="orbit-card" data-cat="3d"><img src="./pinmian/8.jpg" alt="Work 4" loading="lazy"><figcaption><span>3D MODEL</span><strong>3D&#24314;&#27169; 04</strong></figcaption></figure>
<figure class="orbit-card" data-cat="visual"><img src="./pinmian/9.jpg" alt="Work 5" loading="lazy"><figcaption><span>VISUAL</span><strong>&#35270;&#35273;&#20316;&#21697; 05</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/10.jpg" alt="Work 6" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 06</strong></figcaption></figure>
<figure class="orbit-card" data-cat="visual"><img src="./pinmian/11.jpg" alt="Work 7" loading="lazy"><figcaption><span>VISUAL</span><strong>&#35270;&#35273;&#20316;&#21697; 07</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/12.jpg" alt="Work 8" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 08</strong></figcaption></figure>
<figure class="orbit-card" data-cat="ai"><img src="./pinmian/14.jpg" alt="Work 9" loading="lazy"><figcaption><span>AI</span><strong>AI&#23454;&#39564; 09</strong></figcaption></figure>
<figure class="orbit-card" data-cat="3d"><img src="./pinmian/15.jpg" alt="Work 10" loading="lazy"><figcaption><span>3D MODEL</span><strong>3D&#24314;&#27169; 10</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/16.jpg" alt="Work 11" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 11</strong></figcaption></figure>
<figure class="orbit-card" data-cat="ai"><img src="./pinmian/17.jpg" alt="Work 12" loading="lazy"><figcaption><span>AI</span><strong>AI&#23454;&#39564; 12</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/18.jpg" alt="Work 13" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 13</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/5.jpg" alt="Work 1" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 01</strong></figcaption></figure>
<figure class="orbit-card" data-cat="visual"><img src="./pinmian/6.jpg" alt="Work 2" loading="lazy"><figcaption><span>VISUAL</span><strong>&#35270;&#35273;&#20316;&#21697; 02</strong></figcaption></figure>
<figure class="orbit-card" data-cat="ai"><img src="./pinmian/7.jpg" alt="Work 3" loading="lazy"><figcaption><span>AI</span><strong>AI&#23454;&#39564; 03</strong></figcaption></figure>
<figure class="orbit-card" data-cat="3d"><img src="./pinmian/8.jpg" alt="Work 4" loading="lazy"><figcaption><span>3D MODEL</span><strong>3D&#24314;&#27169; 04</strong></figcaption></figure>
<figure class="orbit-card" data-cat="visual"><img src="./pinmian/9.jpg" alt="Work 5" loading="lazy"><figcaption><span>VISUAL</span><strong>&#35270;&#35273;&#20316;&#21697; 05</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/10.jpg" alt="Work 6" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 06</strong></figcaption></figure>
<figure class="orbit-card" data-cat="visual"><img src="./pinmian/11.jpg" alt="Work 7" loading="lazy"><figcaption><span>VISUAL</span><strong>&#35270;&#35273;&#20316;&#21697; 07</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/12.jpg" alt="Work 8" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 08</strong></figcaption></figure>
<figure class="orbit-card" data-cat="ai"><img src="./pinmian/14.jpg" alt="Work 9" loading="lazy"><figcaption><span>AI</span><strong>AI&#23454;&#39564; 09</strong></figcaption></figure>
<figure class="orbit-card" data-cat="3d"><img src="./pinmian/15.jpg" alt="Work 10" loading="lazy"><figcaption><span>3D MODEL</span><strong>3D&#24314;&#27169; 10</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/16.jpg" alt="Work 11" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 11</strong></figcaption></figure>
<figure class="orbit-card" data-cat="ai"><img src="./pinmian/17.jpg" alt="Work 12" loading="lazy"><figcaption><span>AI</span><strong>AI&#23454;&#39564; 12</strong></figcaption></figure>
<figure class="orbit-card" data-cat="graphic"><img src="./pinmian/18.jpg" alt="Work 13" loading="lazy"><figcaption><span>GRAPHIC</span><strong>&#24179;&#38754;&#20316;&#21697; 13</strong></figcaption></figure>
</div>'''

content = content.replace(old_track, new_track)

f = open(r'c:\Users\priest\Desktop\rerenwangzhan\index.html', 'w', encoding='utf-8')
f.write(content)
f.close()

print('HTML Done')
