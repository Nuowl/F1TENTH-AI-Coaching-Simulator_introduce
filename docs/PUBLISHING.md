# Publishing and lab integration

## Standalone GitHub repository

Requested destination: `Nuowl/F1TENTH-AI-Coaching-Simulator_introduce`, public.
Only this website directory is in scope. The simulator repository must remain
unchanged, including its visibility. A repository upload and GitHub Pages
activation are separate actions; neither is performed by the packaging tools.

Use `tools/package_public.py` for an upload candidate that honors `.gitignore`.
Local verification screenshots, caches and spare `racing_wheel.png` are excluded
without deleting them. The candidate is self-contained; no simulator checkout,
design kit, source-video folder or raw experiment sessions are needed.

Upload the contents of this directory, keeping `index.html` at repository root.
Use a new repository; no link to the simulator's Git history is needed. To use
GitHub Pages, publish the root from the chosen branch in repository settings.
All internal URLs are relative and support `/repository-name/` hosting. Configure
the repository visibility and publication settings when actually publishing.

The build and packaging commands do not create repositories or upload files.
There is no assumed public simulator-source link because its repository is private.

## Within AiX Lab

Copy the site's HTML and `assets/` to a dedicated directory, for example
`/research/ai-driving-coaching/`, and link to its `index.html` from the lab menu.
Retain `docs/` if using the evidence/credits links. This version supplies a small
lab masthead; its links navigate to the existing lab site.

Banner HTML and its `SHOW_LAB_HEADER` flag live in `tools/site_chrome.py`.
Set the flag to `False` and run `python3 tools/build.py` to remove the banner
from all generated pages, without editing each page or affecting article controls.
This is separate from the runtime `?embed=1` preview option below.

For integration into an existing layout that already supplies a masthead/footer,
use `?embed=1`. It hides this site's duplicate masthead/footer and uses the host
container's width. For server-template inclusion, wrap the generated project
content in `.aix-research.embedded` and include the shared CSS/JS once. Do not nest
an entire HTML document inside the host page. Relative asset paths must resolve
from the destination document. Test the actual host template before deployment.

CSS is scoped beneath `.aix-research`, but aggressive host rules with `!important`
can still override it. The standalone subdirectory is the verified integration path;
the live lab's server/template access has not been provided or modified.

## Final publication checks

On 11 September 2026, after the media-rights and screen-visible identifier
review question, the owner explicitly confirmed public release and instructed
upload. This records the owner's authorization, not an independently obtained
license from every third-party rights holder. Attribution is retained.

The source paper lists the arXiv non-exclusive distribution license, not a
Creative Commons reuse license. A citation alone does not establish permission.
For future replacements, confirm the reuse basis for paper figures, product
photos and lab artwork, and review visible session IDs, timestamps and per-run
values before publishing them. If uncertain, use a source link instead.

- [Paper license label](https://arxiv.org/abs/2606.25337v1)
- [arXiv license guidance](https://info.arxiv.org/help/license/index.html)
- [GitHub large-file guidance](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)

No project-wide license is added automatically. `private: true` in `package.json`
prevents accidental npm publication; it does not make the GitHub repository private.

Review translated content and screen-visible identifiers as publication material.
Preserve the source credits for the paper figure, AutoDRIVE images and lab logo.
Review the media owner's applicable redistribution terms before applying a blanket
repository license. Replace dated status copy when the research progresses.

The site needs no cookies, analytics, remote fonts or API keys. If adding an absolute
canonical URL or social-preview URL, use the final hosting address rather than a
placeholder domain. No public URL is fabricated in the current build.
