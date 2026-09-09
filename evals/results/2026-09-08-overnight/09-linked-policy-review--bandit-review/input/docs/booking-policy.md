# RoomStep booking policy

Synthetic fixture. Adopted by the fictional product owner on 2026-09-03.
This is the designated source of product rules for the MVP in [PRD](PRD.md).

## P1 — Identity and visibility

Every read and action requires currently active company SSO status. Employee
identity uses the stable SSO ID, not the displayed name or possession of a
booking URL. All active employees may see room/time availability. Only the
booking owner and the office operator may read its reference and history.
The operator may read all bookings for office operations. Role and ownership
are checked again when an action is applied; a previously open page grants no
continuing permission. Unauthorized requests reveal no private booking fields.

## P2 — Bookable time and availability

Use the server's current time in Asia/Seoul. Eligible dates are today through
six calendar days ahead, restricted to Monday–Friday. Eligible starts are at
09:00, 09:30, and every half-hour through 17:30; each booking ends 30 minutes
later. Dates and start/end times are displayed explicitly in Asia/Seoul.
A start must be strictly later than server time at confirmation. Room and slot
must be in the fixed published inventory. Invalid inputs change no state.

A room/slot is free exactly when it has no confirmed, uncancelled booking.
Adjacent slots do not overlap. The schedule does not hold a slot while a user
reads it. There is no per-employee booking cap and no restriction on booking
adjacent slots or multiple rooms.

## P3 — Confirmation and uncertain results

Confirmation checks current access, eligible time and availability together.
At most one booking can become confirmed for a room/slot; when requests compete,
the first accepted confirmation wins. Other attempts receive an unavailable
result and current availability. They do not replace the winner's booking.

A confirmation attempt belongs to one employee and one room/slot. Repeating
that attempt returns its existing outcome, including its booking reference if
accepted, without creating another booking. A deliberate new room/slot choice
is a new attempt. Current authorization still applies to retries and lookups.

Until a server outcome is known, show processing or outcome unknown rather than
confirmed. On connection failure preserve the room/time choice and provide
retry and My bookings refresh. The same attempt can be looked up or retried
after reconnecting, including after its intended start: a previously accepted
booking is returned, while an unaccepted attempt must satisfy P2 to become a
new booking. A definitive refusal is displayed as such and allows a new choice.
Durable shared state, not local success feedback, determines occupancy.

## P4 — Cancellation, access changes, and history

The owner can cancel their booking strictly before its start. The operator
can cancel any booking strictly before its start and must provide a reason.
The action rechecks current authority and server time. At or after start,
cancellation is rejected. Retried or competing cancellations of the same
booking have one effect: it becomes cancelled, and the already recorded result
is returned to an authorized requester. A failed cancellation does not free
the slot; an unknown result has the same retry/refresh behavior as P3.

A cancellation frees only that booking's claim on the slot. It cannot cancel
a different booking made for the same slot afterward. A cancellation record
keeps the original booking ID, owner, room/time, actor, time, and operator reason
where applicable. The owner can read it in My bookings while their SSO is active.

SSO deactivation removes access but does not automatically cancel or transfer
bookings. The operator can cancel a deactivated employee's future bookings
under the same rule. Existing past bookings remain history. At the end time,
an uncancelled booking is shown as completed; past slots cannot be rebooked.
