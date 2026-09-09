# RoomStep — internal room booking MVP

Synthetic fixture. This product, organization, policies, and planning records
are fictional development inputs, not real customer or execution evidence.

## Adopted scope — 2026-09-03

An active employee at the Seoul office can view a room's available half-hour
slots, book one, see the confirmed booking, and cancel it before it starts.
There are three fixed rooms. The booking covers the whole room for 30 minutes.
This is a software planning handoff; implementation has not started.

The product owner adopted [booking policy](booking-policy.md) as the authority
for access, time, ownership, state, conflicts, and failure recovery. This PRD
references that policy rather than duplicating each rule.

The existing company SSO supplies the stable employee ID and current active
employee status on every read and action. Its current integration contract is
accepted for this MVP; no account registration or password feature is added.
The office operator also uses that SSO with an operator role.

## Included journey

1. An employee opens the schedule and chooses an eligible room/date/slot.
2. The employee reviews the room and local start/end time, then confirms.
   Availability on the schedule is advisory; confirmation follows policy P3.
3. The result shows the booking reference, room, time, and current state. A
   confirmed booking is visible in My bookings and makes the room unavailable
   to others. Reopening the schedule reads current shared state.
4. My bookings lets the owner cancel before the start, with a confirmation
   step. The operator can cancel under policy P4. The schedule then reflects
   the cancellation; the booking remains in the owner's history.

Included screens are schedule, confirmation/result, and My bookings. Operator
cancellation is a small role-gated action on the same booking view. No other
person's name, meeting title, or purpose is collected or shown in the schedule.

## Boundary and dependencies

The MVP has no booking edit or reschedule promise: an employee may cancel and
try a separate booking, but the new slot is not guaranteed. Recurring bookings,
multiple sites, public guests, payments, calendar integration, waitlists, and
notifications are outside the adopted scope. Users reopen My bookings to check
current status. Operations handles physical access and room equipment through
existing office procedures. The three-room inventory is fixed during this MVP.

[Later discovery notes](discovery-notes.md) are proposals for future iterations.
They do not replace this scope or the adopted booking policy.

## Planned acceptance checks

All checks below are planned and unexecuted. They describe required product
outcomes, not completed verification or a release-readiness claim.

| Check | Action and observable outcome |
| --- | --- |
| A1 | An active employee confirms an eligible free slot: one booking reference appears in My bookings after a reload, and another employee sees that slot as unavailable. |
| A2 | Two employees confirm the same free slot: one confirmed booking exists, and the other sees an unavailable result with an updated schedule. |
| A3 | Confirmation succeeds but its response is lost: retry/reload resolves the same attempt to its recorded booking, with no second booking; no success is shown while its outcome remains unknown. |
| A4 | An owner cancels before the start: the booking is cancelled, its history remains, and another employee can book the slot. Another employee's cancellation attempt changes nothing. |
| A5 | A user with inactive SSO status attempts a read or action: access is denied. Their existing booking follows P4, without silently changing ownership. |
| A6 | Invalid time, past start, or cancellation at/after start is submitted: the action is rejected and current state is shown. Server time and boundary rules follow P2/P4. |
| A7 | An operator cancels a future booking with a reason: the owner sees the cancelled state, reason and actor when reopening My bookings; no notification delivery is implied. |
