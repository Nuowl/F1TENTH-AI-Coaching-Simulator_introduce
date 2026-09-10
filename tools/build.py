"""Generate portable static pages: python3 tools/build.py (no dependencies)."""
from pathlib import Path
from html import escape
from components import bi, p
from content import PROJECT, TAGLINE, GROUPS, PAGES, RESEARCH_AREA, UPDATED, PERIOD
from site_chrome import header

ROOT = Path(__file__).resolve().parents[1]


def build():
    entries = [entry for _, items in GROUPS for entry in items]
    for i, (key, label) in enumerate(entries):
        page = PAGES[key]
        nav = ''
        for group, links in GROUPS:
            nav += f'<div class="nav-group"><p class="nav-label">{escape(group)}</p>'
            for slug, name in links:
                active = ' aria-current="page"' if slug == key else ''
                nav += f'<a class="side-link" data-local href="{slug}.html"{active}>{escape(name)}</a>'
            nav += '</div>'
        previous = entries[i-1] if i else None
        following = entries[i+1] if i+1 < len(entries) else None
        pager = '<nav class="page-nav" aria-label="Adjacent pages">'
        pager += f'<a data-local href="{previous[0]}.html">← {escape(previous[1])}</a>' if previous else '<span></span>'
        pager += f'<a data-local href="{following[0]}.html">{escape(following[1])} →</a>' if following else '<a href="#top">↑ Back to top</a>'
        pager += '</nav>'
        html = f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(page['title'])} | {escape(PROJECT)}</title>
<meta name="description" content="{escape(page['lead'][0], quote=True)}">
<meta name="theme-color" content="#000000">
<meta name="color-scheme" content="dark">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/css/research.css">
<script defer src="assets/js/research.js"></script>
</head><body class="aix-research" id="top">
<a class="skip" href="#main-content">Skip to content</a>
{header()}
<div class="wrap">
<header class="hero"><p class="eyebrow">AiX Lab / {escape(RESEARCH_AREA)}</p><h1 data-heading>{escape(PROJECT)}</h1>{p(*TAGLINE, cls='tagline')}</header>
<div class="layout"><aside class="sidebar">
<button class="mobile-menu" aria-controls="project-navigation" aria-expanded="true">{bi('Project menu', '프로젝트 메뉴')}<span aria-hidden="true">☰</span></button>
<nav class="js-nav open" id="project-navigation" aria-label="Project sections">{nav}</nav>
<div class="sidebar-note">Research development<br>Updated · {escape(UPDATED)}</div>
</aside>
<main class="article" id="main-content" tabindex="-1">
<div class="language-bar" role="group" aria-label="Content language"><button data-language="ko" aria-pressed="false" lang="ko">한국어</button><button data-language="en" aria-pressed="true" lang="en">English</button><span class="article-index">{i+1:02d} / {len(entries):02d}</span></div>
<noscript><p>This page is available in English. Enable JavaScript for Korean and the video playback and enlargement controls.</p></noscript>
<h2 class="page-title" data-heading>{escape(page['title'])}</h2>
{p(*page['lead'], cls='lead')}
{page['body']}
{pager}
</main></div></div>
<footer class="footer"><div class="wrap footer-inner"><span>AiX Lab · Gyeongsang National University</span><span>{bi('Research in progress · ' + PERIOD[0], '연구 진행 중 · ' + PERIOD[1])} · <a data-local href="references.html">References &amp; Credits</a></span></div></footer>
<dialog aria-label="Expanded animation"><button type="button" data-label-en="Close" data-label-ko="닫기" aria-label="Close">×</button><img alt=""></dialog>
</body></html>'''
        html = '\n'.join(line.rstrip() for line in html.splitlines()) + '\n'
        (ROOT / f'{key}.html').write_text(html, encoding='utf-8')
        print(f'Built {key}.html')


if __name__ == '__main__':
    build()
