"""Builds the two gallery pages (index.html = Combined, simmertones/index.html = Simmertones).

Run from the repo root:  python tools/build_gallery.py
Edit the CARDS data below to add or reorder concepts; screenshots live in shots/<slug>-{1,2,3}.jpg.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

COMBINED = [
    ("samples/late-session/", "late-session", "Elegant", "The Late Session",
     "A Kingston supper club after midnight, with brass, ink and a slowly spinning 7\".",
     ["Hero", "On air", "The Simmertones"]),
    ("samples/liner-notes/", "liner-notes", "Elegant", "Liner Notes",
     "An editorial reissue booklet with a typographic timeline and a catalogue-style discography.",
     ["Hero", "Story", "The Simmertones"]),
    ("samples/offbeat/", "offbeat", "Modern", "Offbeat",
     "A kinetic gig poster where everything moves on the offbeat.",
     ["Hero", "On air", "What’s on"]),
    ("samples/selector/", "selector", "Modern", "The Selector",
     "A radio-first listening hub with a live countdown to Sunday 7pm.",
     ["Hero", "DJ nights", "The Simmertones"]),
    ("samples/boss-sounds/", "boss-sounds", "On-brand", "Boss Sounds",
     "Built from his Ska Au Go Go roundel, in the style of a 1960s Jamaican 7\" label.",
     ["Hero", "On air", "What’s on"]),
    ("samples/ten-feet-tall/", "ten-feet-tall", "On-brand", "Ten Feet Tall",
     "A Two-Tone Riviera look taken from The Simmertones' album art and his mod style.",
     ["Hero", "Ska Au Go Go", "The Simmertones"]),
]

BAND_NEW = [
    ("two-tone/", "simmertones-two-tone", "2026 · Editorial", "Two Tone",
     "Strict black and white. The band name crosses a checkerboard, inverting square by square, and stretches as you scroll.",
     ["Hero", "Line-up", "Press"]),
    ("toon-torbay/", "simmertones-toon-torbay", "2026 · WebGL", "Toon Torbay",
     "A toon-shaded 3D Torbay of beach huts, a bandstand and a festival field, built on a spinning 7\" record that turns as you scroll.",
     ["Hero", "Line-up", "Records"]),
    ("windrush/", "simmertones-windrush", "2026 · Label shop", "Windrush",
     "The band's own label as a premium record shop, with 3D records you can spin and a crate to collect them.",
     ["Hero", "Catalogue", "The band"]),
]

BAND_FIRST = [
    ("something-for-the-weekend/", "simmertones-something-for-the-weekend", "On-brand", "Something for the Weekend",
     "A 1960s barbershop taken from their 2013 album cover, with gilt window lettering, a turning barber pole and a felt letterboard for gigs.",
     ["Hero", "The chairs", "What’s on"]),
    ("main-stage/", "simmertones-main-stage", "Modern", "Main Stage",
     "A cobalt festival identity built for promoters, with a rider-style fact sheet, an interactive stage plot and a copy-ready bio.",
     ["Hero", "Stage plot", "Records"]),
    ("master-tape/", "simmertones-master-tape", "Craft", "Master Tape",
     "The band as a recording session: a nine-channel mixing desk, tape boxes with track sheets, and a take log.",
     ["Hero", "Tape shelf", "Take log"]),
]

CSS = """
  :root { --bg:#0b0b0b; --fg:#f4f1ea; --muted:#9a958b; --card:#161616; --line:#2a2a2a; --accent:#e2401e; }
  * { box-sizing:border-box; }
  body { margin:0; background:var(--bg); color:var(--fg); font-family:Inter,system-ui,sans-serif; line-height:1.5; }
  main { max-width:1100px; margin:0 auto; padding:28px 16px 64px; }
  .tabs { display:inline-flex; gap:4px; padding:4px; background:var(--card); border:1px solid var(--line); border-radius:999px; margin:0 0 36px; }
  .tabs a { color:var(--muted); text-decoration:none; font-weight:600; font-size:.95rem; padding:8px 18px; border-radius:999px; transition:background .2s,color .2s; }
  .tabs a:hover { color:var(--fg); }
  .tabs a[aria-current="page"] { background:var(--fg); color:var(--bg); }
  .tabs a:focus-visible { outline:2px solid var(--accent); outline-offset:2px; }
  h1 { font-size:clamp(2rem,6vw,3.5rem); font-weight:800; margin:0 0 8px; letter-spacing:-.02em; }
  h1 span { color:var(--accent); }
  p.lead { color:var(--muted); max-width:62ch; margin:0 0 36px; }
  h2.group { font-size:clamp(1.4rem,3.6vw,2rem); font-weight:800; letter-spacing:-.01em; margin:56px 0 6px; }
  h2.group:first-of-type { margin-top:8px; }
  h2.group + p.lead { margin-bottom:24px; }
  .grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(min(100%,330px),1fr)); gap:16px; }
  a.card { display:block; background:var(--card); border:1px solid var(--line); border-radius:14px; padding:24px; color:inherit; text-decoration:none; transition:transform .2s, border-color .2s; }
  a.card:hover, a.card:focus-visible { transform:translateY(-3px); border-color:var(--accent); outline:none; }
  .tag { font-size:.75rem; text-transform:uppercase; letter-spacing:.12em; color:var(--accent); font-weight:600; }
  .card h3 { margin:6px 0 8px; font-size:1.4rem; }
  .card p { margin:0 0 14px; color:var(--muted); font-size:.95rem; }
  .shots { display:grid; grid-template-columns:1fr 1fr; gap:6px; margin-top:4px; }
  .shots figure { margin:0; position:relative; border-radius:8px; overflow:hidden; border:1px solid var(--line); background:#000; }
  .shots .s1 { grid-column:1 / -1; }
  .shots img { display:block; width:100%; height:auto; aspect-ratio:16/10; object-fit:cover; transition:transform .4s; }
  a.card:hover .shots img { transform:scale(1.03); }
  .shots figcaption { position:absolute; left:6px; bottom:6px; font-size:.68rem; font-weight:600; letter-spacing:.06em; text-transform:uppercase; background:#000c; color:#fff; padding:2px 7px; border-radius:4px; }
  footer { margin-top:48px; color:var(--muted); font-size:.85rem; }
  @media (prefers-reduced-motion:reduce){ a.card,.shots img,.tabs a{transition:none;} }
"""


def card(href, shot, tag, title, desc, caps, prefix):
    figs = "".join(
        f'<figure class="s{i}"><img src="{prefix}shots/{shot}-{i}.jpg" alt="{escape(title)}: {escape(c)} section" '
        f'width="640" height="400" loading="lazy"><figcaption>{escape(c)}</figcaption></figure>'
        for i, c in enumerate(caps, 1)
    )
    return (f'    <a class="card" href="{href}"><span class="tag">{escape(tag)}</span><h3>{escape(title)}</h3>'
            f'<p>{escape(desc)}</p><div class="shots">{figs}</div></a>\n')


def page(title, prefix, current, body):
    tabs = (f'<nav class="tabs" aria-label="Concept sets">'
            f'<a href="{prefix or "./"}"{" aria-current=\"page\"" if current == "combined" else ""}>Combined</a>'
            f'<a href="{prefix}simmertones/"{" aria-current=\"page\"" if current == "band" else ""}>Simmertones</a></nav>')
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<link rel="icon" href="{prefix}samples/boss-sounds/assets/roundel.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<main>
  {tabs}
{body}  <footer>Concept samples. Facts come from public sources; items marked [Placeholder] are not real data.</footer>
</main>
</body>
</html>
"""


def grid(cards, prefix, href_prefix=""):
    return '  <div class="grid">\n' + "".join(card(href_prefix + c[0], *c[1:], prefix) for c in cards) + "  </div>\n"


combined_body = (
    '  <h1>Glyn Wilcox <span>·</span> Ska Au Go Go</h1>\n'
    '  <p class="lead">Six concepts for Glyn\'s all-in-one site, which covers him as a singer, a vinyl DJ and a Palm Torbay radio presenter. '
    'Two are elegant, two are modern, and two are built from his own branding.</p>\n'
    + grid(COMBINED, "")
)

band_body = (
    '  <h1>The Simmertones <span>·</span> band sites</h1>\n'
    '  <p class="lead">Six concepts for the nine-piece Torbay ska band Glyn fronts. '
    'All of them use the research of 24 November 2026: the named line-up, the full <i>Ten Feet Tall</i> tracklist, and the confirmed live history.</p>\n'
    '  <h2 class="group">Modern restyles</h2>\n'
    '  <p class="lead">Three 2026 restyles. Each takes its technique from an award-winning artist site and keeps the ska heritage.</p>\n'
    + grid(BAND_NEW, "../")
    + '  <h2 class="group">First round</h2>\n'
    '  <p class="lead">The original three band concepts, updated with the new facts.</p>\n'
    + grid(BAND_FIRST, "../")
)

(ROOT / "index.html").write_text(page("Glyn Wilcox · Site Concepts", "", "combined", combined_body), encoding="utf-8", newline="\n")
(ROOT / "simmertones" / "index.html").write_text(page("The Simmertones · Site Concepts", "../", "band", band_body), encoding="utf-8", newline="\n")
print("wrote index.html and simmertones/index.html")
