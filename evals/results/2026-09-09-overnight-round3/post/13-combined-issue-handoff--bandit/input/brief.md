# ShelfNote — first warehouse trial

Synthetic fixture. This warehouse, staff, reports, constraints, and estimates
are fictional planning inputs, not real customer or delivery evidence.

## Current direction — adopted 2026-09-09

One warehouse has 12 day-shift pickers and a shift lead. The lead sometimes
changes between shifts; the existing employee directory supplies the current
lead role. Staff want to report missing or unreadable shelf labels and stock
stored under the wrong shelf label. This trial does not manage emergencies,
inventory quantities, purchasing, or equipment maintenance.

A picker should be able to identify a shelf, describe its problem, and see the
report's current handling state later. The shift lead reviews reports, arranges
the physical correction through existing warehouse work, and records what was
done. A report is resolved only when the lead explicitly records that correction;
opening or reading a report is not a resolution. Software does not itself move
stock or verify the physical correction.

Pickers can create reports and read their own reports. The shift lead can read
all warehouse reports and record resolution. The existing sign-in service
provides stable employee IDs, active status, and the current lead role; keep
that integration. Former staff have no app access. Public links and a new
account-registration system are outside the trial.

The initial team is fixed. Managers have not promised recurring reports,
notifications, images, or offline submission. The earlier
[screen sketch](draft.md) is a proposal, not an adopted delivery commitment.

## Existing tools and working conditions

- A read-only shelf directory supplies valid shelf IDs, such as A-03-02, and
  their aisle names. Its existing lookup can be reused on the phone.
- Staff currently send plain-text messages to the shift lead. The lead keeps
  a private spreadsheet with shelf ID, description, reporter, date, and handling
  note. Some reporters send another message because they cannot see the sheet.
- The existing application shell includes sign-in, the employee directory, a
  simple shared record store, and mobile text forms. It has no issue-specific
  submission, status list, resolution screen, upload service, or offline queue.
- Wi-Fi is available in the warehouse, but a phone can lose its connection while
  submitting. Staff may tap again when a result does not arrive. They can walk
  back into coverage; offline submission is not a trial requirement.
- Staff have work phones with browsers. The lead can check a shared list during
  the shift, but has no time to relay every status change individually.

## Capacity and estimates

One developer has four developer-days before the proposed first use. The lead
can join one half-day walkthrough of the retained flow. No field walkthrough,
implementation, or product test has happened yet.

These rough estimates assume the existing application shell and integrations
remain unchanged. Build items include ordinary saved-state/error feedback but
exclude the walkthrough and its fixes. They are additive; no contingency or
validated delivery date is included.

| Candidate | Developer-days | Included work |
| --- | ---: | --- |
| Text report and My reports | 1.5 | Shelf lookup, note submission, saved report reference and current status |
| Lead queue and resolution | 1.0 | Shared unresolved list, report details, resolution note and updated state |
| Photos | 1.5 | Upload, access control, size/error handling and report display |
| Offline outbox | 2.5 | Local queued reports, reconnect behavior and conflict/retry handling |
| Email status notifications | 1.0 | Delivery integration, message content and delivery failures |
| Aisle map | 1.5 | Visual shelf selection and current issue markers |
| Retained-flow walkthrough | 0.5 | Staff/lead scenarios on phones; fixes are additional work |

The developer can defer candidates or recommend a smaller first trial. The
four-day limit still includes the retained-flow walkthrough.
