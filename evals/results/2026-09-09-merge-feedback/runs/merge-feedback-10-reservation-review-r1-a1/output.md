The draft needs corrections before pilot inclusion: its proposed behavior conflicts with adopted rules for organizer authority, revision-specific acceptance, and allocation status, and leaves a failed publication without recovery. Withdrawal remains an explicitly pending Operations decision.

Reviewed all four supplied input documents by inspection. The community notice explicitly excludes its signup list from this pilot. References below use paths relative to `input/`. No files were changed; no code or tests were run.

1. **Active membership incorrectly grants acceptance authority.**

   **Adopted rule:** Only the assigned organizer may accept; managers cannot accept on their behalf (`policy/offer-acceptance.md:10–13`).

   **Plan behavior:** The endpoint checks membership and workspace ownership, explicitly omitting organizer assignment (`reservation-confirmation-plan.md:20–30`).

   **Scenario and consequence:** An active colleague or manager submits the current revision for another organizer’s reservation. The proposed checks permit an unauthorized agreement.

   **Bounded correction and acceptance check:** Require the caller to be the reservation’s assigned organizer before accepting or returning an acceptance as a successful action. Check that an active, unassigned member and a manager cannot create an acceptance or trigger ledger application; the assigned, active organizer can proceed for the current revision. Membership and workspace checks remain necessary.

2. **The duplicate lookup conflates exact retries with new or superseded revisions.**

   **Adopted rule:** The same organizer, reservation, and revision define one logical action. A new revision requires fresh review and acceptance; requests naming superseded revisions must explain that the offer changed (`policy/offer-acceptance.md:15–19`).

   **Plan behavior:** Lookup and row uniqueness use only member and reservation, and lookup precedes revision validation (`reservation-confirmation-plan.md:21–30`). The client retains the original payload until success (`:10–13`).

   **Scenarios and consequences:** After accepting revision A, an organizer reviews and submits B but receives A’s stored success. Alternatively, a retained request for A returns success after B is published. The first prevents fresh agreement; the second hides an outdated request.

   **Bounded correction:** Validate the submitted revision against the current offer before duplicate success, and distinguish revision-specific agreements. On an offer-changed response, require review of the latest contents before a fresh submission; do not silently substitute revision IDs.

   **Acceptance checks:** An exact retry while its revision remains current produces one logical acceptance. Submitting reviewed B after A records agreement to B. Submitting superseded A explains the change and creates no new acceptance or allocation action. The adopted policy already determines these outcomes; they do not need a new product decision.

3. **An interrupted publication can leave an acceptance permanently unapplied.**

   **Plan behavior:** The acceptance commits before queue publication. Publication failure returns 503, persists no event for later sending, and has no scheduled publisher. A retry returns the existing row before publication; operators can inspect but cannot repair (`reservation-confirmation-plan.md:21–26,34–40`).

   **Scenario and consequence:** Publication fails after commit. The organizer retries and receives 200, but nothing ensures that the ledger ever receives the acceptance. Consumer event-ID deduplication does not recover an event that was never delivered.

   **Proposed correction:** Add a durable retry or reconciliation path with an operational owner, preserving the same logical ledger action across retries. The specific mechanism is an engineering choice.

   **Acceptance checks:** Interrupt after acceptance commit and before confirmed publication. Recovery must eventually apply the eligible acceptance once, without requiring another agreement. Also check publication with a lost acknowledgement: recovery must not allocate twice. Until application, show the response as received and allocation as pending.

4. **“Room secured” is asserted before authoritative allocation.**

   **Adopted rule:** Acceptance and allocation are separate; the ledger determines whether the room is secured (`policy/offer-acceptance.md:21–23`).

   **Plan behavior:** Status reads the acceptance row and labels `accepted` as “Room secured” (`reservation-confirmation-plan.md:34–37`).

   **Scenario and consequence:** Even successful queue publication can precede ledger processing. During that interval—or publication failure—the organizer receives an unsupported assurance.

   **Correction and acceptance check:** Derive “Room secured” from confirmed ledger application. A committed acceptance with delayed or failed application shows “Response received”; only confirmed allocation shows “Room secured.”

**Pending decision:** Operations must decide withdrawal during pending application, including the outcome when withdrawal and ledger application overlap (`policy/offer-acceptance.md:25–27`). The draft acknowledges this deferral (`reservation-confirmation-plan.md:40–42`); it is not an omitted adopted rule. Resolve and document the outcome before including withdrawal, then add matching acceptance criteria. Do not assume withdrawal wins or automatically releases allocation.

These are document-level findings, not observed failures. Implementation and runtime evidence were unavailable. The next useful step is to revise the bounded behaviors above and subsequently verify the proposed acceptance checks against the implementation.