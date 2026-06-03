"""Auto-generate mkdocs.yml from directory structure"""
import os, yaml

def scan(path, base=''):
    items = []
    for e in sorted(os.listdir(path)):
        f = os.path.join(path, e)
        r = os.path.join(base, e) if base else e
        if os.path.isdir(f):
            c = scan(f, r)
            if c:
                items.append({e: c})
        elif e.endswith('.md') and e != 'index.md':
            items.append({e[:-3]: r})
    return items

cfg = {
    'site_name': '自动化知识笔记',
    'site_url': 'https://huarenjian1.github.io/',
    'theme': {
        'name': 'material',
        'language': 'zh',
        'features': ['navigation.instant', 'navigation.top', 'search.suggest', 'search.highlight'],
        'palette': [{'scheme': 'default', 'primary': 'indigo', 'accent': 'indigo'}]
    },
    'extra_css': ['stylesheets/extra.css'],
    'markdown_extensions': ['pymdownx.arithmatex', 'pymdownx.superfences'],
    'extra_javascript': [
        'javascripts/mathjax.js',
        'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'
    ],
    'nav': [{'首页': 'index.md'}] + scan('docs')
}

with open('mkdocs.yml', 'w', encoding='utf-8') as f:
    yaml.dump(cfg, f, allow_unicode=True, sort_keys=False)

print('mkdocs.yml generated')
