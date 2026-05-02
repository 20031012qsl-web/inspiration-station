f = open(r'c:\Users\priest\Desktop\rerenwangzhan\styles.css', 'r', encoding='utf-8')
content = f.read()
f.close()

old = '.marquee__track{display:flex;width:max-content;gap:48px;padding:18px 0;color:var(--text-tertiary);font:600 12px/1 var(--font-mono);letter-spacing:.18em;animation:marquee 28s linear infinite}@keyframes marquee{to{transform:translateX(-50%)}}'
new = '.marquee__track{display:flex;width:max-content;padding:18px 0;color:var(--text-tertiary);font:600 12px/1 var(--font-mono);letter-spacing:.18em;animation:marquee 28s linear infinite}.marquee__track span{margin-right:48px}@keyframes marquee{to{transform:translateX(-50%)}}'

content = content.replace(old, new)

f = open(r'c:\Users\priest\Desktop\rerenwangzhan\styles.css', 'w', encoding='utf-8')
f.write(content)
f.close()

print('Done')
