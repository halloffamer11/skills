# Browser posting

## Before entry

Start only with a current gate A approval (see SKILL.md) whose scope covers
every value you will enter. Compare the approved design with the listing record;
if anything it covers has changed, the approval is stale: keep the draft and ask
again.

## Inspect the live form

Use an available signed-in browser. The live form is the authority: read its
labels, choices, required indicators, validation, restrictions, and review and
publish controls each time. Do not rely on a remembered field schema, a
particular automation tool, or a page layout.

If the form offers a consequential choice the approved design did not resolve
(category, condition meaning, shipping commitment, location visibility, payment
or delivery term, audience), stop and ask. Do not choose for the seller.

## Enter and map values

Gate A permits reversible entry of resolved values only. Do not resolve an
unknown, accept an unexpected consequential default, enter a claim the record
cannot support, or enter private notes, research, receipt identifiers, contact
details, or pricing floors. Record a mapping in the record's Form mapping
section:

| Record value | Form field observed | Normalization or platform change |
| --- | --- | --- |
| `listing.title` | Title field label | Exact text entered; truncation |
| `pricing.approved`, `pricing.currency` | Price field label | Amount entered; displayed currency or formatting |
| `listing.description` | Description field label | Exact text entered; truncation |
| `listing.category` | Category selector | Path selected; suggested or substituted category |
| `listing.condition` | Condition selector | Label selected; platform interpretation |
| `seller.fulfillment` | Delivery, shipping, pickup controls | Options selected; resulting platform text |
| `seller.postal_code` | Location field | Locality level displayed; expose no more than needed |
| `media.selected` | Photo and video uploader | Approved files in order; reorder, rejection, processing |

Upload only the files in `media.selected`, in order. Confirm the visible order
after upload and record any reorder, crop, compression, or rejection. Any file
outside the approved set needs a new gate A approval.

## Preflight

After entry, give a concise **Preflight**: title, displayed price and currency,
category, condition, fulfillment, visible location level, media count and
order, and every normalization, warning, restriction, or unresolved choice.
Include a screenshot when it is safe to keep (see privacy-and-payment.md).
Then ask for gate B on that visible state, and after it, for gate C. If any
mapped field changes after review, repeat the preflight and gate B.

## Completion

After publication succeeds, record `publication.url`, `publication.published_at`,
the final displayed price, and any platform change seen at publication. Keep
the mapping and confirmation text. Report completion without exposing private
account or location details.

## Failure recovery

Never work around a safeguard. Keep completed reversible work and stop:

| Failure | Recovery |
| --- | --- |
| Login or expired session | Say sign-in is needed; after the seller signs in, re-inspect the form and its values |
| Account security check | Do not handle credentials, codes, or identity checks; the seller completes the step |
| Category restriction or required change | Record the restriction and alternatives; get a decision, and a new gate A if the design changes |
| UI change or unfamiliar consequential field | Record the visible labels and state; do not guess a mapping |
| Upload failure | Keep the error; retry the same approved file only if the error looks transient |
| Browser crash or lost session | Treat the filled state as unverified: reopen, re-inspect every field and the media order, repeat preflight and gate B |
| Platform warning | Keep the exact text and stop; the seller decides whether to satisfy it, change the listing, or abandon |

The recovery report names: completed work; preserved artifacts (record
location, approved media and order, mapping, safe screenshots); the exact
blocker as observed, without guessing a cause; the safest next action; and any
step only the seller can take. A recovery never turns an earlier approval into
publication authority.
