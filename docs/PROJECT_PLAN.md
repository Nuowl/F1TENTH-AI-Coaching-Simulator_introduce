# Research website plan

Status: implementation, browser verification and standalone packaging complete · 2026-09-11

## Deliverables

1. Independent static, bilingual research website, ready for a separate GitHub repository.
2. Independent AiX research design kit with specification, editable reference diagrams,
   screenshots, working starter, content contract and a Codex reuse prompt.
3. Separate ZIP archives and a local browser preview. Publication is a later action.

## Information architecture

Research: Overview → Background → Research Questions → Research Approach.
Environment: Simulator → Dashboard & Overlay → Replay Studio → Data Collection.
Outlook: Current Progress → Future Work → References.

Each destination is an actual HTML file with a stable URL, shared sidebar and
language switch. English is the default. Project titles, section headings and
navigation remain English in both modes. Body copy, captions, controls and
alternative text switch to Korean. A deep link carries the chosen language.

## Evidence and boundaries

- AI Coaching: user-supplied PDF, public arXiv v1 and authors' attribution.
- AutoDRIVE: official ecosystem site and Tinker-Twins repository.
- Current implementation: 2026-09-11 source snapshot of ftenth_sim, including
  STATUS, SOURCE_INDEX, DATA_CONTRACT, dashboard README and relevant code.
- Newer source/status overrides outdated future-tense paragraphs in older docs.
- Completed UI and data infrastructure do not demonstrate human learning gains.
- PP provides speed/steering references; pedal recommendations are future work.
- No raw participant recordings, unpublished manuscripts or simulator binaries
  are redistributed. Supplied screenshots illustrate interfaces, not study results.

## Visual contract

Follow the supplied Formal Methods research page: black canvas, large project
title and summary above a left sidebar/right article layout, blue active links,
language tabs above the article, English headings, clear horizontal dividers.
Use a restrained extension for figures, study-stage diagrams and component cards.
Use a black logo background, preserving orange artwork and displaying lettering in white via CSS.

## Acceptance

- All eleven pages contain meaningful EN/KO content, nearby citations and media captions.
- Navigation, persisted language, browser Back, media play/stop, enlarge/close and
  keyboard use work with relative paths, including a nested hosting prefix.
- No clipping at 360, 390, 768, 1280 and 1440 CSS pixels; 200% text zoom review.
- GIFs autoplay with transparent lower-left play/stop/enlarge icons; static images have no toolbar.
- Original MP4s take priority over GIF fallbacks; playback controls retain position during enlargement.
- Korean uses natural explanatory prose; English and Korean paragraphs break at corresponding meanings.
- Background explains the source paper and platform before connecting them to the project; source results and project progress stay separate.
- Site runs directly from index.html or any static HTTP server; no runtime dependencies.
- Design kit can be copied and built without ftenth_sim or this site.

## Implementation order

Evidence review → design contract → content and media → static page generation →
browser checks and visual review → standalone template and ZIP packaging.

## Delivery state

All eleven pages generated. Browser verification passed for 22 page/language
combinations across five widths. Internal local links/assets/fragments passed;
independent seven-page starter also passed direct-file/mobile/Korean checks.
Two ZIP packages are built separately. See VERIFICATION.md for limits and commands.
Public GitHub upload is owner-authorized for the standalone website repository.
Live lab deployment and GitHub Pages activation are separate, out-of-scope actions.

The bilingual content revision expands AI Coaching/L2C and AutoDRIVE, adds the
source paper's Figure 2, the basic simulator screenshot and a PP map recording.
See CONTENT_REVIEW.md for the source cross-check and editorial decisions.

The detailed program-guide revision adds coaching notation and its F1TENTH
interpretation, experiment comparisons, action-space/safety design, AutoDRIVE
architecture and Unity context, wheel/gamepad operation, verified vehicle limits,
linked dashboard/overlay callouts and the requested replay videos. Twelve original
MP4s are now packaged locally. The source simulator and raw recordings remain unchanged.
