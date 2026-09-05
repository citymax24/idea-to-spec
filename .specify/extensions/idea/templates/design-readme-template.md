# Design folder

`brief.md` is derived from the spec. `mockups/v<spec-version>/` holds exports per spec version.

## Two lanes for mockup feedback

| Feedback sounds like | It is | Where it goes |
|----------------------|-------|---------------|
| "Button bigger", "colour too harsh", "table too dense" | Visual | Stays in the design canvas. No spec change. |
| "The customer name is missing here", "why can't I cancel?", "nobody needs this screen" | Content or flow | New feedback round: `/speckit-idea-feedback`. After `/speckit-idea-apply`, regenerate the affected artboards. |

The AI sorts incoming mockup feedback into these lanes and says which lane each item is in. Changing content in the mockup instead of the spec looks fast and breaks the moment someone builds from the spec.
