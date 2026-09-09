# BorrowBox instant reservations — synthetic PRD

Version 0.2, drafted 2026-08-20. This document describes an invented neighborhood tool-lending
cooperative. The following was the approved planning direction on that date.

## Goal and audience

Let any resident reserve one of 40 tool types for same-day pickup from East or West depot.
An instant confirmation should remove the need to telephone staff. New visitors can create
an account during checkout; returning members use their existing account.

## Evidence and decisions

On 2026-08-14, seven of ten existing members in a staff-assisted paper exercise said they
would like to choose a confirmed pickup slot. Staff checked tool availability manually
during that exercise. No unattended reservation flow or deposit payment was tested.

On 2026-08-20, the planning group chose an instant-confirmation concept that assumed a
partner inventory API and a refundable deposit integration would be available. The group
had not tested those integrations or a public self-service signup flow.

## Primary flow

1. Visitor creates an account or signs in.
2. Visitor selects a tool, depot, and pickup slot from live partner inventory.
3. The system authorizes a refundable deposit and reserves the tool immediately.
4. The system shows “Confirmed” and emails a confirmation containing the pickup location.
5. A member can cancel in the account page; the tool is released and the deposit is voided.

## Requirements

- Show all 40 tool types at East and West. Refresh availability from the partner API at
  least once per minute; a reserved unit cannot be sold or reserved elsewhere.
- Confirmation normally takes under five seconds. Staff approval is not required.
- If payment authorization fails, do not reserve the tool. Allow retrying the payment.
- Prevent duplicate payment authorizations if the visitor retries a timed-out request.
- Automatically cancel an uncollected reservation after 48 hours and refund the deposit.
- Let staff see confirmed reservations and mark tools as collected or returned.

## Acceptance examples

- Given a new visitor and an available tool, when checkout and deposit authorization
  succeed, then a confirmed reservation and pickup instructions appear within five seconds.
- Given a confirmed reservation, when the member cancels, then stock becomes available
  immediately and the deposit is voided.
- Given a partner inventory timeout, when the visitor checks availability, then show a
  retry message and do not charge a deposit.

## Launch and measurement

Launch public signup at both depots with 40 tool types. Track checkout completion,
payment failures, and reservations per active visitor. The initial aspiration is a 20%
increase in weekly pickups; the paper exercise did not establish a baseline or effect size.

## Open questions

Partner API delivery date, deposit provider readiness, support staffing, and the policy
for tools that are reserved but not collected remain unconfirmed.
