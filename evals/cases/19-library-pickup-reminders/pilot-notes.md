# Supplied branch pilot record — 2026-09-09

Synthetic fixture. All counts, statements, and resource limits are fictional.

## Population, opportunity, and outcome records

The branch has 250 active cardholders. Fifty agreed to the August pilot; they
were recruited at the desk and were not randomly selected. The other 200 have
not been surveyed about SMS consent, phone readiness, or their next hold.

The pilot ran August 3–30. `reader-outcomes.csv` has disjoint groups covering all
50 readers. Its unit is a reader, not a message, visit, or book. For a reader
with one or more ready holds, staff followed the first such hold as the index
hold. Later holds are outside this outcome export. Every index hold's seven-day
deadline had passed by the August 30 18:00 UTC export. Staff reconciled desk
scans for every index hold; there are no missing or immature pickup outcomes.

`index_holds_ready` counts readers with that pickup opportunity. A zero in the
no-ready-hold group means no opportunity arose during this window. `NA` in that
group's pickup fields means not applicable, not an unknown or failed pickup.
`sms_delivered_readers` requires provider-confirmed delivery for the index hold;
it does not establish that the reader opened or understood the text.
`pickup_within_72h` counts index holds collected within 72 hours after Ready.
`pickup_before_expiry` includes those early collections and any later collection
before the seven-day deadline; these columns must not be added together.

The consented readers with failed deliveries had confirmed phone numbers but no
confirmed SMS delivery after staff attempts. The no-consent group had not opted
in. The phone-unconfirmed group had consented, but staff did not send until the
number was confirmed. All ready index holds also received the ordinary email
notice. Group membership was not randomized. No email-only comparison was
assigned, and the records do not identify which notice prompted a pickup.

The circulation lead says, "Most readers who got the text collected promptly.
I would like this available throughout the branch." The desk supervisor says,
"Some readers never had a ready hold, and others could not be reached by text.
I need to know what the new queue will do for those cases." These are proposals
and observations, not additional adopted policies.

## Adopted next-release direction and constraints

Nora approved replacing manual SMS composition with an automated queue tied to
the existing Ready event. Staff must be able to see when a message is waiting,
delivered, failed, or unresolved and what needs attention. Existing email, desk
collection, account access, and seven-day expiry remain unchanged. This decision
does not adopt SMS for all 250 cardholders or promise any pickup improvement.

One developer has five days, including verification and fixes. Existing account
and hold services, the current SMS provider, and the staff application may be
reused. There are no component estimates yet. New mobile apps, another branch,
marketing texts, and changes to borrowing or expiry policy are outside this work.

The desk supervisor has 90 minutes total next week for SMS enrollment help,
delivery exceptions, and pilot follow-up. Ordinary email and physical pickup
work continue through their existing processes; that time is not an extra SMS
support pool. No other employee can take additional SMS work. Enrollment can be
offered without a promise of an immediate hold, and a smaller continuation is
allowed. No rollout beyond the August pilot has been announced or performed.
