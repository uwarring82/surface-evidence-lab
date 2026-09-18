# Lab webpage

`index.html` is the lab's landing page. The [Pages workflow](../.github/workflows/pages.yml) publishes it to GitHub Pages when `site/`, `teaching/figures/` or the workflow changes on `main`. The page links to the Markdown materials on GitHub instead of copying them.

- **Learning paths:** a plain-language introduction and five-step Croshaw starter lead into guided core work, an optional bounded extension and optional open research. The starter does not replace the worksheet submission. Keep each level's scope, expected output and stopping point explicit; broader freedom must retain the same standards for evidence. Students do not need to attempt every level.
- **Figure:** the workflow copies `teaching/figures/croshaw-2020-fig5.jpg` into the published site, so the figure has a single source. Keep its credit line beside the image. Reproduce no other third-party figure without a verified reuse basis; Seibert stays link-only.
- **Fonts:** `fonts/` holds IBM Plex Sans, Plex Sans Condensed and Plex Mono (latin subsets from Fontsource 5.3.0) under the SIL Open Font License; see `fonts/OFL.txt`. They are served from the site so the page makes no third-party font requests.
- **Local preview:** copy the figure into `site/figures/` and open `site/index.html`, or serve the folder with `python3 -m http.server`. Do not commit `site/figures/`.
