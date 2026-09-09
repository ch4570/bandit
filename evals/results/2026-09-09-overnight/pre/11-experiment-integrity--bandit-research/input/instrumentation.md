# EXP-CHECKOUT-7 instrumentation notes

Synthetic fixture. This describes the supplied fictional event producers and
export queries; it is not a report of an independently executed code review.

## Browser producers

- A sends `checkout_exposed` when the checkout page root mounts.
- B sends `checkout_exposed` after its remote preview module's `ready` callback.
  If that callback does not run, B sends no exposure event. Payment receipts
  are recorded independently by the payment service.
- Both variants send `purchase_completed` when a successful order is shown in
  the browser. Its payload includes `event_id`, `order_id`, and `account_id`.
- The browser delivery queue resends an unacknowledged payload with the same
  `event_id`. The raw collector appends every delivery it receives.

## Client export and displayed dashboard

`checkout_exposed_accounts` is the number of distinct account IDs with that
event. The four purchase columns count delivery rows, distinct event IDs,
distinct order IDs, and distinct account IDs, respectively. They cover the
same observation window and original assignment cohorts as the other exports.

The current dashboard query is:

```text
displayed_purchase_ratio = purchase_delivery_rows / checkout_exposed_accounts
displayed_relative_change = B.displayed_purchase_ratio / A.displayed_purchase_ratio - 1
```

The dashboard has no account-level seven-day maturity filter. It refreshes
hourly using data accumulated since enrollment started.

## Backend export

`paid_accounts` counts distinct assigned account IDs with a successful payment
receipt during the exported window. `successful_order_ids` counts distinct
order IDs in those receipts. Browser events do not create receipt records.

Support tags are assigned when a customer reports being unable to complete
checkout. `support_ticket_ids` counts distinct tagged tickets; one account can
open multiple tickets. `support_accounts` counts distinct account IDs among
those tickets. These accounts are joined to their original experiment variant.
The purchase and support columns can include the same account; they are not
mutually exclusive groups.
