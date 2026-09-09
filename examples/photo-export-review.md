# 모아전 — photo exports after permission withdrawal

**Synthetic example from unreleased local BANDIT development.** This recorded
`$bandit-review` answer uses Korean source documents and responds in Korean.
It is not a public BANDIT 0.4.0 result, a real customer case, or the first
Korean review request in the evaluations. The v0.3/v0.4 labels below belong
to the fictional photo-export product, not BANDIT releases.

[Original request](../evals/cases/22-photo-export-consent/request.md) ·
[PRD draft](../evals/cases/22-photo-export-consent/delivery-prd.md) ·
[Adopted policy](../evals/cases/22-photo-export-consent/delivery-policy.md) ·
[Static code](../evals/cases/22-photo-export-consent/export_snapshot.py) ·
[Verification record](../evals/cases/22-photo-export-consent/verification-note.md) ·
[Actual Korean review](../evals/results/2026-09-09-overnight-round13/bandit-review/output.md)

## What to inspect

The review identifies two consequential findings without rewriting the supplied
artifacts. First, the adopted rule forbids starting a new download after
permission withdrawal is saved, even for an already requested or prepared ZIP.
The implementation-derived draft freezes permission at request time, while
the download function checks requester, expiry and readiness without checking
current project permission. A mixed-project ZIP could include withdrawn photos.
This is a static-source inference, not an
observed disclosure or runtime breach.

Rejecting an affected bundle and inviting a new request is a proposed
correction, not adopted policy.
Stopping an in-progress transfer or remotely retrieving a saved copy remains
outside the promised withdrawal boundary.

Second, two reported v0.3 passes covered another requester's access and expiry
with fixed permissions. They do not establish v0.4 asynchronous-export or
withdrawal readiness. It preserves those historical passes while requesting
new checks. Agreement with a code-derived PRD is not independent policy
verification.

Useful controls remain: project/photo restrictions at request time and
requester, readiness and expiry checks at download time. Public sharing,
nonmembers, private photos, watermarks and new SSO are not required repairs.
No product code or tests were executed, and this is not a legal-compliance
assessment.

The [paired baseline](../evals/results/2026-09-09-overnight-round13/baseline/output.md)
also identifies both material findings. Read the full answers and
[paired assessment](../evals/results/2026-09-09-overnight-round13/grades-22.md).
This selected example is not a quality benchmark or evidence of skill
advantage, general Korean performance, or customer outcomes.

## Try it with your own materials

Supply your own adopted policy, draft and verification records. These adapted
prompts are not the exact words that produced the recorded review.

```text
$bandit-review Review this photo-delivery PRD against its linked adopted
policy, supplied code and verification records. Prioritize consequential
findings with source locations, impact, corrections and next checks. Preserve
supported controls and exclusions. Distinguish static inference from observed
execution. Use only these files; do not edit them or execute code or tests.
```

```text
$bandit-review 사진 전달 PRD와 연결된 승인 정책, 코드, 검증 기록을 함께 검토해줘.
중요한 발견을 근거 위치, 영향, 수정·결정 사항, 다음 확인과 함께 우선순위화해줘.
이미 맞는 통제와 제외 범위는 유지하고 정적 추론과 실제 실행 결과를 구분해줘.
한국어로 답하고 제공 파일만 읽어줘. 파일 수정이나 코드·테스트 실행은 하지 마.
```
