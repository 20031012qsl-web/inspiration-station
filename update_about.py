f = open(r'c:\Users\priest\Desktop\rerenwangzhan\index.html', 'r', encoding='utf-8')
content = f.read()
f.close()

# Chinese: remove 我 and 自己
content = content.replace('&#25105;&#35757;&#32451;&#27169;&#22411;&#65292;&#20063;&#35757;&#32451;&#33258;&#24049;&#35266;&#30475;&#19990;&#30028;&#30340;&#26041;&#24335;', '&#35757;&#32451;&#27169;&#22411;&#65292;&#20063;&#35757;&#32451;&#35266;&#30475;&#19990;&#30028;&#30340;&#26041;&#24335;')

# English: remove I and my
content = content.replace('I train models, and I train my own way of seeing.', 'Training models, and training the way of seeing.')

f = open(r'c:\Users\priest\Desktop\rerenwangzhan\index.html', 'w', encoding='utf-8')
f.write(content)
f.close()

print('Done')
