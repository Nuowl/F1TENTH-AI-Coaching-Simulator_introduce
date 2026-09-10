# Bilingual content review · 2026-09-11

## Scope and sources

Final pre-publication review (11 September 2026): reviewed all eleven EN/KO
pages, the paired READMEs, source register and publishing instructions. Checked
paper equations/study statistics against arXiv v1, Unity/platform claims against
AutoDRIVE primary sources, and control/session/replay claims against the current
simulator source/status. No simulator source or raw recordings were changed.

Corrections: map-only and right-panel video captions now match their recordings;
PP steering is distinguished from the accompanying speed planner; speed decline
alone is not labeled brake use; Figure 2 is included in the reference description;
the no-JavaScript notice no longer promises image enlargement. English wording,
Korean phrasing and matching paragraph breaks were tightened. Headings remain
English, with balanced wrapping and left-aligned body text in both languages.

Public upload excludes generated verification screenshots, caches, local
environments and unused spare media. Owner authorization for public release was
explicitly confirmed after the media/identifier review question. This is not a
claim of independent third-party license verification; credits remain intact.

Session illustration follow-up: added the supplied `dashboard_exp_02.png` beside
`dashboard_exp_01.png`, with paired EN/KO captions explaining the Stage selector.
The pair stacks below 701 CSS px. Original assets are unchanged. Subsequently,
presentation-only video crops were applied at the user's request; see
`VIDEO_CROPS.md`. No recorded data, source MP4 or research claim was changed.

Reviewed all 11 pages, including captions, signal definitions and future-work
claims. This is a website editorial review, not a fresh simulator acceptance test.
No simulator source, raw session or project planning file was changed.

- Owner-supplied `AI_Coaching.pdf`, arXiv:2606.25337v1, pp. 1–8:
  coaching motivation, VoI, L2C modules, per-axis blending, PPO, runtime gate-level
  skill inference, study design and statistical results.
- [AutoDRIVE ecosystem](https://autodrive-ecosystem.github.io/) and
  [original repository](https://github.com/Tinker-Twins/AutoDRIVE):
  Simulator, Devkit, Testbed, Unity and external algorithm connection.
- Separately maintained `ftenth_sim`: NOTES, STATUS, REQUIREMENTS, TRACEABILITY,
  AI Coaching SOURCE_INDEX, DATA_CONTRACT_EN, dashboard README and focused
  source checks for sampling frequency and session countdown settings.

## Content decisions

| Topic | Revised treatment |
| --- | --- |
| AI Coaching | Explain the learning objective before the algorithm; expert competence and coaching strategy are separate. |
| Skill model | Simulated skill transitions are model assumptions; runtime skill is estimated, not directly measured. |
| Study evidence | 33 participants, 11 per group; yaw/roll controlled by participants, pitch/thrust automated. |
| Statistics | 27.9%, 11.3%, 6.2% are paper-reported mean pre/post changes. Within-L2C significance does not establish significant superiority between groups; adjusted p=0.09–0.16 is stated. |
| Figure 2 | Individual trajectory examples are not group averages and are not F1TENTH results. |
| Platform attribution | AutoDRIVE supplies the simulation foundation; project additions are identified separately. |
| Current capabilities | PRE/EXPERT driving, session recording, dashboard/overlay and replay exist. No current learned coach, pedal recommendation or coaching-specific independent safety guard is claimed. |
| Data boundaries | 20 Hz means latest-value sampling; Applied is a command, not physical steering feedback; missing fields do not mean zero. |
| Validation | Historical provenance mismatches and incomplete participant-study validation remain explicit. |

## Language and readability

Korean uses natural explanatory sentences with technical names retained where
useful: AI Coaching, L2C, PPO, PP Expert and Replay Studio. Terms such as data
freshness and contract are explained as update status and collection format.
Long paragraphs are split at matching semantic boundaries in both languages.
Headings and navigation remain English. Word wrapping respects Korean word units;
paragraph width is bounded without shrinking images or videos.

## Added media

- `sim_basic_01.png`: supplied basic interface, visibly disconnected; caption
  identifies this state rather than implying live connectivity.
- `ai-coaching-figure2.png`: native PDF crop of Figure 2, page 2 at 200 dpi.
  Reproduce with `tools/extract_paper_figure.sh`; original marks and values retained.
- `map_pp_01.mp4`: original supplied PP map recording, not a generated animation.
- Current Progress now uses the existing Replay Studio MP4.

Attribution is provided; this review does not grant new redistribution rights to
third-party figures. The source PDF is not distributed in the website package.

## Verification

### Coaching-focused and program-guide revision

- Added paper-to-vehicle symbol definitions, blending, Bayesian observation update,
  condensed VoI notation and simulated skill reward. F1TENTH adaptations are
  explicitly proposed, not claimed as a running L2C policy.
- Questions now identify comparison conditions and confounds. Approach separates
  action conversion, reference construction, coaching, safety and unassisted testing.
- Restored AutoDRIVE identity artwork; added the full architecture diagram after
  the Unity explanation. The diagram does not imply every ecosystem tool is used.
- Simulator page owns side-panel operation, wheel/gamepad illustrations, manual
  and PP modes, configured limits and collision-rearm behavior.
- Dashboard/overlay guides use numbered linked notes over unchanged images.
  Asynchronous live updates are not presented as sensor-level synchronization.
- Replay uses replay_06 for session selection, replay_04 MP4 for graph modes,
  replay_03 MP4 for transport/alignment, and replay_01 MP4 for Current Progress.
- Current/Future pages retain the boundary between available reference/recording
  tools and pending coaching, pedal recommendations and safety producers.

Expanded content is maintained in `tools/research_details.py`, keeping reusable
page components separate from the primary page registry in `tools/content.py`.

Run `python3 tools/build.py`, `python3 tools/verify_links.py` and the Playwright
browser suite. Current machine-readable results and screenshots are under
`docs/verification/`. Check paragraph-language parity, fixed English headings,
responsive layouts and media decoding alongside playback controls.
