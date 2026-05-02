f = open(r'c:\Users\priest\Desktop\rerenwangzhan\styles.css', 'r', encoding='utf-8')
content = f.read()
f.close()

old = '.hero__grid{position:absolute;inset:0;opacity:.55;background:radial-gradient(circle at 50% 54%,rgba(var(--accent-rgb),.16),transparent 12rem),radial-gradient(circle at 52% 48%,rgba(var(--cyan-rgb),.16),transparent 34rem)}'
new = '.hero__bg-image{position:absolute;inset:0;z-index:0;background:url("./4月30日/4月30日.gif") center/cover no-repeat;opacity:.3}.hero__grid{position:absolute;inset:0;z-index:1;opacity:.55;background:radial-gradient(circle at 50% 54%,rgba(var(--accent-rgb),.16),transparent 12rem),radial-gradient(circle at 52% 48%,rgba(var(--cyan-rgb),.16),transparent 34rem)}'

content = content.replace(old, new)

f = open(r'c:\Users\priest\Desktop\rerenwangzhan\styles.css', 'w', encoding='utf-8')
f.write(content)
f.close()

print('CSS Done')
