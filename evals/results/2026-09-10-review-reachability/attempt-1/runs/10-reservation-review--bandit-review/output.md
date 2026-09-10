The draft needs bounded corrections before the pilot: it permits unauthorized acceptance, treats different offer revisions as the same action, and can report a room as secured after allocation delivery has failed. Withdrawal during pending allocation remains an explicitly owned policy decision.

This review inspected the plan, its adopted policy, and the community notice. The notice adds no applicable reservation rules. All findings concern documented behavior; no implementation or runtime behavior was verified.

**1. Assigned-organizer permission is missing from the proposed endpoint.**

Sources: `reservation-confirmation-plan.md:17–30`; `policy/offer-acceptance.md:10–13`.

The adopted rule permits only the assigned organizer to accept. Active workspace membership is necessary but insufficient, and managers cannot accept on the organizer’s behalf. The endpoint explicitly checks only membership and workspace ownership.

**Scenario and consequence:** Another active member—including a manager—submits the reservation’s current revision and records agreement without the organizer’s authority.

**Bounded correction:** Require the authenticated member to be the reservation’s assigned organizer before accepting or returning an acceptance as a successful action.

**Acceptance checks:** For a reservation assigned to organizer A, A can accept its current revision. Active member B and a workspace manager cannot accept it; neither request creates an acceptance or initiates ledger allocation. Inactive and cross-workspace requests remain denied. These checks implement an adopted rule, not a new policy decision.

**2. Repeat detection conflates retries with acceptance of changed terms.**

Sources: `reservation-confirmation-plan.md:10–13,21–30`; `policy/offer-acceptance.md:6–8,15–19`.

The policy defines one logical action by organizer, reservation, and revision. The plan instead finds an existing acceptance using only member and reservation, returning it before checking the submitted revision. Publishing a new revision does not update that row.

**Scenario and consequence:** A accepts revision R1. A manager publishes R2 with changed room details. After reviewing R2, A presses “Accept offer,” but the endpoint returns the stored R1 acceptance. The new agreement is never recorded. Alternatively, an old R1 payload retained after a timeout receives HTTP 200 after R2 appears, without the required explanation that the offer changed.

**Bounded correction:** Validate the request against the current published revision before successful repeat handling. Distinguish an exact retry from a new revision’s acceptance, and retain which revision each agreement concerns. The physical table design is an engineering choice; the product outcome is already decided.

**Acceptance checks:**

- Repeating acceptance of still-current R1, including after a lost response, produces one logical acceptance and no additional allocation effect.
- After R2 is published, submitting R1 explains that the offer changed and does not accept the superseded offer.
- After the organizer reviews R2, submitting R2 records agreement to R2 rather than returning R1 as fulfillment of that request.
- A retained stale client payload cannot silently become acceptance of R2; the organizer must review the changed contents.

**3. A committed acceptance can become permanently disconnected from allocation.**

Sources: `reservation-confirmation-plan.md:21–26,34–40`.

The insert commits before queue publication. If publication fails, the endpoint returns 503, but no event is retained for later delivery. A retry finds the acceptance and returns HTTP 200 without reaching publication. Operators can inspect the mismatch but have no repair action.

**Scenario and consequence:** An organizer’s acceptance is saved, queue publication fails, and the organizer retries. The retry appears successful, yet the ledger never receives the acceptance. The described flow provides no recovery path to securing the room.

**Bounded correction:** Specify a recoverable handoff between recording agreement and ledger application. Engineering may choose durable delivery, reconciliation, or a bounded operator repair mechanism. Whichever mechanism is chosen must survive interruption and preserve one logical allocation effect. Consumer event-ID deduplication alone does not recover an event that was never sent.

**Acceptance checks:** Interrupt the operation after acceptance commit but before successful publication. The response remains visibly pending, and the defined recovery path eventually delivers it without requiring a new agreement. Also cover successful publication followed by a lost response: retries and redelivery must not create an additional allocation effect. An operator must be able to identify and resolve an acceptance that remains unapplied through the chosen recovery path.

**4. “Room secured” is asserted from the wrong source of truth.**

Sources: `reservation-confirmation-plan.md:34–37`; `policy/offer-acceptance.md:21–23`.

The adopted policy separates receiving agreement from securing the room and makes the ledger authoritative. The proposed status endpoint reads only the acceptance row and labels `accepted` as “Room secured.”

**Scenario and consequence:** Even with successful queue publication, the consumer may not yet have applied the acceptance. The organizer sees a secured room before allocation exists. Publication failure makes that incorrect status potentially persistent.

**Bounded correction:** Show “Response received” while ledger application is pending. Show “Room secured” only when supported by authoritative ledger allocation for the relevant acceptance/revision. Repairing queue delivery does not by itself correct this premature claim.

**Acceptance checks:** Before ledger application—including delayed or failed publication—status shows “Response received,” not “Room secured.” Once the ledger confirms the applicable allocation, status shows “Room secured.” Repeated requests and page reloads preserve this distinction.

**5. Withdrawal requires an operations decision, not an inferred winner.**

Sources: `reservation-confirmation-plan.md:39–42`; `policy/offer-acceptance.md:25–27`.

Both documents explicitly leave withdrawal while awaiting allocation undecided. This is an acknowledged dependency, not an overlooked policy or evidence that the proposed acceptance flow already implements withdrawal incorrectly.

**Scenario and consequence:** An organizer withdraws while the consumer is about to apply acceptance. Different implementations could allocate despite withdrawal, suppress allocation, or release an allocation. The policy authorizes none of those outcomes yet.

**Required owner decision:** Operations must choose the observable outcome and the boundary after which withdrawal is unavailable or follows a separate process. Record that decision before including withdrawal in the pilot.

**Conditional acceptance checks:** If pending withdrawal is allowed, check withdrawal before application and concurrent with application against the chosen ordering rule, including repeated withdrawal requests. If it is disallowed, a pending withdrawal attempt must clearly report that result and leave the acceptance unchanged. Any release behavior needs explicit authorization.

All files remain unchanged. The next useful step is to incorporate these targeted corrections and resolve the withdrawal dependency, then execute the proposed interruption, permission, and repeat-action checks against the implementation. None of those checks has been run; this review establishes planning issues, not demonstrated software failures or customer evidence.