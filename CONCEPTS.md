# Glyn Wilcox: six website concepts

Read `reference/REFERENCE.md` first. It holds the facts, copy deck, site map, colours and image inventory.
Pairs: **Elegant** (1–2), **Modern** (3–4), **On-brand** (5–6, built from his real artwork).

---

## Build instructions for the sample agent(s)

- Build one sample per concept at `samples/<slug>/index.html`. Each is a single self-contained HTML file with inline CSS/JS, Google Fonts only, and no build step.
- Load images by relative path: `../../reference/images/<file>`.
- Implement the full shared site map (7 sections), responsive down to 360px wide, with no horizontal scroll.
- Use only the real facts and copy from REFERENCE.md. No invented testimonials, prices or quotes. Mark extra gigs and contacts as `[Placeholder]`.
- Both photos are low-res (300–600px). Never stretch them past their native size. Use duotone, halftone, grain, framing or cut-out treatments instead.
- The "Listen live" button links to `https://player.aiir.com/palmtorbay/`. The Mixcloud archive can be a styled card linking to the show URL, or an iframe embed.
- Respect `prefers-reduced-motion` for every animation.
- Each sample should feel unmistakably different from the other five.

---

## 1. Elegant: "The Late Session"

**Idea:** A 1960s Kingston supper club after midnight. The site feels like a velvet-rope listening room, with ska presented as the sophisticated, jazz-rooted music it is (The Skatalites were jazz players).

- **Mood:** low light, brass, smoke, polished wood, the hush before the band counts in.
- **Palette:** ink `#0E0D0B`, warm charcoal `#1C1A17`, brass `#C6A15B`, cream `#EDE4D0`, single accent oxblood `#6E1F24`.
- **Type:** *Cormorant Garamond* (display, italic for names) + *Montserrat* small caps with wide letter-spacing for labels.
- **Layout:**
  - Centred, symmetrical and generous: a "menu card" structure.
  - Hero: the portrait in a thin brass oval frame, "Glyn Wilcox" in large italic serif, "Singer · Selector · Broadcaster" in spaced caps beneath.
  - Sections are separated by a thin brass rule with a small ★ (borrowed from his logo).
  - Gigs are presented like an evening programme ("Sunday, 20 September · The Railway Brewhouse · from three o'clock").
- **Signature moments:**
  - A slow-rotating 7" record behind the hero portrait (CSS, very subtle).
  - The radio section is styled like a vintage valve radio dial, with a needle that points to "SUN 7PM".
- **Copy voice:** understated, slightly old-world. Tagline: *"Boss sounds, after dark."*
- **Avoid:** checkerboards and loud colour. Restraint is the point.

## 2. Elegant: "Liner Notes"

**Idea:** An editorial monograph, as if Glyn's career were the subject of a beautifully printed reissue booklet. Long-form, typographic, gallery-calm.

- **Mood:** reissue box-set booklet, museum caption, broadsheet culture section.
- **Palette:** paper `#F5F1E8`, ink `#151515`, mid-grey `#8A857A`, single accent burgundy `#7A1E2C` (from his polo stripes).
- **Type:** *Fraunces* (display, high-contrast optical sizes) + *Inter* (body) + *IBM Plex Mono* for catalogue numbers and dates.
- **Layout:**
  - Asymmetric editorial grid with big margins.
  - Hero: huge "Glyn Wilcox" set across the page, a small captioned portrait offset to the right ("Fig. 1 — On the decks, Torbay").
  - Story section as a numbered **timeline** in the margin (age 10 · Too Hot · The Simmertones, 2007 · Madness, 2018 · Palm Torbay).
  - Discography shown as a catalogue (SIM-001, SIM-002…), with covers small and precise, and hover reveals track count and year.
  - Pull-quote: "the magical vocals of Glyn Wilcox" (cite Last.fm).
- **Signature moments:**
  - Footnote-style superscripts linking to sources.
  - Scroll-triggered fade-in of paragraphs, like turning pages.
- **Copy voice:** knowledgeable music writer. Tagline: *"Twenty-five years on the offbeat."*
- **Avoid:** heavy imagery. Typography carries it.

