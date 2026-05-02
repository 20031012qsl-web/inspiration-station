f = open(r'c:\Users\priest\Desktop\rerenwangzhan\index.html', 'r', encoding='utf-8')
content = f.read()
f.close()

old = '<article class="work-stream__item work-stream__item--one"><span>PROJECT 01</span><strong>俄罗斯方块</strong><small>Tetris</small></article>'
new = '<article class="work-stream__item work-stream__item--one" onclick="window.open(\'http://loca\', \'_blank\')" style="cursor:pointer"><span>PROJECT 01</span><strong>俄罗斯方块</strong><small>Tetris</small><img src="./elsfk.png" alt="俄罗斯方块" loading="lazy" class="work-stream__item-image"></article>'

content = content.replace(old, new, 1)

f = open(r'c:\Users\priest\Desktop\rerenwangzhan\index.html', 'w', encoding='utf-8')
f.write(content)
f.close()

print('Done')
