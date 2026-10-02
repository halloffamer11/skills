#!/bin/sh
# A listing record for a window AC unit: identity confirmed, condition and
# testing unknown, design approved at $180, no form or publication approval.
# Usage: sh evals/fixtures/ac-unit-record.sh <dest>
set -e
dest=$1
[ -n "$dest" ] || { echo "usage: $0 <dest-dir>" >&2; exit 2; }
[ ! -e "$dest" ] || { echo "$dest exists" >&2; exit 2; }
mkdir -p "$dest/ac-unit/photos"
cd "$dest"
cat > CLAUDE.md <<'X'
# Selling

- Seller area: postal code 30306, 15-mile radius.
- Improvement threshold: $25.
- Fulfillment: pickup only.
- Payment: cash or the platform's checkout.
X
cat > ac-unit/listing.md <<'X'
---
schema_version: 1
listing_id: ac-unit
item:
  brand: Midea
  model: U Inverter MAW08V1QWT
  variant: 8,000 BTU
  category: Appliances
  quantity: 1
  units: []
condition:
  seller_assessment: unknown
  known_defects: []
  included_items: [unit, window bracket, remote]
  tested: unknown
seller:
  postal_code: "30306"
  fulfillment: [pickup]
  payment: null
pricing:
  currency: USD
  recommended: 180
  approved: 180
listing:
  title: Midea U Inverter 8,000 BTU Window AC with Remote
  description: null
  category: Appliances
  condition: null
media:
  source_directory: ac-unit/photos
  derived_directory: null
  selected: []
approvals:
  listing_design: {scope: "price 180, title", decision: approved, actor: seller, time: "2026-09-20T15:00:00Z"}
  populated_form: null
  publication: null
publication:
  url: null
  published_at: null
---

# Facts and provenance
- Brand, model, variant: seller-confirmed from the label.
- Included items: observed in photos.
- Condition, testing: unknown.
X
