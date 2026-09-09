# Library pickup-reminder forward development check

Written before the first TASK run. This is a synthetic, author-designed forward
test, not a held-out benchmark or proof of general reliability. Supply only the
raw request, existing `docs/PRD.md`, pilot notes, CSV, and selected instruction snapshot
to TASK agents. Keep this rubric, author analysis, prior outputs, and historical
case scores outside their context. Record the raw/rubric digests before running;
preserve the complete output before grading. Do not change historical grades
or soften these criteria after observing an answer.

Grade each criterion pass, partial, or fail by meaning, with concrete locators.
This is a PRD task: reward usable product decisions and requirements, not a
worksheet or a fixed list of ratios. Report material issues beyond the rubric
separately. Either rollout recommendation can pass if supported and coherent.

## 19 — Library pickup reminders

1. Rewrites the actual `input/docs/PRD.md` into one coherent current PRD around
   the adopted automated, staff-visible
   SMS queue and explicitly recommends an initial availability boundary: the
   original 50 or all 250 cardholders, potentially with a clearly proposed
   staged admission policy. Turns that choice into requirements and rollout
   behavior rather than leaving an evidence memo beside an unchanged v1.
   Preserves mandatory email, optional consent plus confirmed phone, own-reader
   versus branch-staff access, generic SMS content, and the existing desk scan
   as collection authority. Does not make the 72-hour measurement target a new
   expiry rule: the adopted hold remains available for seven days. Small
   delegated defaults may be proposed, not silently attributed to Nora.
2. Interprets the evidence at the level needed for the rollout choice. Separates
   pickup among SMS-reached readers from coverage of readers with an opportunity
   and the whole pilot population. The underlying records are 50 readers, 30
   with a ready index hold, 14 reached by SMS, and 12 early pickups among those
   14; the whole opportunity group had 18 early pickups and 23 before expiry.
   These facts do not establish the same outcome rate for all 50 or the proposed
   250. Clear counts, prose, or appropriately labeled rates can satisfy this;
   there is no required menu of fractions, every subgroup sum, or specific table.
   Does not count the 20 without a ready hold as failed pickups, confuse reach
   with pickup, add overlapping early/final pickup columns, or treat the 200
   unobserved cardholders as known eligible opportunities. Does not infer an
   SMS-caused lift from the selected delivered group: all ready holds also had
   email and exposure was not randomized. Uncertainty must inform the decision,
   not merely appear as a disclaimer after an unsupported rollout claim.
3. Specifies the complete retained notification-to-pickup path at useful PRD
   resolution: Ready creates eligible queue work; consent, phone readiness,
   current hold state, and access rules govern sending; the reader can find
   the actual deadline/state; staff can distinguish delivered, failed, and
   unresolved notification outcomes from collection. Gives a workable response
   to cancellation/collection/expiry or consent withdrawal before a queued send.
   A lost provider response or retry must not silently imply delivery or create
   uncontrolled duplicates. May defer an uncertain retry to bounded staff
   review while preserving email, rather than invent verified provider features
   or prescribe infrastructure. The PRD need not specify every technical race
   or a full provider integration design to be implementable at this stage.
4. Makes a defensible tradeoff about availability, support, and what remains
   unknown. Wider optional enrollment is not automatically wrong; narrower
   continuation is not automatically justified by counting no-opportunity
   readers as failures. Accounts for the five developer-days including checks
   and fixes, and the 90-minute shared SMS-support/follow-up allowance without
   inventing measured estimates or an unlimited manual rescue path. Gives a
   meaningful scope or operating bound consistent with its recommendation and
   identifies an economical next observation plus a condition that could reopen
   it. That observation must connect to a material unknown such as consent/phone
   coverage, actual delivery and pickup in a defined opportunity window, or
   exception workload. No prescribed sample, conversion target, or rollout
   verdict is required. Future delivery, uptake, and time savings remain open.
5. Preserves original evidence and authority while replacing obsolete manual
   workflow requirements. Retains H1 as an unproven benefit hypothesis; preserves
   V1/V2 as reported passes under their original v1 staging conditions, not
   evidence that the SMS queue or production behavior passed. Manual pilot
   records remain operational observations. Gives planned, observable checks
   for the new queue's ordinary outcome and material permission, stale-state,
   consent, and uncertain-send cases; does not mark them executed. Answers in
   English as a useful current PRD and gives a short final summary. Count the
   complete edited `input/docs/PRD.md`, not the final summary, against the
   800-whitespace-delimited-word cap. Only that PRD may change; all other raw
   inputs and instruction files remain byte-identical. Uses only supplied
   evidence and performs no external actions, implementation, or product-test
   execution. Artifact editing and read-only arithmetic are allowed.

## Design distinction and limits

The domain is a library's physical hold-pickup service, not quote approval or
collaborative editing. Opportunity is a ready hold, SMS reach requires consent,
phone readiness, and actual delivery, and collection is a separate staff-recorded
outcome. Whole-population availability also concerns readers who had no hold
this month and an unobserved extension beyond the pilot. The task asks for an
operational PRD update under adopted service policies, not a pricing comparison,
an onboarding feature ranking, or a demonstration of all calculable percentages.

The rubric assesses whether population conditioning changes the substance of
the recommendation and its requirements. It does not turn an omitted redundant
ratio into an automatic defect when the material meaning is already clear.
Results will remain synthetic development observations, without superiority,
instruction-caused improvement, or population-level reliability claims.
