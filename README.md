# Glyn Wilcox: website concepts

Static website concepts for Glyn Wilcox (ska singer, vinyl DJ and Palm Torbay radio presenter) and his band, The Simmertones.

The gallery has two tabs:

- **Combined** (`index.html`): six concepts for Glyn's all-in-one site.
- **Simmertones** (`simmertones/index.html`): six band-site concepts, with the three 2026 restyles on top and the first round below.

Each concept is a single self-contained `index.html` (inline CSS/JS, Google Fonts) with its own `assets/`. *Toon Torbay* also loads Three.js from a CDN. There's no build step: open `index.html` locally, or publish with GitHub Pages (Settings → Pages → deploy from branch `main`, folder `/`).

- `CONCEPTS.md` and `simmertones/CONCEPTS.md`: the design briefs.
- `reference/REFERENCE.md`: research facts, copy deck and source images. Its band section is the source of truth for every Simmertones fact.
- `tools/build_gallery.py`: regenerates both gallery pages (`python tools/build_gallery.py`).
- `shots/`: gallery screenshots (640×400).

### Combined (Glyn)

| Concept | Path |
|---|---|
| The Late Session (elegant) | `samples/late-session/` |
| Liner Notes (elegant) | `samples/liner-notes/` |
| Offbeat (modern) | `samples/offbeat/` |
| The Selector (modern) | `samples/selector/` |
| Boss Sounds (on-brand) | `samples/boss-sounds/` |
| Ten Feet Tall (on-brand) | `samples/ten-feet-tall/` |

### The Simmertones (band)

| Concept | Path |
|---|---|
| Two Tone (2026, monochrome editorial) | `simmertones/two-tone/` |
| Toon Torbay (2026, toon-shaded WebGL) | `simmertones/toon-torbay/` |
| Windrush (2026, label shop) | `simmertones/windrush/` |
| Something for the Weekend (on-brand barbershop) | `simmertones/something-for-the-weekend/` |
| Main Stage (modern, for promoters) | `simmertones/main-stage/` |
| Master Tape (studio session) | `simmertones/master-tape/` |
