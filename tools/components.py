"""Small HTML components shared by the project and the portable design starter."""
from html import escape
from pathlib import Path
import json


_crop_file = Path(__file__).with_name('video_crops.json')
VIDEO_CROPS = json.loads(_crop_file.read_text()) if _crop_file.exists() else {}


def bi(en, ko):
    """Editorial strings may include reviewed HTML; headings never use this helper."""
    return f'<span lang="en" data-lang="en">{en}</span><span lang="ko" data-lang="ko" hidden>{ko}</span>'


def p(en, ko, cls=''):
    """Explicit paragraph breaks stay paired across languages."""
    english, korean = en.split('\n\n'), ko.split('\n\n')
    if len(english) != len(korean):
        raise ValueError('English and Korean paragraph counts must match')
    return ''.join(f'<p class="{cls}">{bi(e, k)}</p>' for e, k in zip(english, korean))


def h(title):
    return f'<h3 data-heading>{escape(title)}</h3>'


def cite(*numbers):
    return ''.join(f'<a class="citation" data-local href="references.html#ref-{n}" aria-label="Reference {n}">[{n}]</a>' for n in numbers)


def note(en, ko):
    return f'<aside class="note">{p(en, ko)}</aside>'


def cards(items):
    return '<div class="cards">' + ''.join(
        f'<section class="card"><span class="number">{i:02d}</span><h4 data-heading>{escape(title)}</h4>{p(en, ko)}</section>'
        for i, (title, en, ko) in enumerate(items, 1)) + '</div>'


def media(file, en, ko, gif=None, paper=False, compact=False):
    """Animations autoplay with playback toggle and enlarge; stills have no toolbar."""
    asset = 'assets/media/' + file
    alt_en = escape(en.split('<')[0], quote=True)
    alt_ko = escape(ko.split('<')[0], quote=True)
    controls = ''
    video = Path(gif).with_suffix('.mp4').name if gif else None
    if video and not (Path(__file__).resolve().parents[1] / 'assets/media' / video).is_file():
        if gif.endswith('.mp4'):
            raise FileNotFoundError(f'Missing required video: {video}')
        video = None
    if gif:
        icons = [('play', 'Play', '재생', '<path data-icon-play d="m8 5 11 7-11 7Z"/><rect data-icon-stop style="display:none" x="6" y="6" width="12" height="12" rx="1"/>'),
                 ('enlarge', 'Enlarge', '확대', '<path d="M9 4H4v5m11-5h5v5M4 15v5h5m11-5v5h-5"/>')]
        for action, eng, kor, icon in icons:
            data = f'data-play="assets/media/{gif}" aria-pressed="false"' if action == 'play' else f'data-{action}'
            controls += f'<button type="button" {data} aria-label="{eng}" data-label-en="{eng}" data-label-ko="{kor}"><svg viewBox="0 0 24 24" aria-hidden="true">{icon}</svg></button>'
        controls = f'<div class="media-tools">{controls}</div>'
    visual = f'<img src="{asset}" data-poster="{asset}" alt="{alt_en}" data-alt-en="{alt_en}" data-alt-ko="{alt_ko}" loading="lazy" decoding="async">'
    if video:
        visual = f'<video src="assets/media/{video}" poster="{asset}" autoplay muted loop playsinline preload="metadata" aria-label="{alt_en}" data-label-en="{alt_en}" data-label-ko="{alt_ko}"></video>'
    crop_class, crop_style = '', ''
    if video in VIDEO_CROPS:
        source_w, source_h, x, y, width, height = VIDEO_CROPS[video]
        if not (0 <= x < x + width <= source_w and 0 <= y < y + height <= source_h):
            raise ValueError(f'Invalid video crop: {video}')
        crop_class = 'media-cropped'
        crop_style = f'style="--crop-ratio:{width / height};--video-width:{100 * source_w / width}%;--video-left:{-100 * x / width}%;--video-top:{-100 * y / height}%"'
        visual = f'<div class="media-viewport">{visual}</div>'
    return f'''<figure class="{'figure-compact' if compact else ''}" {'data-demo' if gif else ''}>
      <div class="media-frame {'paper' if paper else ''} {crop_class}" {crop_style}>
        {visual}
        {controls}
      </div><figcaption>{bi(en, ko)}</figcaption></figure>'''


def table(headers, rows):
    return '<div class="table-wrap"><table><thead><tr>' + ''.join(f'<th scope="col">{escape(x)}</th>' for x in headers) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td>{x}</td>' for x in row) + '</tr>' for row in rows) + '</tbody></table></div>'


def steps():
    data = [
        ('PRE', 'Unassisted baseline', '초기 무보조 주행'),
        ('EXPERT', 'PP reference calibration', 'PP 기준 주행 보정'),
        ('COACHING', 'Adaptive assistance', '적응형 주행 보조'),
        ('PROBE', 'Independent practice check', '훈련 중 독립 주행 확인'),
        ('POST', 'Unassisted outcome', '훈련 후 무보조 평가'),
    ]
    return '<div class="steps">' + ''.join(f'<div class="step {"future" if i > 1 else ""}"><strong>{t}</strong>{p(e,k)}</div>' for i,(t,e,k) in enumerate(data)) + '</div>'
