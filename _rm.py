from pathlib import Path

p = Path(r"c:\Users\priest\Desktop\rerenwangzhan\index.html")
t = p.read_text(encoding="utf-8", errors="replace")
s = t.find('<div class="hero-portrait')
if s == -1:
    print("not found")
else:
    d, i, e = 0, s, s
    while i < len(t):
        if t[i:i+4] == '<div':
            d += 1
        elif t[i:i+6] == '</div>':
            d -= 1
            if d == 0:
                e = i + 6
                break
        i += 1
    t = t[:s] + t[e:]
    p.write_text(t, encoding="utf-8")
    print("done")
