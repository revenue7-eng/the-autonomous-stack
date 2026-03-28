#!/usr/bin/env python3
"""
Single source of truth: generates all data-driven content from catalog card frontmatter.

Triggered by GitHub Actions on every push to docs/catalog/*.md
(see .github/workflows/generate-catalog.yml).

Generates:
  1. docs/catalog/index.md        — full markdown catalog grouped by category
  2. docs/audit.html              — <option> list between AUTO:AUDIT_OPTIONS markers
  3. docs/catalog-index.html      — CARDS[] JS array between AUTO:CATALOG_CARDS markers
  4. map.html                     — CARDS[] JS array between AUTO:MAP_CARDS markers
  5. README.md, index.md, docs/index.md, docs/autonomy-map.html
     — technology count updated via regex replacement

All four outputs are derived from the same frontmatter fields:
  - title, category, autonomy_level, transparency_level, trajectory

Marker format:
  HTML files use <!-- AUTO:NAME:START --> / <!-- AUTO:NAME:END -->
  JS blocks use /* AUTO:NAME:START */ / /* AUTO:NAME:END */
  Everything between START and END is replaced. Surrounding code is preserved.
"""

import os
import re
from collections import defaultdict

CATALOG_DIR = 'docs/catalog'
SKIP_FILES = {'index.md', 'assessment-scale.md', 'template-card.md'}

# ── Category mapping for catalog/index.md ──────────────────────────────────

CATEGORY_LABELS = {
    'network/vpn':              ('Network', 'VPN'),
    'network/dns':              ('Network', 'DNS'),
    'network/proxy':            ('Network', 'Proxy'),
    'network':                  ('Network', 'General'),
    'identity':                 ('Identity', ''),
    'identity/auth':            ('Identity', ''),
    'storage/sync':             ('Storage', 'Sync'),
    'storage/backup':           ('Storage', 'Backup'),
    'storage/cloud':            ('Storage', 'Cloud'),
    'storage/database':         ('Storage', 'Database'),
    'storage/cache':            ('Storage', 'Cache'),
    'storage':                  ('Storage', 'General'),
    'observability/dashboards':  ('Observability', 'Dashboards'),
    'observability/metrics':     ('Observability', 'Metrics'),
    'observability/monitoring':  ('Observability', 'Monitoring'),
    'observability':            ('Observability', ''),
    'compute':                  ('Compute', ''),
    'compute/container':        ('Compute', 'Containers'),
    'compute/orchestration':    ('Compute', 'Orchestration'),
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
    'applications/ci-cd':       ('Applications', 'CI/CD'),
    'applications/version-control': ('Applications', 'Version Control'),
    'applications/wiki':        ('Applications', 'Documents & Wiki'),
    'applications':             ('Applications', 'General'),
    'cloud':                    ('Cloud', ''),
    'communication/email':      ('Communication', 'Email'),
    'communication/messaging':  ('Communication', 'Messaging'),
    'communication':            ('Communication', 'General'),
    'analytics/web':            ('Analytics', ''),
    'analytics':                ('Analytics', ''),
}

# High-level category for catalog-index.html grouping
CATEGORY_TO_GROUP = {
    'network':        'Network',
    'identity':       'Security',
    'storage':        'Storage',
    'observability':  'Observability',
    'compute':        'Compute',
    'compute/container':     'Compute',
    'compute/inference':     'Compute',
    'compute/os':            'Compute',
    'compute/virtualization':'Compute',
    'security':       'Security',
    'applications/media':         'Media & Content',
    'applications/photos':        'Media & Content',
    'applications/downloads':     'Media & Content',
    'applications/news':          'Media & Content',
    'applications/reading':       'Media & Content',
    'applications/cloud':         'Productivity',
    'applications/documents':     'Productivity',
    'applications/wiki':          'Productivity',
    'applications/notes':         'Productivity',
    'applications/finance':       'Productivity',
    'applications/household':     'Productivity',
    'applications/bookmarks':     'Productivity',
    'applications/search':        'Productivity',
    'applications/files':         'Productivity',
    'applications/version-control': 'Development',
    'applications/ci-cd':         'Development',
    'applications/automation':    'Automation & Home',
    'applications/remote-access': 'Remote Access',
    'applications':   'Applications',
    'cloud':          'Applications',
    'communication':  'Communication',
    'communication/email':        'Communication',
    'communication/messaging':    'Communication',
    'communication/notifications':'Communication',
    'analytics':      'Analytics',
    'analytics/web':  'Analytics',
}

