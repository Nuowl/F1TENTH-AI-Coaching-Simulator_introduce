"""Copy matching original videos without re-encoding; record provenance hashes.

Usage: python3 tools/import_videos.py /path/to/video
GIF counterparts and explicitly selected program-guide recordings are imported.
"""
import hashlib
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    source = Path(sys.argv[1]).resolve()
    records = []
    names = {gif.with_suffix('.mp4').name for gif in (ROOT / 'assets/media').glob('*.gif')}
    names.update(['replay_01.mp4', 'replay_03.mp4', 'replay_04.mp4', 'sim_01.mp4', 'sim_02.mp4'])
    for name in sorted(names):
        video = source / name
        if not video.is_file():
            raise FileNotFoundError(video)
        target = ROOT / 'assets/media' / name
        shutil.copy2(video, target)
        records.append(dict(file=target.name, source_file=video.name,
                            sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
                            bytes=target.stat().st_size, operation='Original MP4; no re-encoding'))
    (ROOT / 'docs/video-manifest.json').write_text(json.dumps(records, indent=2) + '\n')
    print(f'Imported {len(records)} original videos without re-encoding.')


if __name__ == '__main__':
    main()
