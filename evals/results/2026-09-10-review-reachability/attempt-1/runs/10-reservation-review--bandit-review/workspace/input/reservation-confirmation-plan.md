# Synthetic reservation-confirmation plan

Draft for engineering review, 2026-09-18. The pilot serves existing invited workspaces and
uses [the adopted offer-response policy](policy/offer-acceptance.md). Offers and organizer
assignments already exist. No payments, public signup, or changes to studio opening hours
are included. The examples use invented reservations and accounts.

## Organizer flow

The detail page shows the latest published offer and its revision ID. An organizer presses
“Accept offer.” The client sends the reservation ID and displayed revision ID. If the
request times out, the client retries that payload when the organizer presses the button
again. It also keeps the original request payload until a successful response arrives.

## Proposed endpoint behavior

`POST /reservations/{id}/accept` takes `revision_id` from the request body. Authentication
provides `member_id`, `workspace_id`, and active-membership status.

1. Require active membership and confirm that the reservation belongs to that workspace.
2. Look for an acceptance by this member for this reservation. If one exists, return its
   stored revision and state with HTTP 200. This lookup runs before revision validation.
3. Otherwise reject a revision that differs from the latest published offer. Insert an
   acceptance containing the member, reservation, submitted revision, and state `accepted`.
4. Publish `ApplyAcceptance` to the room-ledger queue. Return HTTP 200 if publication succeeds;
   return HTTP 503 if publication raises an error. The acceptance insert is already committed.

The acceptance table has one row per `(reservation_id, member_id)`. There is no organizer
assignment check after the membership and workspace checks above. No handler updates that
row merely because a manager publishes a later offer revision.

## Ledger and operations

The ledger consumer marks the room allocation once it receives `ApplyAcceptance`. Its own
event-ID deduplication is implemented. A failed queue publication does not persist an event
for later sending, and there is no scheduled publisher. The status endpoint reads the
acceptance row; the proposed interface labels an `accepted` row “Room secured.”

An operator can search acceptance rows and ledger allocations by reservation ID, but this
plan adds no repair action. The withdrawal endpoint and its acceptance criteria remain
unwritten pending the operations decision. The team expects to review this plan before
adding either endpoint to the pilot.
