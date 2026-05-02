f = open(r'c:\Users\priest\Desktop\rerenwangzhan\index.html', 'r', encoding='utf-8')
content = f.read()
f.close()

old = '<div class="marquee__track"><span>MODEL FEEDBACK</span><span>VISUAL ARCHIVE</span><span>GRAPHIC SYSTEM</span><span>3D STUDY</span><span>PROMPT EXPERIMENT</span><span>MODEL FEEDBACK</span><span>VISUAL ARCHIVE</span><span>GRAPHIC SYSTEM</span></div>'
new = '<div class="marquee__track"><span>MODEL FEEDBACK</span><span>VISUAL ARCHIVE</span><span>GRAPHIC SYSTEM</span><span>3D STUDY</span><span>PROMPT EXPERIMENT</span><span>MODEL FEEDBACK</span><span>VISUAL ARCHIVE</span><span>GRAPHIC SYSTEM</span><span>3D STUDY</span><span>PROMPT EXPERIMENT</span></div>'

content = content.replace(old, new)

f = open(r'c:\Users\priest\Desktop\rerenwangzhan\index.html', 'w', encoding='utf-8')
f.write(content)
f.close()

print('Done')
