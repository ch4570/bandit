# ChangeDesk — change the offer, preserve the evidence

**Synthetic example.** A freelancer's change-quote tool moves from KRW 9,000 per
quote to free use with collaborative drafting. A named customer decision maker
still exclusively accepts or rejects a particular quote version.

[Update request](../evals/cases/02-offer-change/request.md) ·
[Previous PRD](../evals/cases/02-offer-change/current-plan.md) ·
[Supplied pilot report](../evals/cases/02-offer-change/observations.md) ·
[Evaluation record](../evals/README.md)

## Follow the change

The current plan needs to remove the payment-before-send rule and the old send
button price. Team members can draft; that does not transfer the customer's
decision authority. Concurrent drafting needs a product rule and a future
check, because the supplied preview used manual concierge coordination.

The old pilot remains evidence about the old offer. Its eight payments and two
full refunds imply KRW 54,000 still collected at the reporting date. That is not
profit, and it does not demonstrate willingness to pay for the new free offer.

In the preview, four of six senders who had another quote opportunity used the
tool again. Four of fourteen total senders is a different denominator. Eight
senders had no second opportunity yet; treating all eight as churn hides the
observation window. Pricing, sharing, and recruitment changed together, so the
preview cannot isolate the causal effect of price.

These interpretations come from the **fictional supplied data**. They illustrate
the reasoning a useful update should preserve, not real business performance.
See the [PM Craft output](../evals/results/2026-09-07/02-offer-change--pmcraft/output.md)
and [grading, including the shared reporting omission](../evals/results/2026-09-07/grades-02-03-05.md).

## Try it

```text
$bandit 다음 파일럿은 무료로 바꾸고 팀 동료와 초안을 함께 쓰게 할 거야.
고객 승인은 지정 담당자만 할 수 있어. 기존 PRD와 관측 결과를 읽고
영향받은 요구사항·지표·검증을 갱신해줘. 과거 기록은 남겨줘.
```

Use your actual baseline and new evidence. Do not invent a payment, usage event,
or passed software check merely because the new plan needs one.
