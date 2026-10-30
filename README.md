# SteamFox website

Static website for SteamFox (Slush Oulu Pitching Competition 2026).

| File | What it is |
|---|---|
| `index.html` | Landing page |
| `kit-3d.html` | Interactive 3D model of the hardware kit |
| `demo.html` | Operator dashboard demo on real Finnish spot prices |
| `logo.png` | SteamFox logo |

No build step: the pages are plain HTML and load three.js and Google Fonts from public CDNs.

## Publish with GitHub Pages

1. Upload these files to the root of the repository.
2. Settings → Pages → Source: **Deploy from a branch** → Branch: `main`, folder `/ (root)` → Save.
3. After a minute the site is live at `https://<username>.github.io/<repository>/`.
