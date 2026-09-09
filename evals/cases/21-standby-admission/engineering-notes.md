# Planning notes — October 12, 2026

Developer Imani estimated the following work against the existing service.
These are additive point estimates, not measured delivery results. Each build
item includes its own ordinary checks; integrated verification is separate.
There is no contingency or allowance for fixes found during integration.
Fewer offers reduce operating volume, not these shared implementation tasks.

| Item | Engineering hours | Included result |
| --- | ---: | --- |
| Offer claim and status | 6 | Named-member access, assignment/withdrawal, saved acceptance, duplicate/lost-response recovery; no closing or admission-roster update |
| Close and publish | 5 | Deadline handling, pending-response settlement, confirmed-roster update and current gate view; depends on claim/status |
| Integrated verification | 3 | Retained production journey, closing races, withdrawal, role access and gate consistency; includes a 20-minute coordinator walkthrough |
| Plain reply export | 2 | Download existing form rows; no seat decisions, closing, reconciliation, or gate integration |
| Non-production walkthrough prototype | 2 | Scripted offer/status/closing screens in the existing mockup tool, including a 20-minute coordinator review; cannot send real offers or confirm seats |

The form CSV could be reconciled manually with the confirmed roster after
closing. Leah estimates 15 minutes to check the eight offer outcomes plus
five minutes per uncertain response or withdrawal, before publishing the
updated roster. A noon export cannot contain the evening replies. No timed
end-to-end manual rehearsal or production implementation has occurred.
