# ChangeDesk PRD v1

Decision D1 (adopted): freelancers pay KRW 9,000 per change quote before sending
it to a customer. This is a one-time fee per quote, not a subscription.
H1: ten paid quotes per month per freelancer can support KRW 90,000 monthly
gross revenue per active freelancer, before costs and refunds.

R1: only the quote creator may edit its draft. A quote names the customer decision
maker. That person can explicitly accept or reject the sent quote version.
R2: viewing the customer link records a view only; it does not record acceptance.
R3: when amount or delivery date changes after sending, create a new version;
an earlier acceptance does not accept the new terms.
R4: show the creator a payment screen before sending; sending is blocked before
successful payment. The screen reads “Send your quote · KRW 9,000”.

Experiment X1: offer paid quotes to reachable freelancers and observe collected
payments, delivered quotes, refunds, and repeat use over 30 days. The team has
not adopted a universal pass/fail threshold.

V1: explicit accept/reject transitions, executed on v1 in the staging environment,
passed; evidence: supplied test report dated 2026-08-10, linked to R2/R3.
V2: checkout blocks unpaid send, executed on v1 staging, passed on 2026-08-10.
V3: concurrent draft editing, not implemented or tested.
