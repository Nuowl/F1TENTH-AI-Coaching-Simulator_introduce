#!/usr/bin/env bash
# Usage: bash tools/extract_paper_figure.sh /path/to/AI_Coaching.pdf
# Native PDF rendering only: Figure 2, page 2, 200 dpi; no scene retouching.
set -euo pipefail
site_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
pdftoppm -f 2 -l 2 -r 200 -x 290 -y 190 -W 1125 -H 610 \
  -singlefile -png "${1:?Supply the AI Coaching v1 PDF}" \
  "$site_root/assets/media/ai-coaching-figure2"
