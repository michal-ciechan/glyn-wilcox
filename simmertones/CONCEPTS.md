# The Simmertones: three band-site concepts

These are sites for **the band**, and not for Glyn personally. The six concepts in `../samples/` cover Glyn's own site.
Read `../reference/REFERENCE.md` first, especially *The Simmertones* and *Band extras*.

The three concepts take different angles:

| # | Concept | Angle | Feel | Hero device | Key colours |
|---|---|---|---|---|---|
| A | Something for the Weekend | On-brand: built from their 2013 album cover | 1960s barbershop on a Torbay back street | Gilt window lettering + spinning barber pole | barber green · gold leaf · pole red/blue · porcelain |
| B | Main Stage | Modern: a booking tool for promoters and festivals | Contemporary festival identity, Swiss-clean | Name set "ten feet tall" in giant condensed type | cobalt · white · black · stage amber |
| C | Master Tape | Craft: the band as a recording session | Analogue studio: console, masking tape, tape boxes | A nine-channel mixing desk, one fader per member | console slate · masking tape · VU amber · REC red |

---

## Shared rules

- Put each site at `simmertones/<slug>/index.html`: a single self-contained HTML file with inline CSS/JS, Google Fonts only, no build step, and its own `assets/` folder (copy images in from `reference/images/`).
- Use only real facts. Unknowns are written as a visible `[Placeholder]`. Never invent members, tracks, quotes, prices or dates.
- Glyn Wilcox (lead vocals and toasting) is the only confirmed member. The other eight are placeholders. Show realistic ska roles (horns, rhythm section, keys) as an *example* line-up and label it as such.
- The album covers are 300×300. Never show them larger than 300px CSS. There are no band photos, so use a clearly marked `[Band photo placeholder]` frame where a photo would go.
- The site must be responsive down to 360px with no horizontal scroll. It needs visible keyboard focus, must respect `prefers-reduced-motion`, and needs real alt text.
- The enquiry form has no backend: on submit, show an inline note that this is a sample.
- Include a small cross-link to Glyn's own Sunday show (Palm Torbay, Sundays 7–9pm, https://player.aiir.com/palmtorbay/).

### Band site map (all three)
1. **Hero**: The Simmertones, nine-piece authentic ska from Torbay, South Devon. CTAs: *Book the band* and *Hear the records*.
2. **The band**: active since about 2007; originals plus classic ska and rocksteady covers; Glyn on lead vocals and toasting. Their *Doctor Who* theme cover was played on BBC Radio 1, 2 and 6 Music.
3. **Line-up**: Glyn plus eight placeholders.
4. **Records**: Vol. 1 (2009), *Everything's Comin' Up Ska* (2011), *Something for the Weekend?* (2013, MMTONES1), *Ten Feet Tall* (2019), and the single "Perhaps Perhaps Perhaps". Show the known tracks; the rest are placeholders.
5. **Live**: festivals (Bestival, Camp Bestival, Looe Music Festival, London International Ska Festival, Respect Festival Plymouth, Kingsbridge Music Fest), support for Madness at the House of Fun Weekender 2018, past Exeter Phoenix dates (2017/2019/2020), and upcoming dates as `[Placeholder]`.
6. **Press**: "the magical vocals of Glyn Wilcox" (Last.fm); "The vocals are good, the horns are perfect…" (ReadJunk, 2011); airplay on BBC Radio 1, 2 and 6 Music.
7. **Book the band**: an enquiry form (name, email, date, venue/event, message), with placeholder email and socials.

---

## A. "Something for the Weekend": the barbershop (on-brand)

**Idea:** The 2013 album cover shows a grinning barber with a cut-throat razor and a barber pole, asking the old British barber's question. The site *is* that shop: a 1960s barbershop on a Torbay back street, where the nine-piece are the barbers.

- **Palette (from the cover):** barber green `#2E9E4F`, bottle-glass green `#0E3324`, gold leaf `#D4A63A` (gilt gradient `#F7DD84` → `#D4A63A` → `#8A6418`), pole red `#D7262E`, pole blue `#1F4AA8`, porcelain `#FBFBF7`, ink `#000`.
- **Type:** *Abril Fatface* for the gilt sign-writing; *Archivo* for the body and *Archivo Narrow* for the felt letterboard. Two families.
- **Layout:**
  - Hero: a shop window of dark glass in a painted green frame. "The Simmertones" is gilded in an arch (SVG textPath, gold gradient, black drop shade). Under it, a straight gilt line reads "Authentic ska · Torbay · since 2007". A **barber pole** turns beside the window, and a black-and-white tiled floor strip sits under it. This floor is the only checkerboard on the site.
  - **The chairs** (line-up): nine barber chairs in a row, each with a ticket. Chair 1 is Glyn Wilcox, lead vocals and toasting; Chairs 2–9 are placeholders.
  - **Price list** (records): a painted price board with gilt titles and dotted leaders (title … year). Each record sits beside its small cover, and you can open it to see the known tracks.
  - **What's on** (gigs): a black felt **letterboard** with white plastic letters, slightly uneven, showing upcoming `[Placeholder]` dates and past dates.
  - **Overheard in the chair** (press): the quotes on small waiting-room cards.
  - **Book an appointment** (enquiry form) on a porcelain appointment card.
