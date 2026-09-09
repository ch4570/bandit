# General-arm launch correction

The first case-13 launch used `--arm bandit --standalone`. The runner rejected
it before creating a TASK with exit 2: `--standalone requires a specialist arm`.
The pre-run receipt's `standalone: true` for this general arm records that
original plan, not a completed execution. The four specialist plans are unchanged.

The corrected general launch omits `--standalone`; the general arm's normal
instruction layout supplies its complete general `bandit` folder. This correction
does not change raw fixtures, rubric, skill bytes, model defaults, web mode, or
the requested answer. The rejected CLI invocation is not counted as a TASK.
