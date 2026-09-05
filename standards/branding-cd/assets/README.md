# CD assets

Files the `STD-CD` rules point at. Referenced from a rule by path, never by description.

| File | What it is | Licence | Cleared for embedding in a published page |
|------|------------|---------|-------------------------------------------|
| `tokens.json` | colour, type and spacing tokens | internal | yes |
| `[FILL: logo-primary.svg]` | primary logo | internal | [FILL: yes/no] |
| `[FILL: fonts/...woff2]` | licensed typeface | [FILL: foundry + licence type] | [FILL: yes/no — a desktop-only licence is a no] |

## Two hard constraints

**Everything is embedded, never linked.** The prototype is one self-contained HTML file published as a private page whose content policy blocks external stylesheets, fonts, images and media. An asset that is linked simply does not appear, with no error. SVG goes inline; fonts and raster images become `data:` URIs.

**Weight is a real limit.** The published page must stay under 16 MB including every embedded asset, and a base64 `data:` URI is about a third larger than the file. Two subset `woff2` weights and an inline SVG logo are comfortable; a full family with five weights and a photographic hero is not. Subset the fonts to the characters the UI language needs.

**Licence before embedding.** Embedding a font as a `data:` URI redistributes the font file to everyone who opens the page. Most desktop licences forbid that and many webfont licences cap page views. If the row above does not say "cleared", the prototype falls back to the nearest system stack and reports the substitution instead of embedding.
