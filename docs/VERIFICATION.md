# Website checks

## Commands

```bash
python3 tools/build.py
python3 tools/verify_links.py
npm install
npx playwright install chromium
npm test
```

## Coverage

- Eleven pages in English and Korean.
- Responsive layouts at 360, 390, 768, 1280 and 1440 CSS pixels.
- Navigation, language persistence, local links and image/video loading.
- Video playback, pause, enlargement and keyboard dismissal.
- Direct-file access, nested hosting paths and embedded layout.
- Numbered screenshot annotations and matching notes.

Generated reports and screenshots are stored in `docs/verification/`.
Browser coverage is Chromium; Safari, Firefox, physical mobile devices and
integration with a live host template require separate checks.
These checks cover the website, not simulator behavior or coaching efficacy.
