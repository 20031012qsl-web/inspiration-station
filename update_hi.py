f = open(r'c:\Users\priest\Desktop\rerenwangzhan\index.html', 'r', encoding='utf-8')
content = f.read()
f.close()

old = '<span class="hero-word" style="--i:0">Hi,</span>'
new = '<span class="hero-word hero-word--accent" style="--i:0">Hi,</span>'

content = content.replace(old, new)

f = open(r'c:\Users\priest\Desktop\rerenwangzhan\index.html', 'w', encoding='utf-8')
f.write(content)
f.close()

print('Done')
