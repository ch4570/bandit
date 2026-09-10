# Second candidate: reconcile arithmetic and currency

The first five offline tasks passed the unchanged mandatory meaning criteria,
but independent grading found a real arithmetic defect in the general handoff:
the listed cash allocations total 700,000 KRW, not the reported 800,000 KRW.
The live native task also left Cal.com's quoted dollar currency unspecified;
its native transport did not export retrieval events. The live grade was
therefore partial, and neither limitation is erased by the first round's passes.
These observations are tracked in Issue 16 alongside Issue 15.

The second candidate adds two general checks: recompute reported arithmetic
with available tools and reconcile unallocated funds; verify quoted currency
before comparing sources using the same symbol. No fixture-specific amount,
company, or answer is added to the skill. First-round instruction bytes are
preserved in instruction-snapshots/round1-product-journey.md.txt.

Repeat all five CLI tasks from protocol.md against the second candidate, with
the same raw fixtures, original criteria, caps, host-default routing, and fresh
workspaces. Do not tell the executing agents the earlier defect or intended fix.
Store them separately as round2 runs. The grade criteria remain unchanged;
independent arithmetic/units checks are reported explicitly in addition to the
original criteria so a permissive pass cannot conceal a numerical error.

Also repeat case 14 using the CLI runner's explicit --allow-web flag. Only this
registered case can enable live web search; other cases still reject that flag,
and case 14 refuses to run without it. Its raw request, unchanged research skill
route, and original criteria stay separate. Use an 1800-word cap and 600-second
timeout, with a read-only workspace, no child agents and no external actions
other than requested source retrieval. Preserve web events for an independent
source/answer review; model/usage observations remain limited to actual events.

This is a corrective development round, not a comparison proving superiority.
All earlier artifacts and grades remain. No criterion is rewritten to pass.
