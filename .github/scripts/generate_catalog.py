#!/usr/bin/env python3
"""
Auto-generates docs/catalog/index.md from frontmatter of catalog cards.
Triggered by GitHub Actions on every push to docs/catalog/*.md
"""

import os
import re
from collections import defaultdict

CATALOG_DIR = 'docs/catalog'
OUTPUT_FILE = 'docs/catalog/index.md'
SKIP_FILES = {'index.md', 'assessment-scale.md', 'template-card.md'}

CATEGORY_LABELS = {
    'network/vpn':              ('Network', 'VPN'),
    'network/dns':              ('Network', 'DNS'),
    'network/proxy':            ('Network', 'Proxy'),
    'network':                  ('Network', 'General'),
    'identity':                 ('Identity', ''),
    'storage/sync':             ('Storage', 'Sync'),
    'storage/backup':           ('Storage', 'Backup'),
    'storage/cloud':            ('Storage', 'Cloud'),
    'storage':                  ('Storage', 'General'),
    'observability/dashboards':  ('Observability', 'Dashboards'),
    'observability/metrics':     ('Observability', 'Metrics'),
    'observability/monitoring':  ('Observability', 'Monitoring'),
    'observability':            ('Observability', ''),
    'compute':                  ('Compute', ''),
    'security/password-manager':('Security', 'Password Manager'),
    'security/passwords':       ('Security', 'Password Manager'),
    'security/secrets':         ('Security', 'Secrets'),
    'security':                 ('Security', 'General'),
    'applications/media':       ('Applications', 'Media'),
    'applications/git':         ('Applications', 'Version Control'),
    'applications/photos':      ('Applications', 'Photos'),
    'applications/documents':   ('Applications', 'Documents'),
    'applications/notes':       ('Applications', 'Notes'),
    'applications/cloud':       ('Applications', 'Cloud Platform'),
    'applications/automation':  ('Applications', 'Automation'),
    'applications':             ('Applications', 'General'),
    'cloud':                    ('Cloud', ''),
}

def parse_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None
    
    fm = {}
    for line in match.group(1).splitlines():
        m = re.match(r'^(\w[\w_-]*):\s*["\']?(.+?)["\']?\s*$', line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"\'')
    
    return fm

def get_section(category):
    cat = category.lower().strip()
    for key in CATEGORY_LABELS:
        if cat == key or cat.startswith(key + '/'):
            return CATEGORY_LABELS[key]
    return ('Other', '')

def autonomy_sort_key(level):
    return {'A3': 0, 'A2': 1, 'A1': 2, 'A0': 3}.get(level, 9)

def generate_index():
    cards = []
    
    for filename in os.listdir(CATALOG_DIR):
        if filename in SKIP_FILES or not filename.endswith('.md'):
            continue
        
        filepath = os.path.join(CATALOG_DIR, filename)
        fm = parse_frontmatter(filepath)
        if not fm:
            continue
        
        # Skip nav_exclude cards
        if fm.get('nav_exclude', '').lower() == 'true':
            continue
        
        title = fm.get('title', filename.replace('.md', '').replace('-', ' ').title())
        category = fm.get('category', 'other')
        autonomy = fm.get('autonomy_level', '—')
        transparency = fm.get('transparency_level', '—')
        slug = filename.replace('.md', '')
        
        # Get description from brief description section
        with open(filepath, 'r', encoding='utf-8') as f:
            body = f.read()
        desc_match = re.search(r'## Brief Description\s*\n+(.+?)(?:\n\n|\n##)', body, re.DOTALL)
        description = ''
        if desc_match:
            description = desc_match.group(1).strip().replace('\n', ' ')
            # Take first sentence only
            first_sentence = re.split(r'(?<=[.!?])\s', description)[0]
            description = first_sentence[:120] + ('...' if len(first_sentence) > 120 else '')
        
        section, subsection = get_section(category)
        
        cards.append({
            'title': title,
            'slug': slug,
            'autonomy': autonomy,
            'transparency': transparency,
            'description': description,
            'section': section,
            'subsection': subsection,
            'category': category,
        })
    
    # Group by section → subsection
    grouped = defaultdict(lambda: defaultdict(list))
    for card in cards:
        grouped[card['section']][card['subsection']].append(card)
    
    # Sort cards within each group by autonomy level
    for section in grouped:
        for subsection in grouped[section]:
            grouped[section][subsection].sort(key=lambda c: autonomy_sort_key(c['autonomy']))
    
    # Define section order
    section_order = ['Network', 'Identity', 'Storage', 'Observability', 'Compute', 'Security', 'Applications', 'Cloud', 'Other']
    
    lines = []
    lines.append('---')
    lines.append('title: "Technology Catalog"')
    lines.append('nav_order: 5')
    lines.append('has_children: true')
    lines.append('---')
    lines.append('')
    lines.append('# Technology Catalog')
    lines.append('')
    lines.append('Each technology is evaluated on two axes:')
    lines.append('')
    lines.append('- **Autonomy Level** (A0–A3): operational independence from cloud and internet.')
    lines.append('- **Transparency Level** (T0–T2): architectural openness and auditability.')
    lines.append('')
    lines.append('Cards also include a **Philosophical Assessment** — Pause, Exit, Recoverability, Visibility — based on the [whose.world](https://whose.world) criteria.')
    lines.append('')
    lines.append('The catalog includes both autonomous alternatives and the mainstream services they replace. The contrast makes the trade-offs visible.')
    lines.append('')
    lines.append('See [Assessment Scale](assessment-scale.md) for detailed definitions.')
    lines.append('')
    lines.append(f'*{len(cards)} technologies evaluated.*')
    lines.append('')
    lines.append('---')
    lines.append('')
    
    for section in section_order:
        if section not in grouped:
            continue
        
        lines.append(f'## {section}')
        lines.append('')
        
        subsections = grouped[section]
        
        for subsection, sub_cards in sorted(subsections.items()):
            if subsection:
                lines.append(f'### {subsection}')
                lines.append('')
            
            lines.append('| Technology | Autonomy | Transparency | Description |')
            lines.append('|------------|----------|--------------|-------------|')
            
            for card in sub_cards:
                desc = card['description'] or '—'
                lines.append(f"| [{card['title']}]({card['slug']}.md) | **{card['autonomy']}** | **{card['transparency']}** | {desc} |")
            
            lines.append('')
        
        lines.append('---')
        lines.append('')
    
    lines.append('*The catalog grows. Contributions welcome — see [CONTRIBUTING](../../CONTRIBUTING.md).*')
    lines.append('')
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    
    print(f'Generated {OUTPUT_FILE} with {len(cards)} cards.')

if __name__ == '__main__':
    generate_index()
