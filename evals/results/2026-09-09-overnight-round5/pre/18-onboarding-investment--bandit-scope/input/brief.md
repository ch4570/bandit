# StockBridge — next week's investment

Synthetic fixture. All shops, records, statements, money, and estimates below
are fictional planning inputs, not real customer or delivery evidence.
Decision date: 2026-09-09.

## Product and available time

StockBridge helps independent hardware shops import an inventory export, review
stock quantities, and prepare their weekly supplier orders. Existing sign-in,
shop isolation, inventory storage, and stock-change history remain in place.
Each shop is one account, even if its owner uploads several files.

For September 14–18, one engineer has 30 hours total, including verification
and fixes. The founder has four hours total for all customer work that week:
existing reports, onboarding, troubleshooting, and checking outcomes. There is
no additional support person, overtime, contractor budget, or new integration.
The founder had more time during the completed pilot; that availability does
not continue next week. Engineering and founder hours are not interchangeable.

Eight additional shops with the same two export families are available for a
next-week trial. None has been promised admission or a delivery date. The team
may invite fewer or postpone them. Their outcomes and support needs are unknown.

## Completed onboarding pilot

`onboarding.csv` contains one row for each of the 16 shops admitted to the free
pilot. They are distinct from the six existing paying shops described below.
All 16 had a current export and a planned stock check at the start of August 31.
Their common observation window ended September 6 at 18:00 UTC. All attempted
an import, and every owner supplied the end-of-window outcome; there are no
pending windows or missing outcome records in this file.

CSV fields:

- `shop_id`: unique account; `export_family`: the shop's source-file family.
- `import_attempts`: all submitted import events, including retries by that shop.
- `stored_import_events`: attempts for which the server parsed and stored rows
  without a parser error. A shop may have several such events. This status does
  not check whether quantities or item identities are usable for the stock check.
- `manual_rescue`: 1 if the founder edited a source file, mapping, or imported
  data for the shop during this window; 0 otherwise. Rescue need not succeed.
- `usable_stock_check`: 1 if the owner completed the planned stock check using
  the imported inventory in StockBridge without correcting it in another tool
  by the deadline; 0 otherwise. Founder-corrected imports can meet this outcome.
- `support_minutes`: all founder time attributable to that shop during the
  window, including messages, diagnosis, rescue, and outcome confirmation.
  A shop can receive support without a manual rescue. Zero means no founder
  assistance was needed; the owner submitted the outcome through an existing form.
- `issue_note`: the support log's main issue, not an experimentally established
  cause or a claim that one proposed feature would solve everything.

The current importer does not offer a field-mapping preview or validate units
and duplicate item identifiers before storing rows. Successful storage is shown
as "Import complete." Owners can retry or ask the founder for help.

## Existing reporting work

Six older shops have each paid their current $60 monthly invoice. Their imports
are usable and their stock history is available. A weekly stock-change and
low-stock report is included in their current service; it must still be supplied
if report automation is deferred. Upcoming renewals have not been observed.

For each of the past two weeks, the founder logged 20 minutes per shop extracting
existing data and emailing the report. Four owners said they used the latest
report to prepare supplier orders; two have not reported whether they used it.
Three owners requested a download button so they need not wait for the email.
No owner has committed to renew because of that button.

The account manager argues, "These shops already pay us, and we are spending
time recreating the same report. Automating it could give us room to onboard."
The founder argues, "A file can say import complete while the shop still cannot
use its stock list. More reporting will not fix that first experience."
Neither statement is an adopted priority.

## Rough engineering estimates

These estimates use the existing application and data. They are unvalidated,
additive engineering hours, with no contingency. No candidate has been built
or tested. Verification covers the retained flow with representative files or
existing report data; fixes would use remaining engineering time.

| Candidate | Build | Verification | Included and excluded |
| --- | ---: | ---: | --- |
| Import review | 20 h | 6 h | Field mapping and preview, unit and duplicate-SKU warnings, correction and retry through the existing importer. No encoding repair, missing-source-data reconstruction, or vendor integration. |
| Weekly report download | 18 h | 6 h | Stock-change and low-stock report from existing usable inventory/history, with a downloadable file and date range. No forecasting, purchasing, or scheduled email. |

The engineer guesses a report download could reduce founder report work to
25 minutes total per week for the six shops, including exceptions. This is not
a timed result. No support-time saving or usable-outcome lift has been estimated
for import review, and no controlled comparison of either candidate exists.
