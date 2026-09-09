# SeatRelay — useful work without promising an unsupported launch

**Synthetic example from unreleased local BANDIT development.** The recorded
`$bandit-scope` answer recommends an investment; it does not execute a workshop
rollout or demonstrate that a prototype works. It is not a public 0.4.0 result.

[Original request](../evals/cases/21-standby-admission/request.md) ·
[Brief](../evals/cases/21-standby-admission/pilot-brief.md) ·
[Adopted rules](../evals/cases/21-standby-admission/adopted-rules.md) ·
[Estimates](../evals/cases/21-standby-admission/engineering-notes.md) ·
[Recorded recommendation](../evals/results/2026-09-09-overnight-round10/current/21-standby-admission--bandit-scope/output.md)

## What to inspect

The intended result is a confirmed standby seat that appears on the final
admission roster. An acceptance screen or reply CSV alone cannot provide that
result. The complete supplied estimate is 14 engineering hours before fixes,
against 12 available; fewer invitations do not remove the shared work.

Manual reconciliation needs responses received that evening. The coordinator
has 20 free minutes at lunch, but none after closing. Those minutes cannot be
moved to the evening, and gate volunteers cannot allocate seats. The issue is
when work can happen, not just whether the two minute totals look compatible.

The answer recommends the estimated two-hour non-production walkthrough and
its included 20-minute coordinator review, leaving ten engineering hours
uncommitted to standby production. It states what the prototype cannot deliver.
Deferring standby admission still needs Mara's approval because it changes the
adopted workshop outcome; the answer does not claim that approval exists.

This is one possible bounded recommendation, not a rule to always build a
prototype, leave time unused, or refuse a tight deadline. A different complete
plan would need its own supported estimate and applicable authority. The
[paired assessment](../evals/results/2026-09-09-overnight-round10/grades-21.md)
records that the baseline also reached the material distinctions. This example
establishes no skill advantage, causal effect, customer value or general reliability.

## Try it with your own materials

Supply your actual outcome, estimates and people's availability. These adapted
prompts are not the exact request that produced the linked answer.

```text
$bandit-scope Recommend what to fund before this event using the attached
adopted rules, estimates and staffing windows. Explain what the scope actually
delivers, what it leaves out, and any manual work it requires. Name the next
decision and what could change your recommendation. Do not edit files.
```

```text
$bandit-scope 확정된 행사 규칙, 작업량 추정, 담당자별 가능 시간을 보고
이번 행사 전에 무엇에 투자할지 추천해줘. 실제로 제공하는 결과와 빠지는 부분,
필요한 수동 작업을 설명하고 다음 결정과 권고를 다시 볼 조건을 정리해줘.
파일은 수정하지 마.
```
