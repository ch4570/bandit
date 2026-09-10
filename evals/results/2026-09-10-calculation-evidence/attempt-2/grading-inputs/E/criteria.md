# Case 13 — offer consistency before paid intake

Source of truth: `OPS-0910` in `approved-offer.md`, the supplied original trial record, and the scope of the Korean request. `launch-artifacts.md` is a proposed bundle, not an adopted replacement policy or evidence of a working implementation.

## P0 criteria

### J13-1 — The fulfillment promise is consistent across the journey

The review identifies both geographic/service-method and turnaround conflicts. `AD-1` promises nationwide doorstep service and next-day return, while the adopted offer is only Solbit A/B lockers and Tuesday pickup with Friday 18:00 locker return. `UX-1` permits an unsupported “other/doorstep” route, and `UX-3` repeats the unsupported 24-hour promise. Korean or translated names are acceptable if the same places are clear.

It connects the incorrect messages to the customer consequence and identifies the affected artifacts that must agree. It preserves or recognizes the corresponding accurate `LP-1` material. A finding only about advertising without the conflicting selection/completion experience is partial. A different faster/nationwide offer is not an authorized fix.

### J13-2 — Historical observations are not inflated into proof

The review identifies that all-customer satisfaction is not established by 5 responses out of 8 households, even though all 5 respondents reported satisfaction. It separately identifies the unsupported 99.9% sterilization/safety claim because no relevant testing occurred and sterilization is outside the approved offer. It does not turn the free trial into paid repurchase or pricing evidence.

It gives a usable correction, such as removing unsupported copy or narrowly describing the actual free trial conditions. Exact replacement wording is not required. “Need sources” without identifying the supplied response denominator or absent test basis is partial. It should not assert external legal violations; this is a fact/offer consistency review.

### J13-3 — Pricing uses the right order and pair units

The review finds both the waived one-pair transport fee and the duplicate first-order discount. It grounds corrections in the order-level fee/discount rule and conveys the correct first-order totals: 19,000 for one pair, 33,000 for two pairs. It ties the `AD-1` unconditional free transport/15,000 offer to the `UX-2` totals, rather than fixing only one surface.

It does not invent a subscription, recurring commitment, per-pair introductory discount, or a new transport policy. The `LP-1` per-pair base rate, two-pair free transport, one-off service, and discount statement are generally compatible with the approved offer; its missing explicit one-pair fee/maximum quantity may reasonably be flagged as a clarity improvement. A reviewer may recommend clarifying “2 pairs” instead of “2 or more” because the ordering cap is 2, but must not claim the system already allows a third pair.

### J13-4 — Capacity is measured in pairs

The review identifies the `UX-2` check against 24 orders as incompatible with the combined 24-pair capacity of both complexes. It asks for a pair-based availability/reservation check using the requested quantity before payment. It does not infer that the displayed “23 orders” means 23 pairs.

A satisfactory verification example could use an explicitly hypothetical state of 23 pairs reserved: a 1-pair request fits, a 2-pair request does not and goes to another available session without charging. Equivalent examples at the limit are acceptable. It preserves the existing correct next-session path in principle and the existing 1–2 pair quantity selection. Distributed locking or new infrastructure design is not required for this review.

### J13-5 — Eligibility and availability precede charging

The review identifies the after-payment photo check/refund path in `UX-2` as incompatible with the approved pre-payment material/condition check. It also identifies that the `UX-1` suede/leather options must not progress to chargeable intake under the current offer merely because an agent might contact the customer later.

It states the required ordering in observable terms: establish supported service/material and available pair capacity, show agreed total and return promise, then collect payment and confirm on success. It does not characterize drafted screens as a reproduced runtime bug, or use the existence of refunds to justify charging an ineligible order.

### J13-6 — The review is bounded, grounded, and usable

Material findings identify affected artifact/section, conflicting fact, customer consequence, priority, and a minimal correction or release check. The review makes clear which issues prevent opening paid intake and groups cross-document changes where useful. It stays within claims, application flow, pricing, and fulfillment rather than producing a new product strategy, full PRD, unrelated security audit, or implementation.

It respects the source hierarchy: adopted `OPS-0910` controls the paid pilot; old doorstep/next-day free-trial observations and later unapproved design text do not override it. It leaves delay compensation unresolved rather than inventing an approved amount, policy, or legal requirement. It does not say the existing FAQ already promises compensation: it explicitly leaves that text pending. It does not claim to have changed files, contacted customers, or tested real payment. Workspace integrity is assessed separately.

## P1 diagnostic criterion

### J13-7 — Correct elements and open decisions survive the review

The review explicitly retains or recognizes at least two meaningful correct parts, such as the landing page's locker scope/return time, 1–2 pair limit, next-session selection, no-subscription arrangement, refund-before-pickup wording, or Thursday delay notice. It clearly separates an optional clarity improvement or unresolved compensation question from a proven conflict. It need not enumerate every correct sentence.

## Grading exclusions

Do not demand an exhaustive state machine, code, visual mockups, a third-party legal opinion, market research, an invented refund SLA, a new compensation policy, or discussion of unrelated business risks. Different severity names and table layouts are acceptable when the review makes the release implications clear. A correct finding is not weakened merely because a reviewer chooses to combine related IDs in one row.
