The draft has material conflicts with the adopted policy in permissions, revision handling, and recovery. Resolve these before pilot approval. The withdrawal rule is explicitly undecided; it should remain an Operations decision.

Reviewed `input/reservation-confirmation-plan.md`, its adopted policy `input/policy/offer-acceptance.md`, and `input/community-notice.md`. The notice adds no applicable reservation rules. This is document inspection only: no implementation, tests, runtime results, or customer evidence were supplied or exercised.

1. **Workspace membership incorrectly grants acceptance authority.**

   **Sources:** Plan, “Proposed endpoint behavior,” steps 1–3 and its closing paragraph; policy, organizer permissions paragraph.

   **Scenario and consequence:** An active workspace member who is not the assigned organizer—including a manager—submits the current revision. The proposed checks permit an acceptance that the policy reserves for the assigned organizer.

   **Bounded correction:** Require the assigned-organizer check alongside active membership and workspace ownership, before accepting or treating the request as a successful repeat.

   **Acceptance checks:** For a current revision, the active assigned organizer can accept; another member and a manager cannot accept on their behalf. Inactive members and members of another workspace cannot accept. Denied requests create no acceptance or allocation work.

2. **The repeat-action rule conflates different revisions and bypasses stale-offer rejection.**

   **Sources:** Plan, “Organizer flow,” “Proposed endpoint behavior,” steps 2–3 and the one-row constraint; policy, revision and repeat-action paragraphs.

   **Scenario and consequence:** An organizer accepts revision A, then a manager publishes B. Submitting B returns A’s stored acceptance instead of recording agreement to B. Retrying retained payload A also returns success before checking whether A is superseded. This prevents renewed consent and fails to explain that the offer changed.

   **Adopted rule:** The logical action is the same organizer, reservation, and revision. Agreement does not carry forward; a superseded revision must be rejected with an offer-changed explanation. This rule is already decided.

   **Bounded correction:** Make revision part of acceptance identity and apply the superseded-revision rule before returning repeat success. After an offer-changed response, replace the retained retry flow with review of the latest offer and explicit acceptance.

   **Acceptance checks:** Repeating A while A remains current produces one logical acceptance, including after a lost response. Once B is published, submitting A explains the change without accepting it; reviewing and accepting B records agreement to B, not a replay of A.

3. **A publication failure can strand an acceptance while retries report success.**

   **Sources:** Plan, endpoint steps 2 and 4; “Ledger and operations.”

   **Scenario and consequence:** The acceptance commits, queue publication fails, and the endpoint returns 503. A retry finds the stored row and returns 200 without publishing. There is no persisted delivery work, scheduled publisher, or repair action. The ledger may never receive the acceptance, and operator search alone cannot recover it.

   **Bounded correction:** Specify a recoverable path from committed acceptance to ledger application, such as durable pending delivery with retry, or an explicit operator repair mechanism. Preserve one logical action during recovery; the particular implementation is an engineering choice.

   **Acceptance checks:** Interrupt processing after commit but before successful publication, then retry and invoke the chosen recovery path. The acceptance remains visible as pending, eventually reaches the ledger, and results in one allocation effect despite duplicate delivery. Consumer deduplication alone does not establish this recovery.

4. **“Room secured” is displayed before authoritative allocation.**

   **Sources:** Plan, “Ledger and operations”; policy, separate acceptance/allocation states paragraph.

   **Scenario and consequence:** Queue processing is delayed or publication fails, but the status endpoint reads the committed `accepted` row and displays “Room secured.” Members may rely on a room that has not been allocated.

   **Bounded correction and acceptance checks:** Display “Response received” after acceptance recording and throughout delivery delays or failures. Display “Room secured” only when ledger evidence confirms application of the relevant acceptance. Successful queue publication alone must not change that label.

Operations still owns **withdrawal while application is pending** (policy, final paragraph; plan, “Ledger and operations”). Before including withdrawal, record the adopted outcome and checks for withdrawal before delivery and racing with application. If withdrawal wins, verify that delayed delivery cannot secure the room contrary to that decision; if application wins, verify withdrawal clearly reports that outcome. Do not infer automatic release.

Next, reconcile the draft with these adopted rules and select a recovery mechanism; then execute the proposed checks. None is currently a verified pass.