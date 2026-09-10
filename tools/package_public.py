"""Prepare a local GitHub-upload candidate; never create a repo or upload files.

Usage: python3 tools/package_public.py /path/to/output.zip
Exclusions follow .gitignore via Git's read-only no-index matcher.
"""
import argparse
import re
import subprocess
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {'.py', '.cjs', '.js', '.json', '.html', '.css', '.svg', '.md', '.sh'}
SECRETS = re.compile(
    r'(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{50,}|'
    r'sk-(?:proj-)?[A-Za-z0-9_-]{32,}|AKIA[A-Z0-9]{16}|'
    r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)'
)


def ignored(relative):
    # -c core.excludesFile avoids depending on a user's global Git ignore list.
    # git check-ignore needs a repository, so use a separate temporary index-free
    # work tree only for matching; no Git files are written into the website.
    import tempfile
    with tempfile.TemporaryDirectory(prefix='research-ignore-') as scratch:
        subprocess.run(['git', 'init', '--quiet', scratch], check=True)
        result = subprocess.run(
            ['git', '-c', 'core.excludesFile=/dev/null', '--git-dir=' + scratch + '/.git',
             '--work-tree=' + str(ROOT), 'check-ignore', '--no-index', '-z', '--stdin'],
            input='\0'.join(relative) + '\0', text=True, capture_output=True, cwd=ROOT)
        if result.returncode not in (0, 1):
            raise RuntimeError(result.stderr)
        return set(result.stdout.rstrip('\0').split('\0')) if result.stdout else set()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    if output == ROOT or ROOT in output.parents:
        parser.error('Write the candidate ZIP outside the website directory.')
    files = sorted(p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.relative_to(ROOT).parts)
    excluded = ignored([p.relative_to(ROOT).as_posix() for p in files])
    files = [p for p in files if p.relative_to(ROOT).as_posix() not in excluded]
    for file in files:
        if file.is_symlink():
            raise ValueError(f'Symlink requires manual review: {file.relative_to(ROOT)}')
        if file.stat().st_size >= 100 * 1024 * 1024:
            raise ValueError(f'File exceeds ordinary GitHub limit: {file.relative_to(ROOT)}')
        if file.suffix in TEXT_SUFFIXES:
            text = file.read_text(encoding='utf-8')
            if SECRETS.search(text):
                raise ValueError(f'Potential credential; inspect locally: {file.relative_to(ROOT)}')
            if re.search(r'/(?:home|Users)/[^/\s]+/', text):
                raise ValueError(f'Personal filesystem path: {file.relative_to(ROOT)}')
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, 'w', ZIP_DEFLATED) as archive:
        for file in files:
            archive.write(file, file.relative_to(ROOT))
    with ZipFile(output) as archive:
        assert archive.testzip() is None
    largest = max(files, key=lambda p: p.stat().st_size)
    print(f'Candidate: {output.name}; {len(files)} files; {output.stat().st_size / 1024**2:.2f} MiB')
    print(f'Largest: {largest.relative_to(ROOT)} ({largest.stat().st_size / 1024**2:.2f} MiB)')
    print('ZIP integrity, text credential patterns and personal-path scan passed.')
    print('Not uploaded. Media permissions and visible identifiers require owner review.')


if __name__ == '__main__':
    main()
