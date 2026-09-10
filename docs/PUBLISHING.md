# Website integration

The site can be served from a dedicated directory on any static web server.
Keep the HTML files, `assets/` and referenced `docs/` together. Internal URLs
are relative.

## Lab banner

The banner and its `SHOW_LAB_HEADER` flag are in `tools/site_chrome.py`.
Set the flag to `False` and run `python3 tools/build.py` to omit the banner.

`?embed=1` hides the masthead and footer for an integration preview.
When incorporating content into another template, include the scoped CSS/JS
once and use the `.aix-research.embedded` wrapper. Do not nest complete HTML
documents. Check relative asset paths and host stylesheet interactions.

## Content sources

Research citations appear in `references.html`. Media credits are listed in
[ASSET_CREDITS.md](ASSET_CREDITS.md).
