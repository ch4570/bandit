# Reschedule handoff development check

Written before the first run. Synthetic, author-designed diagnostic case, not
a hidden benchmark. Give only raw case files and the skill to the task agent.
Grade pass/partial/fail using meaning and source locators, preserving failures.

1. Adopted policy wins over unadopted draft: original booking survives selection,
   hold expiry, lost target and failure; successful replacement confirms the new
   slot and releases the old together. The existing prepaid entitlement follows
   success. No cancellation-first current requirement remains.
2. Distinguishes browsing, target hold, original booking and replacement. Defines
   owner authorization, server-authoritative two-minute expiry (including exact
   boundary), 24-hour change eligibility and timezone display. Proposed rules
   are distinguished from adopted policy.
3. Provides consistent outcomes for competing customers, two tabs for one owner,
   stale booking state, and lost success response/retry. A delayed action cannot
   silently replace a newer booking or create a second one. Technical mechanisms
   may remain flexible, but actual booking state must be discoverable.
4. Gives observable success, expiry, contention, stale tab and lost-response
   acceptance scenarios as planned, honors excluded features, and does not
   invent observed concurrency behavior or a guaranteed five-day delivery.