## 3. Modern: "Offbeat"

**Idea:** Ska's defining feature, the offbeat skank (the chop on the "and"), becomes the motion system. A bold, kinetic, poster-like site where things move on the offbeat.

- **Mood:** contemporary gig poster, Swiss grid meets 2-Tone, high contrast.
- **Palette:** black `#0B0B0B`, white `#FAFAFA`, one electric accent: signal red-orange `#FF4A1C` (a nod to his roundel, but used in a modern way).
- **Type:** *Archivo Black* / *Archivo Expanded* (display, huge) + *Space Grotesk* (body).
- **Layout:**
  - Full-viewport hero with "SKA AU GO GO" in giant stacked type and "GLYN WILCOX" in a thin line beneath.
  - A horizontal **marquee ticker** of upcoming dates and "ON AIR SUN 19:00".
  - Sections are hard-edged blocks that alternate black and white (a modern take on checkerboard: the squares are layout blocks, not wallpaper).
  - Gigs as large list rows with arrows that slide in on hover.
- **Signature moments:**
  - Elements pulse or shift on an offbeat rhythm (a CSS animation timed around 150 BPM, beat 2 and 4 only).
  - A **sticky mini "Listen live" pill** fixed bottom-right, with a red dot that pulses on Sundays 7–9pm (JS checks the UK time) and otherwise shows "Next show: Sun 7pm".
  - The portrait is rendered as a high-contrast black and white halftone.
- **Copy voice:** punchy, short. Tagline: *"Ska. Reggae. Rocksteady. Loud."*
- **Avoid:** retro pastiche fonts. This should look like 2026.

## 4. Modern: "The Selector"

**Idea:** Radio-first and app-like: a sleek listening hub for the Sunday show and the archive, with the band and DJ bookings as secondary rooms. Think Spotify or NTS Radio, with a deep sound-system palette.

