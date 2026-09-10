# Implementation evidence register

Reviewed 2026-09-11. This is an editorial snapshot of unpublished engineering work,
not an experimental publication. Paths below identify the separately maintained
`ftenth_sim` source project; no local runtime or raw session is needed by this site.

| Website claim | Source inspected | Interpretation |
| --- | --- | --- |
| Project goal and current boundaries | NOTES.md; plans/STATUS.md; plans/REQUIREMENTS.md; plans/TRACEABILITY.md | Current implementation vs planned learning research |
| Paper interpretation | User-supplied AI_Coaching.pdf, pp. 1–8; public arXiv v1 | L2C, VoI, per-axis blending, PPO, inferred skill and drone study; distinguish within-group from between-group statistics |
| 20 Hz default | src/telemetry/ros2_experiment_node.py, default --sample-rate=20.0; DATA_CONTRACT_EN.md | Latest-value collection, not synchronized sensors |
| Human / PP / Applied | src/telemetry/schema.py; DATA_CONTRACT_EN.md | Applied is a final command, not a measured wheel angle |
| Countdown range and default | src/dashboard/session_controls.py, countdown_spin range 1–120, default 15 | Current UI configuration |
| Countdown and PRE/EXPERT live checks | plans/STATUS.md, 2026-09-09 live verification entries | Engineering validation, not completed five-stage human study |
| Replay modes and navigation | src/dashboard/README.md, current Replay Studio section | Same-stage comparisons; A/B chosen by user; graph time axes explained |
| Later recording endpoint | src/dashboard/replay_timeline.py, duration=max(ends) | Ended recordings retain last observed pose |
| Data gaps and nullable coaching | configs/ai-coaching/DATA_CONTRACT_EN.md; schema.py | Policy/guard producers pending, optional IMU; missing is not zero |
| PP range, validation boundaries | NOTES.md; plans/STATUS.md; configs/ai-coaching/SOURCE_INDEX.md | Configured 1–3 m/s reference; no universal collision-free or optimality claim |
| Steering limit | configs/autonomy/pp_shadow_2026_icra.json; autodrive_pp_baseline_2026_icra.json; src/autonomy/pp_core.py; Unity VehicleController.cs | Normalized ±1 corresponds to a configured ±30° vehicle steering range, not wheel-controller rotation |
| Wheel speed control | src/manual_control/control_core.py, MozaTargetSpeedController | 1 m/s cruise, accelerator up to 3 m/s, brake toward zero; wheel profile specifically |
| Collision recovery | src/manual_control/ubuntu_ros2_bridge.py, collision latch and release/rearm paths | Hold zero throttle/steering; release selection then choose exactly one mode; not automatic vehicle reset |
| Dashboard buttons | src/dashboard/desktop_dashboard.py, stop/profile handlers; overlay_dashboard.py opacity/map/window controls | UI and control-profile status are distinct from session-supervisor connectivity |
| Future maps, pedal recommendations, visual path | Owner's instructions dated 2026-09-11 | Research plan, not implemented functionality |

## Reconciliation decisions

Older protocol prose and trailing README sections still describe comparative replay
and five-stage orchestration as future work. The newer STATUS entries and leading
Replay Studio documentation take precedence for the website snapshot. This site
does not silently repair or modify those source documents.

Recent PRE/EXPERT live validation coexists with two historical frozen-baseline
provenance failures. The website does not describe the entire system as fully
validated. No test counts were rerun or newly claimed by this website work.

Do not infer learning gains, steering-feedback hardware capability, complete IMU
coverage, a pedal recommendation policy, or an active adaptive guard from screenshots.
Screenshots include illustrative counters and connectivity states; captions identify
these limits. Demonstration videos and screenshots contain individual lap values
and session identifiers; they are not aggregate study results. Publication of
screen-visible identifiers requires the owner's review.

## Public primary sources

- Wang et al., AI Coaching, arXiv:2606.25337v1: https://arxiv.org/abs/2606.25337v1
- AutoDRIVE ecosystem: https://autodrive-ecosystem.github.io/
- AutoDRIVE source: https://github.com/Tinker-Twins/AutoDRIVE
- Coulter, Pure Pursuit, CMU-RI-TR-92-01 (1992): https://www.ri.cmu.edu/publications/implementation-of-the-pure-pursuit-path-tracking-algorithm/

Re-review this snapshot whenever runtime capabilities or research results change.

The bilingual editorial re-review is recorded in [CONTENT_REVIEW.md](CONTENT_REVIEW.md).
