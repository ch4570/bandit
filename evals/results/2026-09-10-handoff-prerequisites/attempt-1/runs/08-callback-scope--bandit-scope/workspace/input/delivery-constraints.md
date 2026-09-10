# Synthetic delivery constraints

Release window ends 2026-09-30. Available capacity, including integration and fixes:
6 backend engineer-days, 4 frontend engineer-days, and 2 QA engineer-days. There is no
second engineering team to absorb deferred work. Estimates below are separate end-to-end
feature estimates; adding features adds their effort unless an overlap is demonstrated.

| Proposal | Backend days | Frontend days | QA days |
| --- | ---: | ---: | ---: |
| Callback queue with owner and claim | 3 | 3 | 1 |
| Automatic SMS reminders | 5 | 2 | 2 |
| Self-service routing/escalation rules | 4 | 4 | 1 |
| Weekly manager email | 2 | 2 | 1 |

A pilot measurement report using existing server events needs a further 0.5 backend day
and 0.5 QA day; it needs no new frontend. These estimates do not include a multi-branch
ownership redesign or new notification providers.

The SMS adapter is not yet approved by the provider; there is no committed approval date.
The product's existing customer agreement permits SMS only with a stored consent record.
Operations has not approved a fallback that texts customers without that record.

Use existing branch access permissions. Limit pilot enrollment to named desks that agree
to participate; give customer success a way to stop enrollment or disable the feature.
The existing feature flag can disable a pilot without erasing callback records. No payment,
new pricing, contact-data enrichment, or change to branch ownership is authorized here.
