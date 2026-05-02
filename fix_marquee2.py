f = open(r'c:\Users\priest\Desktop\rerenwangzhan\index.html', 'r', encoding='utf-8')
content = f.read()
f.close()

old = '<div class="marquee__track"><span>MODEL FEEDBACK</span><span>VISUAL ARCHIVE</span><span>GRAPHIC SYSTEM</span><span>3D STUDY</span><span>PROMPT EXPERIMENT</span><span>MODEL FEEDBACK</span><span>VISUAL ARCHIVE</span><span>GRAPHIC SYSTEM</span><span>3D STUDY</span><span>PROMPT EXPERIMENT</span></div>'
new = '<div class="marquee__track"><span>MODEL FEEDBACK</span><span>VISUAL ARCHIVE</span><span>GRAPHIC SYSTEM</span><span>3D STUDY</span><span>PROMPT EXPERIMENT</span><span>MODEL FEEDBACK</span><span>VISUAL ARCHIVE</span><span>GRAPHIC SYSTEM</span><span>3D STUDY</span><span>PROMPT EXPERIMENT</span></div>'

# Already correct, just need to fix CSS gap issue
# The problem is the gap causes the 50% translate to not align perfectly
# Fix: use margin instead of gap, and ensure exact duplication

f = open(r'c:\Users\priest\Desktop\rerenwangzhan\index.html', 'w', encoding='utf-8')
f.write(content)
f.close()

print('Done')
