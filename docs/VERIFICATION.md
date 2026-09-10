# Website verification · 2026-09-11

## Results

Final public-release check: all 22 page/language combinations passed again across
five viewport widths; source Python compilation and JavaScript syntax checks
passed. The isolated extracted public ZIP rebuilt all 11 pages and passed 394
local links/assets/fragments, now including video posters. Fixed the link checker
to create its report directory so it also works in a clean checkout.
The upload candidate passed ZIP CRC, text credential-pattern and personal-path
checks. These automated text checks do not inspect every pixel or independently
establish media rights. The owner confirmed public release after that review.

Video crop follow-up: rebuilt 11 pages; 377 local references passed. Full Chromium
suite passed again (22 page/language combinations). `tools/verify_video_crops.cjs`
passed at 390/1440 px for the narrow driving panel, simulator sidebar and replay
controls: buttons below content, no overflow, pause preserved on enlargement,
resume after closing. Three focused screenshots were visually reviewed.
See `VIDEO_CROPS.md` for the sampled border inspection and its limits.

Session image follow-up: focused Chromium checks passed for EN/KO at
390/768/1440 CSS px (two decoded images, stacked/side-by-side placement, no
horizontal overflow). Rebuild passed; 377 site links/assets/fragments passed.
This focused check does not replace the broader results below.

- 11 actual HTML pages × EN/KO = 22 combinations: passed.
- Each combination at 360, 390, 768, 1280, 1440 CSS px: no document-level horizontal overflow.
- English headings identical before/after language switch; hidden language absent from layout.
- One current sidebar destination; language persists across pages; browser Back works.
- Local assets, page links and reference fragments checked; current counts in verification/links.json.
- Revision 1.1: GIF autoplay, two transparent icon-only controls (Play/Stop toggle and Enlarge) and no static-image toolbars passed.
- Original MP4 decoding, muted looping, Play/Stop state, enlarged playback controls and Escape dismissal passed. Paused state survives returning from enlargement.
- Banner-disabled generation preserves all 11 content pages; reciprocal EN/KO README links passed.
- Mobile collapsed menu and expand/collapse passed.
- Nested URL prefix, embed=1 propagation and direct file:// navigation passed.
- English navigation/content remains readable with JavaScript disabled.
- Overview at 200% CSS zoom: no document-level horizontal overflow.
- Browser console exceptions and local HTTP errors: zero.
- Every raster image in page verification decoded successfully, including below-fold lazy media.
- Captured both languages; reviewed all English page compositions and selected Korean
  overview, background, approach, dashboard and mobile layouts. Small panels use
  compact figure widths and animations keep a stable display aspect ratio.
- Independent design starter: 7 pages; local links/assets/fragments and direct-file
  rendering, Korean switch and 390px layout passed without the F1TENTH site.
- Both delivery ZIPs pass archive CRC/integrity checks.

## Reproduce

```bash
python3 tools/build.py
python3 tools/verify_links.py
npm install
npx playwright install chromium
npm test
```

`verify_links.py` also checks the sibling delivery kit when both packages are
present. Browser verification used the pre-existing Playwright 1.57.0 module
and Chromium 143 installed in an isolated temporary browser directory. No
application runtime dependency was installed in the simulator project.

Machine-readable results: `verification/results.json`, `verification/links.json`.
Screen captures are stored under `verification/`.

## Evidence and limitations

Source paper checked against the supplied PDF and arXiv v1. Platform claims
checked against the official AutoDRIVE site/repository. Pure Pursuit reference
checked against CMU's publication record. Original AiX research page captured
in the separate design kit with source URL and measured layout values.

This verifies the static research website, not a fresh run of simulator tests,
a completed human study, accessibility certification, or deployment inside the
lab's actual server template. Browser coverage is Chromium; Safari/Firefox and
real mobile hardware were not separately exercised. The screen recordings retain
the original supplied resolution. No GitHub publication or lab server change occurred.

Initial media quality audit: all six retained GIFs are byte-identical to the supplied
sources (SHA-256 comparison). Simulator recordings are 412×232 and 414×232;
dashboard 584×328; overlay 638×358; replay 636×358; panel 640×360.
The subsequently supplied matching MP4s are now copied into assets/media without
re-encoding and preferred by the builder. All twelve decoded in Chromium with source
widths at least 1000 pixels. Their hashes are recorded in video-manifest.json.
Display dimensions were not reduced; the temporary source directory is not a
runtime dependency. Original source files and unused recordings remain unchanged.

All new files are under the independent research_websites directory. The source
simulator project and source screenshot/PDF assets were read, not modified.

The subsequent bilingual content review is documented in CONTENT_REVIEW.md.
The expanded background, native Figure 2 crop and basic AutoDRIVE screenshot
were included in the 22-page/language regression and responsive layout checks.
The program-guide revision also checks 11 numbered screenshot anchors and their
note/back-link navigation. Desktop diagram/callout and mobile note/device views
were captured and visually inspected. All twelve packaged MP4s decoded successfully.
