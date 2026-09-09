# HoldHarbor PRD — automated pickup SMS queue

Synthetic fixture: the library, policies, and records are fictional.

## Purpose and release decision

Help readers collect ready holds while making SMS work visible to staff. Nora approved replacing manual texts with an automated Ready-triggered queue; she has not chosen enrollment availability or promised pickup improvement.

**Recommendation:** continue with the original 50 readers next release; do not yet offer enrollment to all 250 cardholders. This is the proposed release boundary, not an adopted policy. Enrollment remains optional within that cohort, including readers without a current hold. The other 200 retain existing services. Unknown enrollment demand and exception effort make branch-wide availability unjustified within the supervisor’s 90-minute total SMS budget next week.

## Evidence and interpretation

The [pilot record](../pilot-notes.md) and [outcome export](../reader-outcomes.csv) cover August 3–30: 50 desk-recruited, nonrandom readers; only each reader’s first ready hold was followed. All 30 index holds had mature, desk-reconciled outcomes; the remaining 20 had no pickup opportunity, not failed or missing outcomes.

| Reader group | Readers/ready holds | Delivered | Within 72h | Before expiry |
|---|---:|---:|---:|---:|
| Consented, confirmed, delivered | 14/14 | 14 | 12 | 13 |
| Consented, confirmed, delivery failed | 4/4 | 0 | 1 | 2 |
| No consent | 7/7 | 0 | 3 | 5 |
| Consented, phone unconfirmed | 5/5 | 0 | 2 | 3 |
| No ready hold | 20/0 | 0 | NA | NA |

Delivery reached 14/18 send-eligible readers (78%), 14/30 with an opportunity (47%), and 14/50 participants (28%). Among delivered readers, 12/14 collected early and 13/14 before expiry. Across opportunities, 18/30 collected early, 23/30 before expiry, and 7/30 remained unclaimed. Early collections are included in before-expiry counts. All ready holds received email; delivery does not prove reading. Selection and unassigned comparison groups prevent causal attribution to SMS or extrapolation to 250. H1 remains plausible, without an adopted numeric threshold. The circulation lead favors expansion; the supervisor highlights absent opportunities and reach failures. Neither observation changes policy.

## Preserved authority and requirements

Nora’s August 1 rules remain authoritative:

- **D1:** Ready starts a seven-day hold; pickup remains allowed through the deadline. Seventy-two hours measures early pickup, not expiry.
- **D2:** Automatic email continues for every ready hold. SMS requires explicit consent and a confirmed number; consent is withdrawable. Neither replaces account authentication.
- **D3:** SMS contains only a generic ready-hold notice and sign-in link, never titles or borrower details. Readers access only their own holds; authenticated branch staff manage this branch’s holds.

Staff retain Ready, Collected, Cancelled, and Expired states. Collection requires the existing desk scan; opening links or signing in cannot collect. The hold page retains deadline and state from existing services without changing either.

Proposed defaults: enqueue one initial SMS per eligible hold’s Ready event, restricted to the 50-reader cohort. No periodic reminders or enrollment-triggered backfill. No ready event means no message. Show staff why a hold lacks SMS eligibility; never solicit consent through an unauthorized text.

Persist a unique hold-notice record to suppress repeated events. Recheck consent, confirmed number, cohort, and active hold immediately before submission; withdrawal, collection, cancellation, or expiry suppress unsent work. Already submitted messages may be impossible to recall.

Staff see waiting, delivered, failed, or unresolved status, timestamps, suppression reasons, and next action. Store provider message IDs and reconcile status through lookup. Pending provider delivery stays unresolved until confirmed. A lost submission response is unresolved, never automatically resubmitted: provider duplicate behavior is unverified. Retry only after verified nonacceptance and eligibility recheck. Email continues during exceptions. Reader-facing SMS status is deferred.

## Delivery, rollout, and checks

One developer has five days including verification and fixes. First estimate queue, staff view, and checks; if they exceed capacity, delay activation. Reuse existing services/provider; exclude mobile apps, other branches, marketing, and policy changes.

Proposed supervisor budget: 30 minutes enrollment help, 45 exceptions, 15 follow-up. Log actual effort; at capacity pause new enrollment and SMS dispatch, retain email, and review unresolved work. Expand only after reviewing measured support demand, reach, and queue reliability against available staffing.

V1/V2 reportedly passed in August 2 staging: Ready-to-Collected, seven-day expiry, unchanged collection after email-link opening, and denial of another reader’s details; not a production privacy audit. V3 remains unimplemented/untested. Before activation verify those regressions plus cohort exclusion, eligibility, withdrawal while queued, terminal-state suppression, duplicate events, failed delivery, lost responses without resend, status lookup, and staff visibility. Operational pilot outcomes are not acceptance results.
