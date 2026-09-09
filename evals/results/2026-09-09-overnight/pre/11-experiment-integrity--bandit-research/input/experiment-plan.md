# FlowCart checkout experiment — EXP-CHECKOUT-7

Synthetic fixture. Every product, person, event, export, and observation in this
case is fictional, including the CSV files under `exports/`. They are supplied
planning inputs, not evidence about real customers.

Adopted by the product owner on 2026-09-04. All dates and times use Asia/Seoul.

## Product and assignment

FlowCart sells one-off digital design packs. Signed-in customers currently use
checkout A, which shows the order summary above the payment form. Checkout B
adds an interactive pack preview beside that form. Prices, payment provider,
catalogue, and purchase entitlement are the same in both variants.

Eligible accounts are signed-in customers entering checkout for the first time
during enrollment. Assignment is made on the server before rendering checkout,
using blocks of 20 eligible accounts with 10 assigned to each variant in random
order. The stable account ID retains its first assignment across visits and
devices. There is no reassignment. The assignment log records every allocation.

Enrollment starts 2026-09-05 09:00 and ends 2026-09-19 09:00, exclusive. Existing
participants retain their assigned variant during follow-up unless a safety
pause requires routing them to A; any such routing must be recorded.

## Outcomes and decision schedule

Primary outcome: the proportion of assigned accounts with at least one
successful purchase within seven full days after their first assignment.
Count an account once, regardless of repeat purchases or browser events. The
payment service's receipt records are the outcome source. Analyze all assigned
accounts under their original allocation, including those without a browser
exposure event. The final scheduled efficacy review is 2026-09-26 09:00.

The ordinary dashboard may be viewed for operations. This plan has no sequential
efficacy boundary or rule authorizing an early winner from dashboard changes.

Ongoing guardrail: accounts contacting support about being unable to complete
checkout, divided by all assigned accounts in that variant, cumulatively since
assignment. Count each account once. Once a variant has at least 500 assigned
accounts, a rate above 1.0% requires pausing new assignments to that variant and
investigating; its current participants can use A so they can finish buying.
The product owner adopted this operating limit based on available support
capacity. A higher purchase dashboard value does not waive the pause rule.

## Current data delivery

The attached exports all cover enrollment start through 2026-09-08 09:00,
exclusive. Export time is 2026-09-08 09:00. No later records are supplied.
No variant has been paused or rerouted during this window.

- [Assignment export](exports/assignments.csv): new accounts allocated in each
  non-overlapping interval, from the complete server assignment log.
- [Client export](exports/client-events.csv): raw collector deliveries and
  distinct IDs over the entire current window, for assigned accounts only.
- [Backend export](exports/backend-outcomes.csv): complete payment receipts and
  support records joined to the assignment log by account ID, including accounts
  without a browser exposure event. There is no known missing interval in either
  backend source. Each paid account currently has one successful order.

Field definitions are in [instrumentation](instrumentation.md). The
[PM note](pm-note.md) records the request raised after this export.
