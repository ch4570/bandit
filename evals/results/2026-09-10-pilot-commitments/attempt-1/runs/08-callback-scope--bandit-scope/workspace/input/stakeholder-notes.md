# Synthetic planning notes

Mina, customer success: “The two small desks have offered a two-week pilot and can send us
their shift-handoff notes. They already review late callbacks every Friday.”

Jules, sales: “A large multi-branch prospect said an automation demo would be interesting.
They have not promised a trial, a security-review date, or a purchase.”

Arun, operations: “A shared queue with a visible owner might be enough for the first shift.
Please don't silently move callbacks between branches.”

Leah, design: “If we add a queue, dispatchers need to see who owns an item before claiming
it. We can reuse our table and status components. A custom workflow builder needs new UI.”

Proposals currently circulating:

- Outstanding-callback queue with owner and claim action.
- Automatic SMS reminders when callbacks become late.
- Self-service branch routing and escalation rules.
- Weekly manager email with late-callback totals.

These are proposals, not approved requirements. The managing director has asked for one
useful shipped slice this month and an explicit review before more customers are enrolled.