- **Signature moment:** the turning barber pole. It stops under reduced motion.
- **Copy voice:** a chatty British barber, warm and cheeky. Tagline: *"Something for the weekend?"*
- **Avoid:** using the album's cartoon as wallpaper. The cover appears only as a record.

## B. "Main Stage": the promoter's site (modern)

**Idea:** A band site built for the people who book bands: festival programmers, venue promoters and wedding planners. It's clean, confident and fast to scan, and doubles as a press kit. The name is set "ten feet tall".

- **Palette:** cobalt `#1F3BD6`, white `#FFFFFF`, black `#000000`, a cool grey `#E9EAEE` for alternate panels, and stage amber `#FFB000` used only for highlights and focus.
- **Type:** *Big Shoulders Display* (800–900, tall and condensed) for display, and *Schibsted Grotesk* for the body.
- **Layout:**
  - Hero: a cobalt field with "THE SIMMERTONES" set so tall and condensed it fills the viewport width. Beneath it are one line of positioning, two CTAs, and the *Ten Feet Tall* cover small.
  - **Fact sheet**: a two-column definition list in the form of a promoter rider (line-up, based in, plays, set lengths `[Placeholder]`, stage needs `[Placeholder]`, previously played). These are not stat tiles.
  - **Stage plot**: a top-down SVG stage with nine positions (drums, bass, guitar, keys, horns ×3–4, vocals front). Hovering or focusing a position names it. Label it "Example layout: confirm with the band".
  - **Copy-ready bio**: a 50/150-word toggle and a *Copy bio* button that confirms "Copied". It's for promoters writing listings.
  - **Records** as a clean row of covers with year and format. Live as a list of venue and festival rows. Press as large pull-quotes.
  - **Press kit downloads** (logo, photos, bio, tech rider) as `[Placeholder]` links.
- **Signature moment:** the oversized name on load. The letters rise once, staggered like a count-in, and appear instantly under reduced motion.
- **Copy voice:** plain, direct, professional. Tagline: *"Nine-piece authentic ska. Ready for your stage."*
- **Avoid:** retro pastiche, checkerboards and stat-tile rows.

## C. "Master Tape": the session (craft)

**Idea:** Nine musicians means nine channels. The site is the band's recording session: a vintage mixing console with masking-tape scribbles, reel-to-reel tape boxes on a shelf, and a track sheet in marker pen.

- **Palette:** console slate `#2B3238`, panel grey-blue `#46545F`, masking tape `#EADFB8`, tape-box board `#D8C9A6`, VU amber `#F4C04E`, REC red `#D5281B`, marker black `#000`.
- **Type:** *Permanent Marker* for anything handwritten on tape, and *Barlow* / *Barlow Condensed* for console legends and the body.
- **Layout:**
  - Hero: the console. A long strip of masking tape across the meter bridge reads "THE SIMMERTONES" in marker. Below it are **nine channel strips**, each with a real `<input type="range">` fader, a SOLO button, and a masking-tape label at the foot (Ch 1 "GLYN · VOX"; Ch 2–9 example roles marked `[Placeholder]`). Pressing SOLO shows that member's card.
  - **Tape shelf** (records): each release is a tape box with a hand-written label. Opening a box reveals its *track sheet* (the known tracks, with the rest marked as placeholders), plus the small cover taped to it as a reference print.
  - **Take log** (live): past shows as numbered takes (this is a real chronological sequence), with upcoming dates as `[Placeholder]`.
  - **Notes from the control room** (press): quotes on index cards held with tape.
  - **Book a session** (enquiry form) styled as a studio booking sheet.
  - Footer: a red stamp reading "MASTER · DO NOT ERASE".
- **Signature moment:** on load the nine faders rise to their levels one after another, like a count-in on fader automation, with a single VU needle settling. Under reduced motion they appear at their final levels.
- **Copy voice:** studio shorthand, warm and knowing. Tagline: *"Nine channels. One sound."*
- **Avoid:** spinning reels everywhere and fake skeuomorphic gloss. Keep it flat, crafted and legible.