SECTION_ORDER = ['Network', 'Storage', 'Compute', 'Security', 'Observability',
                 'Communication', 'Analytics', 'Productivity', 'Media & Content',
                 'Development', 'Automation & Home', 'Remote Access', 'Applications', 'Other']


# ── Frontmatter parser ─────────────────────────────────────────────────────

def parse_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None, content

    fm = {}
    for line in match.group(1).splitlines():
        m = re.match(r'^(\w[\w_-]*):\s*["\']?(.+?)["\']?\s*$', line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"\'')

    return fm, content


def get_section(category):
    cat = category.lower().strip()
    for key in CATEGORY_LABELS:
        if cat == key or cat.startswith(key + '/'):
            return CATEGORY_LABELS[key]
    return ('Other', '')


def get_group(category):
    """Map detailed category to high-level group for catalog-index."""
    cat = category.lower().strip()
    # Try exact match first (e.g. applications/media -> Media & Content)
    if cat in CATEGORY_TO_GROUP:
        return CATEGORY_TO_GROUP[cat]
    # Then top-level (e.g. applications -> Applications)
    top = cat.split('/')[0]
    return CATEGORY_TO_GROUP.get(top, 'Applications')


def autonomy_sort_key(level):
    return {'A3': 0, 'A2': 1, 'A1': 2, 'A0': 3}.get(level, 9)


# ── Load all cards ─────────────────────────────────────────────────────────

def load_cards():
    cards = []

    for filename in sorted(os.listdir(CATALOG_DIR)):
        if filename in SKIP_FILES or not filename.endswith('.md'):
            continue

        filepath = os.path.join(CATALOG_DIR, filename)
        fm, body = parse_frontmatter(filepath)
        if not fm:
            continue

        if fm.get('nav_exclude', '').lower() == 'true':
            continue

        title = fm.get('title', filename.replace('.md', '').replace('-', ' ').title())
        category = fm.get('category', 'other')
        autonomy = fm.get('autonomy_level', '—')
        transparency = fm.get('transparency_level', '—')
        trajectory = fm.get('trajectory', 'stable')
        slug = filename.replace('.md', '')

        # Extract description from Brief Description section
        desc_match = re.search(r'## Brief Description\s*\n+(.+?)(?:\n\n|\n##)', body, re.DOTALL)
        description = ''
        if desc_match:
            description = desc_match.group(1).strip().replace('\n', ' ')
            first_sentence = re.split(r'(?<=[.!?])\s', description)[0]
            description = first_sentence[:120] + ('...' if len(first_sentence) > 120 else '')

        section, subsection = get_section(category)
        group = get_group(category)

        # Numeric autonomy/transparency for JS
        a_num = int(autonomy[1]) if autonomy.startswith('A') else 0
        t_num = int(transparency[1]) if transparency.startswith('T') else 0

        # Parse dependency lists from frontmatter
        def parse_yaml_list(raw_text, field):
            m = re.search(rf'^{field}:\s*\[([^\]]*)\]', raw_text, re.MULTILINE)
            if not m or not m.group(1).strip():
                return []
            return [x.strip().strip('"\'\'') for x in m.group(1).split(',') if x.strip().strip('"\'\'')]

        depends_on = parse_yaml_list(body, 'depends_on')
        optional_deps = parse_yaml_list(body, 'optional_deps')

        cards.append({
            'title': title,
            'slug': slug,
            'autonomy': autonomy,
            'transparency': transparency,
            'a_num': a_num,
            't_num': t_num,
            'trajectory': trajectory,
            'description': description,
            'section': section,
            'subsection': subsection,
            'group': group,
            'category': category,
            'depends_on': depends_on,
            'optional_deps': optional_deps,
        })

    return cards


# ── Generator 1: docs/catalog/index.md ─────────────────────────────────────

def generate_catalog_index(cards):
    grouped = defaultdict(lambda: defaultdict(list))
    for card in cards:
        grouped[card['section']][card['subsection']].append(card)

    for section in grouped:
        for subsection in grouped[section]:
            grouped[section][subsection].sort(key=lambda c: autonomy_sort_key(c['autonomy']))

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
    lines.append('- **Autonomy Level** (A0\u2013A3): operational independence from cloud and internet.')
    lines.append('- **Transparency Level** (T0\u2013T2): architectural openness and auditability.')
    lines.append('')
    lines.append('Cards also include a **Philosophical Assessment** \u2014 Pause, Exit, Recoverability, Visibility \u2014 based on the [whose.world](https://whose.world) criteria.')
    lines.append('')
    lines.append('The catalog includes both autonomous alternatives and the mainstream services they replace. The contrast makes the trade-offs visible.')
    lines.append('')
    lines.append('See [Assessment Scale](assessment-scale.md) for detailed definitions.')
    lines.append('')
    lines.append(f'*{len(cards)} technologies evaluated.*')
    lines.append('')
    lines.append('---')
    lines.append('')

    for section in SECTION_ORDER:
        if section not in grouped:
            continue
        lines.append(f'## {section}')
        lines.append('')
        for subsection, sub_cards in sorted(grouped[section].items()):
            if subsection:
                lines.append(f'### {subsection}')
                lines.append('')
            lines.append('| Technology | Autonomy | Transparency | Description |')
            lines.append('|------------|----------|--------------|-------------|')
            for card in sub_cards:
                desc = card['description'] or '\u2014'
                lines.append(f"| [{card['title']}]({card['slug']}.md) | **{card['autonomy']}** | **{card['transparency']}** | {desc} |")
            lines.append('')
        lines.append('---')
        lines.append('')

    lines.append('*The catalog grows. [Add a technology \u2192](../card-builder.html) or see [CONTRIBUTING](../../CONTRIBUTING.md).*')
    lines.append('')

    output = os.path.join(CATALOG_DIR, 'index.md')
    with open(output, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'  catalog/index.md: {len(cards)} cards')


# ── Generator 2: docs/audit.html ───────────────────────────────────────────

def generate_audit_options(cards):
    sorted_cards = sorted(cards, key=lambda c: c['title'].lower())
    lines = []
    for card in sorted_cards:
        esc_title = card['title'].replace("'", "&#39;")
        lines.append(f'      <option value="{card["slug"]}" data-autonomy="{card["autonomy"]}" data-transparency="{card["transparency"]}">{esc_title}</option>')

    replace_between_markers(
        'docs/audit.html',
        '<!-- AUTO:AUDIT_OPTIONS:START -->',
        '<!-- AUTO:AUDIT_OPTIONS:END -->',
        '\n'.join(lines)
    )
    print(f'  audit.html: {len(sorted_cards)} options')


# ── Generator 3: docs/catalog-index.html ───────────────────────────────────

def generate_catalog_cards_js(cards):
    sorted_cards = sorted(cards, key=lambda c: c['title'].lower())
    lines = []
    for card in sorted_cards:
        esc_name = card['title'].replace("'", "\\'")
        esc_desc = card['description'].replace("'", "\\'")
        lines.append(
            f"  {{name:'{esc_name}',a:{card['a_num']},t:{card['t_num']},"
            f"cat:'{card['group']}',traj:'{card['trajectory']}',"
            f"url:'{card['slug']}',desc:'{esc_desc}'}},"
        )

    replace_between_markers(
        'docs/catalog-index.html',
        '/* AUTO:CATALOG_CARDS:START */',
        '/* AUTO:CATALOG_CARDS:END */',
        '\n'.join(lines)
    )
    print(f'  catalog-index.html: {len(sorted_cards)} cards')


# ── Generator 4: map.html ─────────────────────────────────────────────────

def generate_map_cards_js(cards):
    sorted_cards = sorted(cards, key=lambda c: c['title'].lower())
    lines = []
    for card in sorted_cards:
        esc_name = card['title'].replace("'", "\\'")
        lines.append(
            f"  {{name:'{esc_name}',a:{card['a_num']},t:{card['t_num']},"
            f"traj:'{card['trajectory']}',url:'{card['slug']}'}},"
        )

    replace_between_markers(
        'map.html',
        '/* AUTO:MAP_CARDS:START */',
        '/* AUTO:MAP_CARDS:END */',
        '\n'.join(lines)
    )
    print(f'  map.html: {len(sorted_cards)} cards')


# ── Marker replacement utility ─────────────────────────────────────────────

def replace_between_markers(filepath, start_marker, end_marker, new_content):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.index(start_marker)
    end_idx = content.index(end_marker)

    # Keep markers, replace content between them
    before = content[:start_idx + len(start_marker)]
    after = content[end_idx:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(before + '\n' + new_content + '\n' + after)


# ── Main ───────────────────────────────────────────────────────────────────

# ── Generator 5: update technology count in static files ────────────────────

COUNT_REPLACEMENTS = [
    # (filepath, regex_pattern, replacement_template)
    # {n} will be replaced with the actual count
    ('README.md',
     r'\d+ technologies evaluated on two axes',
     '{n} technologies evaluated on two axes'),
    ('README.md',
     r'how \d+ technologies depend',
     'how {n} technologies depend'),
    ('index.md',
     r'\d+ technologies, 12 constellations',
     '{n} technologies, 12 constellations'),
    ('index.md',
     r'\d+ technologies rated by Autonomy',
     '{n} technologies rated by Autonomy'),
    ('docs/index.md',
     r'\d+ technologies, 12 constellations',
     '{n} technologies, 12 constellations'),
    ('docs/autonomy-map.html',
     r'Today \d+ stars',
     'Today {n} stars'),
    ('docs/recommended-stack.md',
     r'\d+ technologies with detailed',
     '{n} technologies with detailed'),
    ('docs/recommended-stack.md',
     r'out of \d+ technologies evaluated',
     'out of {n} technologies evaluated'),
]






# ── Generator: docs/autonomy-map.html ─────────────────────────────────────

def generate_autonomy_map(cards):
    """Generate NODES and INBOUND data for the autonomy map visualization."""
    import json as _json
    from collections import Counter

    nodes = []
    for card in sorted(cards, key=lambda c: c['title'].lower()):
        nodes.append({
            'id': card['slug'],
            'n': card['title'],
            'a': card['a_num'],
            't': card['t_num'],
            'tr': card['trajectory'],
            'g': card['category'].split('/')[0] if card['category'] else 'other',
        })

    # Count inbound dependencies for node sizing
    all_slugs = {c['slug'] for c in cards}
    inbound = Counter()
    for card in cards:
        for dep in card.get('depends_on', []):
            if dep in all_slugs:
                inbound[dep] += 1
        for dep in card.get('optional_deps', []):
            if dep in all_slugs:
                inbound[dep] += 0.5

    inbound_dict = {k: v for k, v in inbound.items() if v > 0}

    nodes_json = _json.dumps(nodes, separators=(',', ':'))
    inbound_json = _json.dumps(inbound_dict, separators=(',', ':'))

    data_block = f'const NODES={nodes_json};\nconst INBOUND={inbound_json};'

    replace_between_markers(
        'docs/autonomy-map.html',
        '/* AUTO:AUTONOMY_MAP_DATA:START */',
        '/* AUTO:AUTONOMY_MAP_DATA:END */',
        data_block
    )
    print(f'  autonomy-map.html: {len(nodes)} stars')


# ── Generator: docs/dependency-graph.html ──────────────────────────────────

def generate_dependency_graph(cards):
    """Generate DATA JSON for the dependency graph visualization."""
    import json as _json

    nodes = []
    for card in sorted(cards, key=lambda c: c['title'].lower()):
        nodes.append({
            'id': card['slug'],
            'n': card['title'],
            'g': card['category'].split('/')[0] if card['category'] else 'other',
            'a': card['a_num'],
            't': card['t_num'],
            'tr': card['trajectory'],
            'deps': len(card.get('depends_on', [])),
            'opts': len(card.get('optional_deps', [])),
        })

    edges_req = []
    edges_opt = []
    all_slugs = {c['slug'] for c in cards}

    for card in cards:
        for dep in card.get('depends_on', []):
            if dep in all_slugs:
                edges_req.append({'from': card['slug'], 'to': dep})
        for dep in card.get('optional_deps', []):
            if dep in all_slugs:
                edges_opt.append({'from': card['slug'], 'to': dep})

    data = _json.dumps({'nodes': nodes, 'req': edges_req, 'opt': edges_opt}, separators=(',', ':'))

    replace_between_markers(
        'docs/dependency-graph.html',
        '/* AUTO:DEPENDENCY_GRAPH_DATA:START */',
        '/* AUTO:DEPENDENCY_GRAPH_DATA:END */',
        'const DATA=' + data + ';'
    )
    print(f'  dependency-graph.html: {len(nodes)} nodes, {len(edges_req)}+{len(edges_opt)} edges')


def update_technology_counts(cards):
    n = len(cards)
    updated_files = set()

    for filepath, pattern, template in COUNT_REPLACEMENTS:
        replacement = template.replace('{n}', str(n))

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = re.sub(pattern, replacement, content)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated_files.add(filepath)

    print(f'  technology counts: {n} in {", ".join(sorted(updated_files)) or "no changes"}')


# ── Main ───────────────────────────────────────────────────────────────────

def main():
    print('Loading cards from frontmatter...')
    cards = load_cards()
    print(f'Found {len(cards)} cards.\n')

    print('Generating:')
    generate_catalog_index(cards)
    generate_audit_options(cards)
    generate_catalog_cards_js(cards)
    generate_map_cards_js(cards)
    generate_autonomy_map(cards)
    generate_dependency_graph(cards)
    update_technology_counts(cards)

    print(f'\nDone. All outputs generated from {len(cards)} cards.')


if __name__ == '__main__':
    main()
