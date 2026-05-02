f = open(r'c:\Users\priest\Desktop\rerenwangzhan\index.html', 'r', encoding='utf-8')
content = f.read()
f.close()

content = content.replace("window.open('http://loca', '_blank')", "window.open('http://localhost:5500/', '_blank')")

f = open(r'c:\Users\priest\Desktop\rerenwangzhan\index.html', 'w', encoding='utf-8')
f.write(content)
f.close()

print('Done')
