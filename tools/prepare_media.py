"""One-time import of supplied assets, preserving originals and recording hashes.

Usage: python3 tools/prepare_media.py /path/to/supplied/HTML
Requires Pillow only for deriving an animation poster. Normal site builds do not.
"""
import hashlib
import json
import shutil
import sys
from pathlib import Path

from PIL import Image

FILES = [
    'aix_lab_logo.png', 'coaching_01.png', 'AutoDRIVE_01.png',
    'sim_pp_01.png', 'sim_pp_01.gif', 'sim_pre_01.png', 'sim_pre_01.gif',
    'dashboard_pre_01.png', 'dashboard_pre_01.gif', 'dashboard_exp_01.png', 'dashboard_exp_02.png',
    'overlay_pre_01.png', 'overlay_pre_01.gif', 'panel_pre_01.gif',
    'replay_01.png', 'replay_02.png', 'replay_02.gif', 'replay_04.png', 'map_pp.png',
    'sim_basic_01.png', 'map_pp_01.gif',
    'replay_06.png', 'replay_03.png', 'sim_01.png', 'sim_02.png',
    'moza_r5.jpg', 'F710.jpg', 'AutoDRIVE Overview - Dark.png',
]


def main():
    source = Path(sys.argv[1]).resolve()
    root = Path(__file__).resolve().parents[1]
    dest = root / 'assets' / 'media'
    dest.mkdir(parents=True, exist_ok=True)
    records = []
    for name in FILES:
        original = source / name
        shutil.copy2(original, dest / name)
        records.append(dict(file=name, source_file=name, sha256=hashlib.sha256(original.read_bytes()).hexdigest(), bytes=original.stat().st_size))
    with Image.open(source / 'panel_pre_01.gif') as image:
        image.seek(0)
        image.convert('RGB').save(dest / 'panel_pre_01-poster.png')
    records.append(dict(file='panel_pre_01-poster.png', source_file='panel_pre_01.gif', operation='Frame 0 poster; no content retouching'))
    figure = dest / 'ai-coaching-figure2.png'
    if figure.is_file():
        records.append(dict(file=figure.name, source_file='AI_Coaching.pdf',
                            sha256=hashlib.sha256(figure.read_bytes()).hexdigest(),
                            operation='Figure 2, page 2, 200 dpi; native crop x=290 y=190 width=1125 height=610'))
    (root / 'docs' / 'media-manifest.json').write_text(json.dumps(records, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'Imported {len(FILES)} supplied files and one poster; originals unchanged.')


if __name__ == '__main__':
    main()
