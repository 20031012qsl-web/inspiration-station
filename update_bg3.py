f = open(r'c:\Users\priest\Desktop\rerenwangzhan\styles.css', 'r', encoding='utf-8')
content = f.read()
f.close()

old = 'url("./4月30日/4月30日.gif")'
new = 'url("./4月30日(3)/4月30日(3).gif")'

content = content.replace(old, new)

f = open(r'c:\Users\priest\Desktop\rerenwangzhan\styles.css', 'w', encoding='utf-8')
f.write(content)
f.close()

print('Done')
