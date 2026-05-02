f = open(r'c:\Users\priest\Desktop\rerenwangzhan\styles.css', 'r', encoding='utf-8')
content = f.read()
f.close()

old = '.hero__bg-image{position:absolute;inset:0;z-index:0;background:url("./4月30日/4月30日.gif") center/cover no-repeat;opacity:.3}'
new = '.hero__bg-image{position:absolute;inset:0;z-index:0;background:url("./4月30日/4月30日.gif") center/cover no-repeat;opacity:.6}'

content = content.replace(old, new)

f = open(r'c:\Users\priest\Desktop\rerenwangzhan\styles.css', 'w', encoding='utf-8')
f.write(content)
f.close()

print('Done')
