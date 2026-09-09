# Synthetic operating facts for the 2026-09 pilot

Both depots are staffed Tuesday–Saturday, 10:00–18:00 Asia/Seoul. Requests are accepted
outside staffed hours. The operator commitment is an approval or decline within two staffed
hours: count only time inside those opening intervals. Staff can respond earlier.

An inventory CSV is exported each morning at 08:00. It identifies the pilot tool types and
depot, but its availability counts can be stale; the local ledger is authoritative for
approval. If the latest successful import is more than 24 hours old, block new requests
for that depot and explain that its availability needs refreshing. Existing request status
must remain readable. A refresh must not erase existing requests.

Members have stable IDs and verified status in the existing member database. The pilot
must use that status and its invitation list; it cannot create or verify new accounts.
Members may see their own requests. Depot operators may see and decide requests for their
assigned depot. Being signed in alone does not grant access to another member's request.

The request store is available. The interface must make a timed-out submission safe to
retry without creating a second logical request. The existing email adapter is available
but can fail; on-screen request status is authoritative. An email failure must not erase
the recorded staff decision or change an approval into a decline. Operators need to see
which notification needs retrying. A member withdrawing a pending request while an operator
approves it must end with one unambiguous decision and a clear response to the losing action.

There is no payment provider, real-time inventory adapter, SMS channel, public registration,
or automated tool-lock control available for this pilot. Product has not chosen a future
deposit amount or a policy for noncollection; those are not implementation decisions for
the current team.
