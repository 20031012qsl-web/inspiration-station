from pathlib import Path

path = Path(r"c:\Users\priest\Desktop\rerenwangzhan\index.html")
text = path.read_text(encoding="utf-8", errors="replace")

start = text.find('<div class="hero-portrait')
if start != -1:
    depth = 0
    i = start
    end = start
    while i < len(text):
        if text[i:i+4] == '<div':
            depth += 1
        elif text[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                end = i + 6
                break
        i += 1
    if end > start:
        text = text[:start] + text[end:]
        path.write_text(text, encoding="utf-8")
        print(f"Removed {end - start} chars")
    else:
        print("Could not find closing tag")
else:
    print("hero-portrait not found")
