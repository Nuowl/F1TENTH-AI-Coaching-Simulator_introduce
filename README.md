# AI Driving Coaching for F1TENTH

**English** | [한국어](README_KO.md)

A bilingual research website introducing an AutoDRIVE-based F1TENTH driving
coaching environment. It covers the research background, goals and approach,
along with the simulator, dashboard, overlay, Replay Studio and future work.

English is the default language. Descriptions and captions can be switched to
Korean; project and section headings remain in English.

## Preview

Open `index.html` in a browser. Alternatively, run a local server:

```bash
python3 -m http.server 8080 --bind 127.0.0.1
```

Then visit http://127.0.0.1:8080/ . The site uses static HTML, CSS and JavaScript;
no application framework or simulator installation is required.

## Structure

- `*.html`: eleven pages covering the research and its software environment.
- `assets/css/`: layout, typography and responsive styles.
- `assets/js/`: language switching, navigation and video controls.
- `assets/media/`: research figures, screenshots and demonstration videos.
- `tools/content.py`, `tools/research_details.py`: English and Korean page content.
- `tools/components.py`, `tools/build.py`: shared components and HTML generation.
- `tools/site_chrome.py`: the lab banner.
- `docs/`: source references and technical notes.

## Editing

Edit the content files, then regenerate the pages:

```bash
python3 tools/build.py
```

Edit `assets/css/research.css` to adjust the design. Use `?lang=ko` to open a page
in Korean. Images and videos are stored locally in `assets/media/`.

## References

See [References & Credits](references.html) for the AI Coaching paper, AutoDRIVE,
Pure Pursuit and [media attribution](docs/ASSET_CREDITS.md).
