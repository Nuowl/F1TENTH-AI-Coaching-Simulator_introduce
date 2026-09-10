"""Check local destinations, fragment targets, duplicate IDs and packaged assets."""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids = set()
        self.links = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f'Duplicate ID {attrs["id"]}'
            self.ids.add(attrs['id'])
        for key in ['href', 'src', 'poster', 'data-play', 'data-poster']:
            if key in attrs:
                self.links.append(attrs[key])


def check(root):
    pages = {p: Page(p.read_text(encoding='utf-8')) for p in root.glob('*.html')}
    count = 0
    for path, page in pages.items():
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path.resolve()
            assert target.is_file(), (path.name, link)
            if url.fragment and target.suffix == '.html':
                assert url.fragment in pages[target].ids, (path.name, link)
            count += 1
    print(f'{root.name}: {len(pages)} pages, {count} local links/assets/fragments passed.')
    return dict(pages=len(pages), links=count, status='pass')


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    result = check(root)
    (root / 'docs/verification').mkdir(parents=True, exist_ok=True)
    (root / 'docs/verification/links.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    starter = root.parent / 'aix-research-design-kit/starter'
    if starter.is_dir():
        check(starter)
