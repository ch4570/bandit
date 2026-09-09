# ToolLoop pilot brief

Synthetic fixture. All people, workload samples, estimates, and records below
are fictional; they are task inputs, not real customer or delivery evidence.

## Adopted pilot constraints

- Existing workshop members only; 36 have asked to participate. We can invite
  fewer for the first week. No promise has been made to all 36.
- A confirmed request means that the named tool is reserved for the stated
  pickup and return slot. The member must be told if that promise changes.
- Workshop collection only, weekdays 17:00–18:00. Manager Mina is present for
  that hour and has no additional hours before or after it. No volunteer backup.
- A member may have one active loan. A returned item must be inspected before
  it is available to someone else. Damaged items stay unavailable.
- The workshop already checks member identity and lending eligibility. Keep
  that process. No payments, deposit, delivery, or public signups in the pilot.
- Builder has 5 developer-days until next Friday, including verification.

## Existing tools

- Shared form accepts preferred item, pickup date and return date. Its receipt
  says "request received"; it does not confirm a reservation.
- Private spreadsheet lists member, tool, requested dates, assigned item,
  confirmation sent, pickup, due date, return, inspection outcome and status.
- Mina can update the sheet and send a prepared email to a member. No member
  access to the sheet. The sheet has no automatic conflict detection.
- Four drills and two sanders are individually labeled. A damaged drill is
  awaiting repair and cannot be lent; the other five items are available now.

## Supplied work estimates

Engineering estimates are rough, have no contingency, and assume the existing
membership tool remains unchanged. Build tasks below do not include testing.

| Candidate | Developer-days | Result |
| --- | ---: | --- |
| Member request/status page | 2 | Authenticated request, received/confirmed/unavailable state |
| Availability and confirmation guard | 2 | One reservation per physical item and slot; manager confirms |
| Pickup/return/inspection screen | 2 | Manager updates loan and item state |
| Automatic reminders | 1 | Email before return time |
| Usage dashboard | 1 | Counts and charts |
| Verify retained journey | 1 | Exercise retained flows and recovery with Mina |

## Workload observations

Mina timed six synthetic rehearsals with paper records. Use these as planning
estimates, not proof of steady-state capacity:

| Manual work | Time per action |
| --- | ---: |
| Review request, check overlap and send confirmation/unavailable email | 6 minutes |
| Check identity and record a pickup | 5 minutes |
| Record a return and inspect the item | 7 minutes |
| Notify a member and resolve one late/damaged item affecting the next booking | 10 minutes |

The signup survey's preferred dates imply up to 8 requests, 5 pickups and 5
returns on one day if everyone is admitted. These are different actions and
can occur on the same day. No historical arrival distribution is available.
The request form can be closed or limited to selected members. We have not
tested a daily action cap or appointment slots with members.
