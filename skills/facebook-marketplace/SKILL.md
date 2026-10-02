---
name: facebook-marketplace
description: Researches, prices, selects photos for, drafts, and posts Facebook Marketplace listings from whatever the seller has (a photo, a model name, a folder of media), keeping one listing record per item and gating form entry and publication on separate seller approvals. Use when the user wants to sell an item on Facebook Marketplace, price a used item against local listings, write or revise a listing, choose listing photos, or fill in and publish the Marketplace form.
---

# Facebook Marketplace

Build the strongest truthful listing the evidence supports. Make progress from
partial input, keep the listing record current, and leave every consequential
choice to the seller (the user).

## Terms

- **Listing record**: one Markdown file per item with YAML frontmatter, started
  from [assets/listing.md](assets/listing.md). It holds every fact, source,
  decision, and approval; chat carries only what the seller needs to act.
- **Project configuration**: the seller's area, improvement threshold,
  fulfillment policy, and payment policy, wherever the project keeps them
  (usually its CLAUDE.md). This skill embeds no location, amount, or seller
  preference; when a value is missing, ask for it rather than assume one.
- **Provenance**: label each material fact `seller-confirmed`, `observed`,
  `source-supported`, `inferred`, or `unknown` in the record. A photo shows only
  what is visible: it never proves cleanliness, function, or an unseen
  accessory. A source shows what a model can do, never this unit's condition.
  An unknown stays unknown until evidence changes it.

## Workflow

Track progress with this checklist. Keep it in your own working notes, not in
replies to the seller, who needs only the next decision:

```
Listing progress:
- [ ] 1 Read project configuration and the listing record
- [ ] 2 Provisional read of the inputs and media
- [ ] 3 Product research
- [ ] 4 Local Marketplace assessment
- [ ] 5 Readiness: draft now, or name the one improvement worth asking for
- [ ] 6 Price and positioning
- [ ] 7 Buyer-facing copy
- [ ] GATE A: seller approves the listing design
- [ ] 8 Fill the live form (reversible entry only)
- [ ] GATE B: seller approves the populated form
- [ ] GATE C: seller separately authorizes publication
- [ ] 9 Publish and record the outcome
```

| Step | Read |
|---|---|
| 2 | [references/intake.md](references/intake.md), [references/media.md](references/media.md) |
| 3 | [references/product-research.md](references/product-research.md) |
| 4 | [references/marketplace-assessment.md](references/marketplace-assessment.md) |
| 6 | [references/pricing-and-positioning.md](references/pricing-and-positioning.md) |
| 7 | [references/listing-copy.md](references/listing-copy.md) |
| 8, 9 | [references/browser-posting.md](references/browser-posting.md) |
| Any external action, media selection, or buyer reply | [references/privacy-and-payment.md](references/privacy-and-payment.md) |

The order is a default, not a script: follow the seller's current direction and
skip what the record already settles. When input is sparse, open with a useful
provisional read and a path to either draft now or improve the listing with one
input. Ask at most one consequential question per turn, and let each answer
choose the next action. Keep detailed research in the record unless it
explains the recommendation or the seller asks for it.

## Approval gates

These are fixed. Record each approval in `approvals.*` with its scope,
decision, actor, and time.

| Gate | Covers | Permits | Does not permit |
|---|---|---|---|
| A `listing_design` | Price, title, description, selected media and order, category, condition, fulfillment, every known form choice | Reversible entry of those values into the form | Publishing |
| B `populated_form` | The visible state of the filled form | Asking for publication | Clicking Publish |
| C `publication` | An explicit, current yes, asked right after gate B | Clicking Publish once | Publishing after any later change |

- A recommendation, delegated judgment ("use your judgment"), an earlier or
  broader approval, or the seller being unavailable is never an approval.
- An approval goes stale when a value it covers changes, a platform change
  alters the visible listing, the form raises a consequential choice the design
  did not resolve, or the filled state cannot be verified after a browser
  interruption. Preserve the work, name the difference, and ask again for the
  affected gate. Append a decision-history entry when an approved value changes.
- Never bypass a login, security check, warning, restriction, or confirmation
  screen. Stop and give the recovery report in browser-posting.md.

## Optional independent review

When uncertainty or judgment risk justifies the overhead, get an independent
product, pricing, skeptical-buyer, or marketing review through any available
consultation or delegation capability. Verify its claims against the record and
sources. A review never replaces a seller approval.
