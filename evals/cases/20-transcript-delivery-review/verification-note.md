# TranscriptDock record compilation

Synthetic fixture. Compiled 2026-09-08; this is a document compilation date.

## Pilot export

`pilot-attempts.csv` was exported September 8 from the August 17–21 studio pilot.
Each row is one provider submission attempt. `recording_id` is the stable editor
work item; retries keep that ID and receive another `attempt_id`. The timestamp
is when the submission began. Results and editor exports were reconciled through
August 21 at 18:00 UTC. There is no later outcome follow-up in this record.

`complete` means the provider returned a transcript. `timeout` means no response
arrived within the client's 20-second wait, not a confirmed provider failure.
`artifact_saved` records whether that attempt's transcript reached studio storage
by the cutoff. `editor_export_confirmed` records a successful file export from
that attempt. These flags do not record quality approval or release of source
audio. All submissions for these pilot work items during the window are included.

## Verification records copied into this note

- **V1:** Developer memo dated 2026-08-05 reports an executed pass on v1.1 staging:
  a saved transcript could be exported by the assigned editor, while another
  studio's user was denied. The memo gives August 5 as the execution date.
- **V2:** Operations handover says "manual retry drill passed on v1.1 staging."
  It describes staff looking up an existing attempt before retrying. The drill's
  execution date was not recorded in the material copied here. No automation
  ran in that drill, and the no-attempt-ID situation was not exercised.
- **V3:** Automatic timeout retry and automatic source deletion checks are listed
  in a draft checklist. No execution result is supplied for them.

No implementation files, fresh release run, or production verification are part
of this handover packet.
