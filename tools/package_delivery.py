"""Assemble the independent starter and two reproducible delivery ZIPs."""
import shutil
import subprocess
import sys
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

SITE = Path(__file__).resolve().parents[1]
KIT = SITE.parent / 'aix-research-design-kit'


def copy(source, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def main():
    for name in ['assets/css/research.css', 'assets/js/research.js', 'assets/favicon.svg',
                 'assets/media/aix_lab_logo.png', 'tools/build.py', 'tools/components.py', 'tools/site_chrome.py', '.gitignore', '.nojekyll']:
        copy(SITE / name, KIT / 'starter' / name)
    subprocess.run([sys.executable, str(KIT / 'starter/tools/build.py')], check=True)
    for source, dest in [('index-en.png', 'implemented-desktop.png'), ('mobile-ko.png', 'implemented-mobile.png')]:
        copy(SITE / 'docs/verification' / source, KIT / 'references' / dest)
    destdir = SITE.parent / 'downloads'
    destdir.mkdir(exist_ok=True)
    for folder in [SITE, KIT]:
        target = destdir / f'{folder.name}.zip'
        with ZipFile(target, 'w', ZIP_DEFLATED) as out:
            for p in sorted(folder.rglob('*')):
                if not p.is_file() or any(x in p.parts for x in ['__pycache__', '.git', 'node_modules']):
                    continue
                out.write(p, Path(folder.name) / p.relative_to(folder))
        with ZipFile(target) as check:
            assert check.testzip() is None
        print(f'{target.name}: {target.stat().st_size / 1024 / 1024:.2f} MiB, ZIP integrity passed')


if __name__ == '__main__':
    main()
