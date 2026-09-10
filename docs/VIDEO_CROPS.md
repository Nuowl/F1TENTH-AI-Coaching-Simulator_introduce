# Presentation-only video crops

Original MP4s are unchanged. `tools/video_crops.json` stores
`[source width, source height, x, y, visible width, visible height]` in pixels.
The builder wraps only configured videos in an overflow-clipped viewport.
The same viewport moves into the enlargement dialog; playback is not restarted.
Buttons sit in a 48 CSS px rail immediately below the cropped picture to avoid
covering recorded controls or values. Portrait views retain a height limit.

Bounds were inspected across all 12 recordings at 0.25-second intervals, using
RGB > 8 to distinguish picture from near-black compression noise. Every crop
keeps 16 source pixels beyond the detected content boundary. Sampling is not an
exhaustive every-frame proof; no automatic cropping happens during playback.
The crop is fixed throughout each recording, with no reframing or stretching.

To recheck supplied recordings using an existing browser installation:

```bash
PLAYWRIGHT_MODULE=/path/to/playwright CHROMIUM_PATH=/path/to/chromium \
  node tools/inspect_video_borders.cjs
```

Review bounds again when replacing a video. Remove its entry to show the full
original frame. The shared component also works without this configuration file.
