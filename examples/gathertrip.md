# GatherTrip — one trip, separate decisions

**Synthetic example.** The founder has chosen an accountless group trip planner.
One developer has two weeks. A lodging vote and a departure-date vote can be
open together. Participants can change their own responses before each closes;
the organizer makes the final choice. No demand research or implementation exists.

[Original request](../evals/cases/01-multiple-decisions/request.md) ·
[Raw brief](../evals/cases/01-multiple-decisions/brief.md) ·
[Evaluation record](../evals/README.md)

## The consequential product rule

A response is identified by `(decision, participant)`, not by the trip alone.
Changing a lodging vote replaces one contribution to that vote. It must not
change the participant's departure-date response or the other vote's deadline.

The independent forward test produced that rule and a complete draft around it:
join explicitly rather than on link open, retain a participant identity without
requiring an account, close each vote independently, show nonresponders for that
vote, and let the organizer choose even when the counts are tied. Unspecified
policies were labeled as draft recommendations.

## One acceptance scenario

> 민수는 숙소에만 응답하고 지수는 아무 투표에도 응답하지 않았다.
> 숙소 미응답자는 지수이고, 출발일 미응답자는 둘이다.

This scenario is a planned check. It does not mean the app was built or a test
passed. It makes a likely implementation mistake visible before development.
Read the [full output](../evals/results/2026-09-07/01-multiple-decisions--pmcraft-forward/output.md)
and [independent grading](../evals/results/2026-09-07/grades-01-04.md).

## Try it

```text
$pm-craft 한 여행에서 숙소와 출발일을 따로 투표하는 웹앱이야.
로그인 없이 참가하고 마감 전 자기 응답을 바꿀 수 있어.
개발자 한 명, 2주 MVP로 기획해줘. 작은 정책은 초안으로 제안해.
```

Bring an existing PRD if you have one. The skill should adapt to its rules rather
than copy every proposed policy from this example.
