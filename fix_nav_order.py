import os, re

catalog = 'docs/catalog'
skip = {'index.md', 'assessment-scale.md', 'template-card.md'}
fixed = []

for fname in os.listdir(catalog):
    if fname in skip or not fname.endswith('.md'):
        continue
    path = os.path.join(catalog, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    
    if 'nav_order:' not in content:
        content = re.sub(r'(parent:.*?\n)', r'\1nav_order: 99\n', content, count=1)
        fixed.append(fname)
    else:
        new = re.sub(r'nav_order:\s*(?!99)\d+', 'nav_order: 99', content)
        if new != content:
            content = new
            fixed.append(fname)
    
    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Fixed {len(fixed)} files")
