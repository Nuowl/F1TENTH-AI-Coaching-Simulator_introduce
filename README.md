# AI Driving Coaching for F1TENTH — Research Website

**English** | [한국어](README_KO.md)

Standalone AiX Lab research introduction, English by default with Korean body text.
Project and section headings remain English in either language. This directory is
independent of the simulator repository and can be uploaded as its own repository.

## Preview

Open `index.html` directly, or run from this directory:

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

Visit http://127.0.0.1:8080/ . No installation, build service or runtime framework.
The checked-in HTML is ready to serve. With JavaScript disabled, English content
and ordinary page navigation remain available.

## Structure and editing

- `*.html`: eleven generated pages with stable, independent URLs.
- `assets/css/research.css`: scoped layout, visual tokens and responsive rules.
- `assets/js/research.js`: language, mobile navigation, demo playback and figure viewer.
- `assets/media/`: supplied illustrations, recordings and fallback media.
- `tools/content.py`: reviewed EN/KO copy and page structure.
- `tools/research_details.py`: coaching equations, application guides and numbered screenshot notes.
- `tools/components.py`: small editorial components, without framework dependencies.
- `tools/build.py`: shared page shell and static generator.
- `tools/site_chrome.py`: optional lab banner; set `SHOW_LAB_HEADER = False` and rebuild to omit it.
- `docs/`: plan, evidence, asset attribution, verification and publishing guidance.

To edit content, change `tools/content.py` or `tools/research_details.py`, then run `python3 tools/build.py`.
Headings are English-only strings. Body copy uses `bi(en, ko)` or `p(en, ko)`.
`?lang=ko` creates a Korean deep link; the selected language persists across pages.
See [publishing](docs/PUBLISHING.md) and [evidence](docs/EVIDENCE.md).

## Media behavior

Fixed presentation crops remove inspected black borders without modifying MP4s.
See [crop settings and verification limits](docs/VIDEO_CROPS.md). Controls remain
below cropped pictures so they do not obscure narrow data panels.

Original MP4 recordings autoplay silently and loop. Two transparent icon buttons
provide a Play/Stop toggle and Enlarge. Stop pauses at the current frame; Play
resumes there. Enlargement keeps the same player and playback position.
Hidden tabs suspend playback and resume previously playing demos on return.
Static figures have no toolbar or enlargement button. Figure captions and source
credits remain visible. No media CDN is required.
Recordings live in `assets/media/` and need no external source folder. The builder
prefers an MP4 with the same stem as the GIF; GIF/poster fallback is retained.
`tools/import_videos.py SOURCE_FOLDER` imports originals without re-encoding and
records hashes in `docs/video-manifest.json`; run `python3 tools/build.py` afterwards.

## GitHub upload

Upload only the contents of `f1tenth-ai-coaching` as the new repository root,
including `index.html`, the other HTML pages, `assets/`, `tools/`, `docs/` and
both README files. Honor `.gitignore`: generated verification screenshots,
caches, local environments and unused spare media are excluded. The simulator
project and separate design kit are not included.
English README is the default; the links at the top switch between languages.

To prepare a checked local upload candidate without publishing anything:

```bash
python3 tools/build.py
python3 tools/verify_links.py
python3 tools/package_public.py ../downloads/f1tenth-ai-coaching-public.zip
```

The ZIP contains repository-root files, not an extra enclosing folder. Review
[publication checks](docs/PUBLISHING.md) before making it public. A public
repository does not change third-party media rights. No blanket license has
been assigned to the website or its third-party media.

The lab banner is isolated in `tools/site_chrome.py`. It can be changed there or
removed at build time using its flag; project titles, navigation and article
content do not depend on it. `?embed=1` remains available for previewing integration.

## Reusable design

The separate `aix-research-design-kit` delivery contains the visual specification,
reference renders, a working generic starter and a Codex reuse prompt. This site
does not depend on that folder at runtime.

`tools/package_delivery.py` is a workspace assembly utility for both deliveries;
run it only when the sibling design-kit folder is present. Normal content builds,
local-link checks and website preview work with this repository alone.

Website date: 2026-09-11. Learning gains and adaptive pedal/coaching control are
research goals, not claims of completed implementation. See References on the site.
