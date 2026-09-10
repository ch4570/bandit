# Independent live-research assessment

Assessment date: 2026-09-10 (Asia/Seoul).

Output SHA256: `12e88fee1d6a47b548177ba78da34c666eb773ffcef29d41d8ddb5c1b53a8fd1`

Inputs read:

- `/tmp/bandit-journey.oMXLuA/live-research/request.md`
- `/tmp/bandit-journey.oMXLuA/live-research/output.md`
- `/Users/ch4570/orca/bandit/evals/criteria/2026-09-10-live-research/14-live-channel-research.md`

No skill instructions, author diagnoses, other outputs, or prior grades were read. The assessor independently opened the cited official sources and inspected the two public pricing pages' HTML. Source checks below establish answer/source correspondence on the assessment date. They do not prove the executing agent's exact retrieval history, tool usage, access dates, or absence of external actions: native execution logs were unavailable. The criteria describe this as an author-created development check, not an independently held-out benchmark.

## Per-criterion result

| Criterion and frozen locator | Status | Output locators and assessment |
|---|---|---|
| 1. Retrieve first-party evidence for both alternatives; preserve links and explain gaps (criteria lines 7–8) | partial | Output lines 1, 7–8, 18–24, 28, and 30 contain working official links for both companies, and the consequential claims correspond to the pages checked below. Cal.com monthly pricing, contract conditions, free-plan eligibility, and document-update uncertainty are left unresolved. This satisfies observable source correspondence. The claim of direct retrieval in output lines 3 and 30 cannot itself establish that the executing agent actually retrieved those pages; that part remains unverified without its logs. No fabricated citation or demonstrated false retrieval claim was found. |
| 2. Distinguish one available host from several simultaneous hosts, attribute plans, preserve uncertainty (criteria lines 9–11) | passed | Output lines 7–10 correctly separate Round Robin, Collective, and Calendly Group. Calendly plan assignments match S1; Cal.com Teams assignments and inheritance match S3–S5. The fixed/mixed-host caveat in line 12 matches S2 and S4. Line 28 correctly preserves Dynamic Group Links as another multi-host option and leaves free-plan eligibility unresolved, supported by S7–S8. |
| 3. Bind prices to unit, currency, period, access date; avoid false equivalence (criteria lines 12–13) | partial | Lines 14–26 distinguish annual monthly equivalents from monthly billing, seat/user units, hypothetical headcount, excluded costs, and non-equivalent products. Lines 3 and 30 supply an access date. All stated base price magnitudes checked out against S3 and S9, including Calendly's monthly values in embedded USD data. The remaining gap is currency precision: line 22 explicitly identifies Calendly USD, but Cal.com amounts in lines 20 and 26 use only `$`. Its cited pricing page and inspected HTML do not identify a currency code. Line 14 leaves Korean checkout currency unresolved, but does not clearly say that the displayed Cal.com denomination itself remains unconfirmed. Do not infer comparable currency from the shared symbol. This is an incomplete condition, not evidence that the stated dollar amount is wrong. |
| 4. Recommend a bounded research question; distinguish user, payer, positioning, and unobserved demand (criteria lines 14–15) | passed | Lines 1, 3, and 32–34 focus on project-specific participant selection and setup effort, identify designers versus studio owners, and explain that feature availability does not establish an unmet need. Lines 36–42 describe positioning as a concept and avoid observed superiority or time-saving claims. The competitor evidence narrows what to investigate without purporting to validate demand. |
| 5. Provisional message and feasible experiment with observable behavior, denominator, and changeable decision (criteria lines 16–18) | passed | Lines 36–42 provide a usable provisional message. Lines 44–50 specify five studio pairs, a bounded schedule and zero-money budget, retrospective evidence, a paper-prototype task, setup success/time, and separate relevant-case and problem-evidence counts. The temporary threshold includes concrete owner follow-up and budget conditions; possible decisions include further prototype research, setup/templates, or shelving the product hypothesis. Lines 50–52 address insufficient eligible cases and explicitly deny statistical demand, willingness-to-pay, or retention proof. Recruitment availability is stated as an assumption rather than guaranteed. |
| 6. Requested scope and no contacting, registration, spending, or publication (criteria line 19) | passed | For the observable answer, lines 1–52 stay in the requested Korean competitor brief, research recommendation, one message, and one experiment plan. There is no market-sizing report or full PRD. Lines 44, 46–48, and 52 consistently frame outreach and testing as future proposals and claim no prohibited action occurred. This rating covers answer scope and stated plans only; it does not independently attest the original agent's external action history. |

