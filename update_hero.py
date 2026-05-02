f = open(r'c:\Users\priest\Desktop\rerenwangzhan\index.html', 'r', encoding='utf-8')
content = f.read()
f.close()

old = '<section class="hero hero-constellation" id="top" aria-labelledby="hero-title"><div class="hero__grid" aria-hidden="true"></div><div class="star-field" aria-hidden="true"></div>'
new = '<section class="hero hero-constellation" id="top" aria-labelledby="hero-title"><div class="hero__bg-image" aria-hidden="true"></div><div class="hero__grid" aria-hidden="true"></div><div class="star-field" aria-hidden="true"></div>'

content = content.replace(old, new)

f = open(r'c:\Users\priest\Desktop\rerenwangzhan\index.html', 'w', encoding='utf-8')
f.write(content)
f.close()

print('HTML Done')
