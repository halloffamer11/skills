---
# Listing record template. Copy it per item and fill fields only as evidence or
# the seller confirms them; use null, [] or "unknown" rather than a guess.
# Do not add a phase or workflow-state field: the approvals show where things stand.
schema_version: 1
listing_id: null
item:
  brand: null
  model: null
  variant: unknown          # color, SKU, generation, size
  category: null
  quantity: 1
  units: []                 # only when one listing offers distinct units: [{id, model, label_facts}]
condition:
  seller_assessment: unknown
  known_defects: []
  included_items: []
  tested: unknown           # what was tested, how, and the result
seller:
  postal_code: null
  fulfillment: []           # pickup, delivery, shipping; set in the form, not the description
  payment: null             # usually inherited from project configuration; for buyer replies only
pricing:
  currency: null
  recommended: null         # a proposal, never an approval
  approved: null            # only the seller sets this
listing:
  title: null
  description: null
  category: null            # the Facebook category chosen
  condition: null           # the Facebook condition label chosen
media:
  source_directory: null    # seller originals, never modified
  derived_directory: null
  selected: []              # in display order: [{file, source, evidence_note}]
approvals:                  # each entry: {scope, decision, actor, time}
  listing_design: null
  populated_form: null
  publication: null
publication:
  url: null
  published_at: null
---

# Facts and provenance

<!-- One line per material fact, labelled seller-confirmed, observed,
source-supported, inferred or unknown. -->

# Open questions

# Research

<!-- Claim records (product research), Marketplace observations and their
limits, pricing rationale. -->

# Media notes

<!-- What each file shows; rejected files and why. -->

# Form mapping

<!-- Filled during browser posting. -->

# Decision history

<!-- Append an entry whenever an approved value changes, and for any
seller-directed claim with the concern raised. -->
