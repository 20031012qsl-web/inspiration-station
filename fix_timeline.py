f = open(r'c:\Users\priest\Desktop\rerenwangzhan\styles.css', 'r', encoding='utf-8')
content = f.read()
f.close()

old = '.timeline-item__date{color:var(--accent);font-size:12px;letter-spacing:.12em}'
new = '.timeline-item__date{color:var(--accent);font-size:12px;letter-spacing:.12em;padding-left:24px}'

content = content.replace(old, new)

f = open(r'c:\Users\priest\Desktop\rerenwangzhan\styles.css', 'w', encoding='utf-8')
f.write(content)
f.close()

print('Done')
