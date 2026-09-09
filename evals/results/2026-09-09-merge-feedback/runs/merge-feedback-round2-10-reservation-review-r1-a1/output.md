The draft needs bounded corrections before pilot inclusion: it permits unauthorized acceptance, conflates responses across offer revisions, and can report a secured room after ledger delivery fails.

This is a document-only review of `reservation-confirmation-plan.md`, its adopted policy, and `community-notice.md`. The notice is outside the pilot’s scope. No files were changed and no code or tests were executed; the checks below are proposed, not verified results.

1. **Enforce the assigned-organizer rule.**

   **Adopted rule:** Only the assigned organizer may accept; active membership is necessary but insufficient, and managers cannot accept on their behalf (`policy/offer-acceptance.md:10–13`).

   **Plan conflict:** The endpoint checks membership and workspace ownership but explicitly omits organizer assignment (`reservation-confirmation-plan.md:20–30`).

   **Scenario and consequence:** Another active member—or a manager—submits the current revision for a reservation in their workspace. The proposed endpoint records agreement without the organizer’s authority.

   **Bounded correction and acceptance check:** Check organizer assignment before returning or creating an acceptance. Given an active, same-workspace member who is not the assigned organizer, an acceptance request must be denied without creating an acceptance or publishing a ledger event. Include a manager in that check. An active assigned organizer can proceed with the current revision. This implements an adopted rule; no new permissions decision is needed.

2. **Separate exact retries from acceptance of a changed offer.**

   **Adopted rule:** The same organizer, reservation, and revision constitute one logical action. A new revision requires fresh review and acceptance; requests naming superseded revisions must explain the change and must not accept them (`policy/offer-acceptance.md:15–19`).

   **Plan conflict:** Existing responses are found by member and reservation before revision validation, and only one row exists for that pair (`reservation-confirmation-plan.md:21–30`). The client also retains and retries the original payload until success (`:10–13`).

   **Scenario and consequence:** After revision A is accepted, a manager publishes B. Accepting B returns A’s stored acceptance instead of recording agreement to B. Retrying A also returns success without explaining that the offer changed. A retained stale payload can prevent the organizer from completing the required fresh review.

   **Bounded correction and acceptance checks:** Make duplicate detection revision-aware and enforce the superseded-revision rule before treating a request as successful. The storage design can remain an engineering choice, provided agreement remains attributable to its revision.
   
   - Repeating acceptance of current revision A, including after a lost response, produces one logical acceptance.
   - Once B is published, submitting A explains the change and creates no acceptance for B.
   - After reviewing B, the organizer submits B and receives a result attributable to B; A is not carried forward.
   
   Update client recovery so a changed-offer response enables review and submission of the latest revision rather than indefinite replay of A.

3. **Distinguish recorded agreement from allocation and provide recoverable delivery.**

   **Adopted rule:** Acceptance and room allocation are separate states; only the ledger establishes “Room secured” (`policy/offer-acceptance.md:21–23`).

   **Plan conflict:** The acceptance commits before publication; a publication error returns 503 without durable resend work. A retry returns the existing row without republishing. Status nevertheless labels that row “Room secured” (`reservation-confirmation-plan.md:21–26, 34–40`).

   **Scenario and consequence:** Publication fails after commit. The organizer retries and receives success, but the ledger never allocates the room. Search-only operator access supplies no repair path. Even successful publication does not prove ledger application.

   **Bounded correction and acceptance check:** Show “Response received” until ledger-confirmed allocation. Specify a recoverable delivery path, such as durable retryable publication or an explicit operator repair action; implementation details need not become product policy. Simulate interruption after acceptance commit and before confirmed delivery: status must not claim allocation, retry must preserve one logical acceptance, and recovery must eventually apply it without duplicate allocation. Consumer deduplication alone does not recover an event never delivered.

**Decision still owned by Operations:** Withdrawal while ledger application is pending remains explicitly unresolved (`policy/offer-acceptance.md:25–27`; plan `:40–42`). This is a declared decision, not an omitted adopted rule. Before including withdrawal, Operations must choose its interaction with pending application. Then check withdrawal followed by late delivery: if withdrawal cancels pending allocation, delivery must not secure the room; if cancellation is unavailable at that stage, the interface must explain that outcome without claiming release.

The next useful step is to reconcile these three conflicts in the plan and use the proposed scenarios for implementation verification. The supplied documents establish intended and proposed behavior, not working software or demonstrated pilot readiness.