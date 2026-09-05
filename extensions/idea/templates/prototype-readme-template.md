# Prototype folder

`prototype.html` is built from the spec and republished to the same URL on every spec version. `prototype-v<spec-version>.html` are the frozen snapshots, `PUBLISHED.md` records the link per version.

The prototype is the spec made clickable, not a design. Anything it shows comes from §6 of the spec; anything it does not show is not in the spec.

## Two lanes for prototype feedback

| Feedback sounds like | It is | Where it goes |
|----------------------|-------|---------------|
| "Button bigger", "colour too harsh", "table too dense", "this looks unfinished" | Visual | Stays in the prototype. Fixed on the next `/speckit-idea-prototype` run. No spec change. |
| "The customer name is missing here", "why can't I cancel?", "nobody needs this screen", "these two steps are the wrong way round" | Content or flow | New feedback round: `/speckit-idea-feedback`. After `/speckit-idea-apply` and re-acceptance, rebuild with `/speckit-idea-prototype`. |

The AI sorts incoming prototype feedback into these lanes and says which lane each item is in. Changing content in the prototype instead of in the spec looks fast and breaks the moment someone builds from the spec.

## Accepting it

`/speckit-idea-accept --prototype` runs the prototype checklist (every SCR built, every FLOW clickable, nothing beyond the spec) and records the reviewer's name and date in the spec header. That is the end of the loop.
