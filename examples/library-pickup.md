# HoldHarbor — rewrite the PRD, keep the evidence

**Synthetic example from unreleased local BANDIT development.** This is a
recorded `$bandit-specify` document edit, not a result from the public 0.4.0
release or evidence about a real library.

[Original request](../evals/cases/19-library-pickup-reminders/request.md) ·
[Before PRD](../evals/cases/19-library-pickup-reminders/docs/PRD.md) ·
[Pilot notes](../evals/cases/19-library-pickup-reminders/pilot-notes.md) ·
[Reader data](../evals/cases/19-library-pickup-reminders/reader-outcomes.csv) ·
[Actual rewritten PRD](../evals/results/2026-09-09-overnight-round8/post/19-library-pickup-reminders--bandit-specify/after/docs/PRD.md)

## What to inspect

The requested direction replaces manually composed pickup texts with a
staff-visible automatic queue. The saved PRD replaces that current behavior
while retaining email, explicit SMS consent, account permissions, seven-day
holds and desk-recorded collection. Opening a message is not collecting a book.

The availability boundary was not chosen by the user. The answer recommends
continuing with the original 50 readers, labels this as proposed, and carries
that boundary into queue requirements and planned checks. It does not call
50 readers a proven fit: it proposes a shared 90-minute support budget and a
pause when that budget is exhausted. Engineering estimates remain outstanding.

The historical record stays historical. Twenty of the 50 readers had no ready
hold, rather than a failed pickup; observed pickup rates concern the 30 with
an opportunity. Manual SMS alongside email does not establish the effect of
automation. Old staging checks do not become passing checks for the new queue.

The linked result is the actual edited PRD, not the final chat summary. Only
that permitted document changed in the isolated run. The
[review and trace notes](../evals/results/2026-09-09-overnight-round8/grades-19-post.md)
include the preserved writing-command recovery and evaluation limits. No
software was implemented or tested, and no rollout occurred. One selected
answer does not establish reliability or improvement caused by the skill.

## Try it with your own materials

Adapt the paths and constraints to your project. These shorter prompts are
usage examples, not the exact prompt that produced the recorded artifact.

```text
$bandit-specify Rewrite docs/PRD.md for the adopted move from manual reminders
to a staff-visible automatic queue. Use the supplied pilot notes and capacity
limits to recommend an initial audience; that choice is still open. Preserve
adopted access and consent rules and the original meaning of past evidence.
Update the affected requirements and acceptance checks. Edit only docs/PRD.md.
```

```text
$bandit-specify 수동 알림을 직원에게 상태가 보이는 자동 큐로 바꾸기로 했어.
제공한 파일럿 기록과 운영 한도로 초기 대상을 추천해서 docs/PRD.md를 다시 써줘.
대상 범위는 아직 미정이야. 확정된 접근·동의 규칙과 과거 근거의 의미는 보존하고,
영향받는 요구사항과 수용 기준을 맞춰줘. docs/PRD.md만 수정해줘.
```