- **Mood:** NTS / Rinse FM / boiler-room dark UI, waveforms, now-playing energy.
- **Palette:** deep green-black `#0B1410`, surface `#13201A`, Jamaican gold `#F2C230`, leaf green `#2FBF71`, soft white `#E9EFEA`. Use red `#E2401E` only for the "LIVE" badge.
- **Type:** *Inter Tight* (UI, all weights) + *JetBrains Mono* for times and episode numbers.
- **Layout:**
  - Hero is a **player card**: show art, "The Ultimate Ska & Reggae Show", "with Glyn Wilcox", a big play button (opens the live player), and a countdown to next Sunday 19:00 (UK time, JS).
  - Below it, **"Past shows"** as a horizontal scroll of episode cards (#24 is real and links to Mixcloud; the rest are `[Placeholder]` cards).
  - Then tabs or segments: *DJ Nights* · *The Simmertones* · *About* · *Book*.
  - Glassy cards with soft borders, and an animated SVG waveform behind the hero.
- **Signature moments:**
  - The live countdown/"ON AIR NOW" state switch.
  - "Genres played" chips (Ska · Rocksteady · Reggae · Dub · Vintage).
  - Smooth card hover lift.
- **Copy voice:** friendly and direct. Tagline: *"Two hours of boss sounds, every Sunday."*
- **Avoid:** checkerboard and heavy retro. Keep it product-like.

## 5. On-brand: "Boss Sounds"

**Idea:** Build straight from his **Ska Au Go Go roundel**. The site is a love letter to 1960s Jamaican 7" labels (Blue Beat, Trojan, Studio One) using his real logo, colours and lettering.

- **Mood:** label art, rubber stamps, sleeve wear, sound-system posters, "BOSS SOUNDS".
- **Palette (from the roundel):** black `#0A0A0A`, red-orange `#E2401E`, white `#FFFFFF`, with a worn-paper off-white `#F0E9DC` for light sections.
- **Type:** *Bowlby One* or *Rubik Mono One* for the chunky display (echoing the roundel's wobbly letters), *Special Elite* (typewriter, matching "BOSS SOUNDS" ring text) for labels, and *Work Sans* for body.
- **Layout:**
  - Hero: the **roundel logo large and centred**, slowly rotating like a record on a black field, with the red petal sunburst extended as a radiating CSS pattern behind it.
  - "GLYN WILCOX PRESENTS" above it in typewriter type.
  - Each section is styled like a **7" record label**: a circular badge header with a centre hole, and text curved round the edge (SVG textPath) for the section names ("ON AIR", "THE SIMMERTONES", "BOOK A NIGHT").
  - Gigs are styled as **sound-system dance posters** (block colour, stacked type, "ADMISSION £2").
  - Subtle grain and paper texture overlay.
- **Signature moments:**
  - Hovering the logo makes it spin up like a turntable reaching 45rpm.
  - Section dividers use the sunburst petal motif.
  - A footer stamp: "SKA · REGGAE · ROCKSTEADY · TORBAY".
- **Copy voice:** sound-system MC, a little playful. Tagline: *"Boss sounds from the English Riviera."*
- **Assets:** `mixcloud-avatar.jpg` (crop it to a circle with CSS `border-radius:50%`, since its background is black) and `glyn-palm-torbay.jpg` as a red/black duotone.

## 6. On-brand: "Ten Feet Tall": Two-Tone Riviera

**Idea:** Bring all his worlds under one roof using the real artwork palette: **The Simmertones' *Ten Feet Tall* cover** (cream, burgundy, yellow starburst, coral/teal hand-lettering), **his own look** (striped polo, pork-pie hat, DMs), and a nod to **Palm Torbay** (palms, the Riviera). Mod/2-Tone heritage meets the English seaside.

- **Mood:** 2-Tone rude boy on Torquay seafront, comic-book starbursts, seaside postcard, retro and joyful.
- **Palette:** cream `#F2EBDA`, burgundy `#8C1D38`, starburst yellow `#F5D01C`, coral `#E8574F`, teal `#3BA6C4`, ink `#14161C`. Black and white checkerboard used sparingly as a trim band.
- **Type:** *Bangers* for comic starburst headings (like the band logo), *Pacifico* or *Yellowtail* for the hand-lettered accent words, and *Nunito* or *DM Sans* for body.
- **Layout:**
  - Hero: a cream field, a yellow comic **starburst** reading "GLYN WILCOX!", the portrait cut out with a thick white sticker border, and hand-lettered "Ska Au Go Go" in coral and teal at a jaunty angle (like "TEN FEET TALL").
  - A **racing-stripe band** (burgundy/cream/navy, taken from his polo) runs across the page as the section divider.
  - "Three hats" trio cards: **The Singer** (Simmertones), **The Selector** (Ska Au Go Go), **The Broadcaster** (Palm Torbay). Each card links to its section.
  - Discography displayed as a fanned stack of the real album covers, which spread out on hover.
  - The radio section has a small "As heard on Palm Torbay" badge with a palm motif.
  - Footer: a checkerboard strip and "Made in Torbay".
- **Signature moments:**
  - Album covers fan out on hover.
  - The starburst wobbles slightly.
  - Polaroid- or postcard-style gig cards ("Greetings from Teignmouth!").
- **Copy voice:** warm, cheeky, seaside. Tagline: *"Get dressed up and start skanking."*
- **Assets:** all three Simmertones covers, `mixcloud-show-art.jpg` (hat photo), `glyn-palm-torbay.jpg`, and the Palm Torbay logo, used small.

---

## Comparison at a glance

| # | Concept | Bucket | Feel | Hero device | Key colours |
|---|---|---|---|---|---|
| 1 | The Late Session | Elegant | Supper club, after dark | Brass-framed portrait + spinning 7" | ink · brass · cream |
| 2 | Liner Notes | Elegant | Editorial reissue booklet | Giant serif name + captioned figure | paper · ink · burgundy |
| 3 | Offbeat | Modern | Kinetic gig poster | Giant stacked type + date ticker | black · white · signal red |
| 4 | The Selector | Modern | Radio app / NTS | Player card + live countdown | green-black · gold · green |
| 5 | Boss Sounds | On-brand | 60s Jamaican 7" label | His real roundel, spinning | black · red-orange · white |
| 6 | Ten Feet Tall | On-brand | 2-Tone seaside comic | Starburst + sticker cut-out | cream · burgundy · yellow · teal |