Summary: 4 passed, 2 partial, 0 failed. Criterion 1 is partial because execution evidence is unavailable; criterion 3 has a minor but concrete currency-condition omission. Do not report this as six fully verified acceptance criteria or as a runtime/tool-use benchmark.

## Official source correspondence

All following checks were performed by this assessor on 2026-09-10. Source line locators refer to the web tool's rendered text during this assessment; section names are supplied for later navigation. No third-party claims were used.

| Source | Source locator and correspondence |
|---|---|
| S1 — [Calendly multi-person scheduling](https://calendly.com/help/multi-person-scheduling-options-for-your-organization) | Updated-date line 71; event definitions/plans lines 74–77, 97–106; paid-host and invitee-seat conditions line 92. Supports output lines 7–8, 22, and the stated update date in line 30. |
| S2 — [Calendly event types overview](https://calendly.com/help/event-types-overview) | Updated-date line 68; Group line 95; Collective and multiple host groups lines 107–116; Round Robin and group availability lines 120–129. Supports output lines 10, 12, and 30. |
| S3 — [Cal.com pricing](https://cal.com/pricing) | Teams card lines 102–123 shows yearly billing, $12 per user/month, Round Robin and collective events; Organizations and Enterprise inheritance lines 152 and 181. Supports output lines 7–8 and 20. Rendered text and public HTML searches found no `USD`, `currency`, or `priceCurrency`; no currency denomination is inferred. No monthly value was imputed from the savings percentage. |
| S4 — [Cal.com Round Robin](https://cal.com/help/event-types/round-robin) | Summary line 85; prioritization/weights/history lines 98–121; groups lines 126–140; fixed hosts lines 146–148. Supports output lines 7 and 12. |
| S5 — [Cal.com Collective Events](https://cal.com/help/event-types/collective-events) | Main explanation lines 83–85 identifies Teams, chosen co-hosts, individual availability by default, and a shared-schedule override. Supports output line 8. |
| S6 — [Cal.com seat billing](https://cal.com/help/billing-and-usage/seat-billing) | Two models line 23; peak membership lines 28–40; active participants and minimum commitments lines 46–59. Supports the distinctions and unresolved plan applicability in output line 24. The page does not resolve which model a new ordinary Teams agreement receives. |
| S7 — [Cal.com Dynamic Group Links product page](https://cal.com/features/dynamic-group-links) | Instant group creation lines 89–91 and link syntax lines 107–109 support output line 28's claim that no team or predefined event setup is needed. |
| S8 — [Cal.com Dynamic Group Links help](https://cal.com/help/event-types/dynamic) | Lines 85–87 explain username composition and participation settings, without an explicit free-plan entitlement condition. Supports output line 28's restrained feature description and unresolved eligibility. |
| S9 — [Calendly pricing](https://calendly.com/pricing) | Yearly selector line 24, Standard card lines 41–47, Teams card lines 81–87. Independently fetched public HTML contains Standard `prices → USD → monthly = $12`, `annual = $10`, and Teams `prices → USD → monthly = $20`, `annual = $16`. Those data, rather than a discount-percentage inference, corroborate output lines 18–19 and 22. The three-user annual calculations in line 26 are arithmetically correct under the stated fixed-count assumptions. |
| S10 — [Calendly company admin guide](https://calendly.com/help/company-admin-guide) | Update date line 68; billing timing and occupied/unoccupied seats lines 219–230. Supports output lines 22 and 30. |
| S11 — [Cal.com Teams product page](https://cal.com/teams) | Round Robin and Collective summaries lines 163–169 support output line 1's broad assertion that both scheduling patterns exist. |

## Major gaps and limits

- No major contradiction was found in the checked feature, plan, base-price, billing, or source-update claims. The Cal.com displayed-currency ambiguity should be made explicit before readers treat the cost examples as a shared-currency comparison. Its monthly price and exact contract-dependent billing conditions appropriately remain unresolved; the assessor supplies no replacement values.
- Original retrieval and action provenance remain unverified. This assessor's successful later retrieval is independent corroboration, not proof of the executing agent's browsing or compliance. Retain the output's claimed access date as a claim, and retain source correspondences separately from execution attestations.
- The proposed five-studio study can guide the next research investment. It does not establish a market, price acceptance, comparative usability gains, or real purchasing behavior, and the output does not claim otherwise.

Only this grading report was created. The request, frozen criteria, and evaluated output were not modified.
