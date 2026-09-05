# Registry index

| Prefix | Module | Authority | Version | Source version | Status | Rules | Assets |
|--------|--------|-----------|---------|----------------|--------|-------|--------|
| `STD-A11Y` | [accessibility-eaa](accessibility-eaa/) | law | 1.0 | EN 301 549 v3.2.1 (→ WCAG 2.1 AA) | active | 15 required + 3 recommended | — |
| `STD-CD` | [branding-cd](branding-cd/) | internal | 0.1 | — (self-versioned) | **draft — values are placeholders** | 9 required + 1 recommended | `assets/` |

Authority bands, strongest first: `law` → `contract` → `internal`. Inside a band, lower `precedence` wins. A breach of a `required` rule in a `law` module blocks acceptance; everything else warns.

## Prefixes

**In use**: `STD-A11Y`, `STD-CD`.

**Held for the modules this mechanism was built to carry next**: `STD-GDPR` (data protection), `STD-SEC` (security), `STD-TONE` (tone of voice). Taking one of these for something else is fine — reserving it is only to stop two people picking `STD-SEC` for different things in the same week.

A prefix that has ever existed is never reused, not even after its module is retired.
