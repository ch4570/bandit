# Examples / 기획 예제

These are fictional product situations, not customer research or evidence that
the products have succeeded. The evaluation inputs contain deliberately supplied
facts, not real-world observations. Choose the specialist for a single task;
use `$bandit` for general or combined planning. Adapted prompts below are not
claims that those exact words produced a linked recorded answer.

## Recorded BANDIT examples / BANDIT 실행 예제

These outputs come from **unreleased local development**, not the public 0.4.0
release. They link to the original inputs, complete artifact and assessment.
They illustrate possible results, not a quality benchmark or a guarantee.

아래 결과는 **아직 공개 배포하지 않은 로컬 개발 버전**의 실행 기록입니다.
원본 자료와 전체 결과물, 검토 기록을 함께 보세요. 실제 고객 성과나 스킬의
일반적인 성능을 입증하는 자료는 아닙니다.

| Example | What to inspect |
| --- | --- |
| [HoldHarbor: rewrite a reminder PRD](library-pickup.md) · `$bandit-specify` | The actual before/after document, proposed rollout boundary, preserved consent rules and historical evidence |
| [SeatRelay: fund work before an event](standby-admission.md) · `$bandit-scope` | Complete admission versus partial screens, operating-time constraints, and a proposed decision without a false launch promise |
| [모아전: review photo-export permission](photo-export-review.md) · `$bandit-review` | A Korean review of linked policy, static code and historical verification; material findings without unnecessary scope changes |

## Historical examples / 이전 버전 예제

The following recorded outputs were produced by **PM Craft 0.1.0**, BANDIT's
earlier name. Their names, evidence and assessments remain historical. The
“Try it” prompts use the corresponding current command.

| Example | What to inspect |
| --- | --- |
| [GatherTrip: two decisions in one trip](gathertrip.md) | A response belongs to a participant **and** a particular vote; joining, editing, closing, and finalizing have distinct rules |
| [ChangeDesk: a free offer with team drafting](change-desk.md) | A pricing change affects current requirements without rewriting past payment evidence or giving collaborators customer approval rights |

각 예제의 원본 요청과 결과는 연결된 평가 자료에서 확인할 수 있습니다.
단순히 양식을 채우는 것보다, 같은 단어가 도메인에서 무엇을 뜻하는지 살펴보세요.
여행의 ‘결정’은 여행 전체가 아닌 숙소·출발일 각각에 속하고,
견적을 ‘함께 작성’하는 권한은 고객을 대신해 ‘승인’하는 권한과 다릅니다.

For your own work, provide the current request, existing adopted decisions, and
the relevant source files. Small tasks can stay in the conversation; the optional
plan template is for a new document that needs to persist. [Usage guide](../docs/usage.md).
