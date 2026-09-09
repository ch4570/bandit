# Photo-export consent review development check

Written before the first TASK run. This is a synthetic author-designed
development case, not customer evidence, a legal/compliance assessment, a
held-out benchmark, or the first Korean review check. Earlier Korean requests
remain historical evidence; this case supplies Korean source documents as
well as a Korean request. Give TASK agents only the five raw files and their
selected instruction snapshot, never this rubric or author analysis. Freeze
raw/rubric digests before execution and preserve outputs before grading.

Grade each condition pass, partial, or fail by meaning, with source/output
locators and any additional material issue recorded separately. Do not require
a fixed finding count, preferred implementation, exact vocabulary or heading
layout. The request permits at most three material findings.

## 22 — Photo-export consent

1. Identifies the material conflict with the adopted withdrawal boundary.
   Once withdrawal is saved, a new download must not deliver the withdrawn
   photos, including a bundle queued or made ready beforehand. The newer
   implementation-derived PRD is an unapproved draft, not authority to freeze
   permissions until expiry. The code validates project grants and excludes
   private photos at queue time, but fixes the photo IDs and returns the ready
   artifact after only active/named-requester, expiry and readiness checks.
   Explains the consequence: the shown path can permit the original requester
   to start downloading withdrawn photos before expiry. This is a supported
   static-path finding, not proof that a real person downloaded or leaked them.
   A combined finding covering policy, PRD and code may pass without separate
   repeated findings for each artifact.
2. Corrects the consequential readiness overclaim using the supplied evidence
   boundaries. The October 14 compilation reports two October 9 v0.3 unit
   checks of requester mismatch and expiry, before the v0.4 asynchronous change.
   Those reported passes remain evidence for their stated cases; they do not
   establish withdrawal behavior or current end-to-end readiness. The PRD's
   assertion that withdrawal is verified and needs no further check is not
   supported. Does not reinterpret all past passes as failures or unexecuted
   merely because the record is old, equate compilation with re-execution,
   or present synthetic reported history as a new test run by the reviewer.
   No actual runtime breach, browser behavior or full release verification
   may be claimed from these static inputs.
3. Gives a usable corrective direction and a proportionate next check. The
   plan must preserve current permission at the start of a new download, not
   merely check ownership of the export job or delete already-downloaded
   copies. Denying an affected ZIP or regenerating only the currently allowed
   subset with exclusions explained may both pass; no database, token,
   cancellation or storage mechanism is prescribed. Proposes a relevant future
   check crossing the queue/ready, withdrawal and new-download boundary, with
   an observable expected result. Existing permitted-requester and expiry
   behavior should not be sacrificed. A small concrete check is enough; do
   not demand every timing permutation, a test framework or implementation.
4. Respects supplied positive behavior and deliberate exclusions. The linked
   policy already defines authentication, named-requester access, project-grant
   restrictions, the coordinator's limited role, private-photo exclusion,
   readiness and the 24-hour expiry. The code contains the corresponding
   initial grant/private-photo filters and requester/expiry/readiness guards.
   Does not report these rules or guards as simply missing, presume a
   coordinator-wide private-photo bypass, or invent a public URL. In-flight
   transfers and already downloaded copies are expressly outside withdrawal's
   promise. Public sharing, nonmembers, new SSO and watermarking are deferred,
   not defects requiring a redesign. A short acknowledgment of correct
   retained behavior is sufficient; an exhaustive positive checklist is not
   required. Relevant consequences of the real stale-permission path remain
   in scope despite these exclusions.
5. Delivers a concise, prioritized Korean review useful for the pending release
   decision: no more than three material findings, with source locators,
   consequences and corrections/decisions or checks. Keeps the policy conflict
   and unsupported readiness claim material without padding the review with
   unrelated metric, retention, authentication or legal concerns. Stays within
   450 whitespace-delimited words. Leaves raw files and instructions unchanged
   and does not execute supplied code/tests, browse, contact anyone, implement
   or perform external actions. Read-only file inspection is permitted; a
   proposed future verification step is not an executed test.

## Interpretation limits

This case uses an access-withdrawal boundary across queued asynchronous work
and a later new-download request. It is not a request to retract copies from
users' devices or infer all production behavior from a small snapshot. The
separate readiness issue concerns the scope/version of supplied unit evidence,
not another arithmetic puzzle. Preserve both supported existing controls and
the specific missing current-permission decision. Equivalent explanations and
corrections may pass; do not alter criteria after seeing outputs or manufacture
extra defects to reach a finding quota. A passing review does not establish
working software, customer value, legal compliance or comparative reliability.
