# Listing copy

## Claim boundary

Every buyer-facing claim traces to a source in the record. Check each before
finalizing:

| Claim | Acceptable source |
| --- | --- |
| Identity and variant | Seller confirmation, a readable label, or cited evidence tied to this item |
| Condition, wear, defects, tests | Seller confirmation or direct observation only; no source can prove this unit's condition |
| Features and compatibility | Cited evidence for the confirmed model, plus seller or observed evidence when the claim is about this unit, an included accessory, or a working setup |
| Included items | Seller confirmation or direct observation |
| Price | `pricing.approved` only; never imply a private floor |
| Warranty | Seller confirmation or cited terms showing it exists and transfers |

A claim without a source is removed, marked unknown for the seller, or becomes
the one question that would support it. Copy never turns an inference into a
fact.

If the seller directs a claim the evidence does not fully support, state the
concern once, then use their wording and record it in the decision history as
seller-directed with the concern raised. Do not repeat the objection later.

## Title

Exact product identity first, then a meaningful confirmed variant or condition,
then at most one credible differentiator (a confirmed accessory or test result)
if space allows. Searchable, plain, concise: no decorative symbols, clickbait,
all-caps, keyword stuffing, or unsupported claims.

## Description

Write these parts in order, omitting any the claim check does not support:

1. The item and its condition.
2. Verified highlights that matter to a buyer.
3. Included items.
4. Testing, and material defects or limitations.
5. The approved price.
6. A plain close.

The description is complete with those six parts and nothing else. Use short,
ordinary sentences and name a limitation plainly.

Pickup, delivery, meetup, the seller's town, and payment are not description
content: they live in the form's delivery and location settings, the record's
`seller.*` fields, and buyer conversations. The description never mentions a
payment method. If the seller explicitly asks for a transaction term in the
description, add it as a final sentence after the price and note the request in
the record.

## Natural language

If the humanizer skill is installed, run it on the title and description drafts.
Otherwise do the same pass yourself: audit every claim against its source,
remove inflated or promotional phrasing, read for plain natural language, then
recheck that facts and price are unchanged. Humanizing only rephrases; it never
adds a claim, changes a price, or edits the record.

## Example

Illustrative facts only; never copy them into a real listing.

Input: seller-confirmed Jabra Elite 8 Active Gen 2 earbuds, navy; seller
confirms both earbuds and the case work and that pairing and playback were
tested; observed earbuds, charging case, and USB-C cable; observed light scuffs
on the case; seller-confirmed pickup only (`seller.fulfillment`, set in the
form); approved price $80.

Title: `Jabra Elite 8 Active Gen 2 Earbuds, Navy, Tested`

Description:

> Jabra Elite 8 Active Gen 2 earbuds in navy. Tested for pairing and playback;
> both earbuds and the charging case work. Includes the earbuds, charging case,
> and USB-C cable. The charging case has light scuffs, shown in the photos.
> Price is $80. Please message with questions.

Every statement traces to the input. Pickup lives in the delivery settings, and
the copy adds no model features, battery claims, cleanliness claims, payment
methods, or accessories.
