# TranscriptDock — proposed release handoff

Synthetic fixture. The studio, recordings, records, and people are fictional.
Written 2026-09-09 by product coordinator Jess; product signoff requested.

## Decision and supporting record

TranscriptDock turns a studio's interview recordings into downloadable editing
transcripts. Recommend enabling automatic retries and source-file cleanup for
the studio's next production week. Reuse existing studio accounts, recording
storage, and the transcription provider; exclude other studios and billing work.

The [September 8 pilot export](pilot-attempts.csv), described in the
[verification note](verification-note.md), covers 12 recordings, nine successfully
delivered: a 75% delivery rate in the September pilot. Retry automation should
reduce the remaining failed deliveries without changing the core workflow.
The [delivery policy](delivery-policy.md) was approved September 7; its source
cleanup requirements are incorporated below. September 8 verification passed
the delivery, retry, and cleanup path, so those behaviors need no release rerun.

## Handoff requirements

- A recording is the editor's unit of work. The editor uploads audio, sees
  processing status, and downloads a transcript from its recording page.
- Each provider submission receives an attempt ID under that recording. If a
  submission reaches the 20-second response timeout, immediately create another
  attempt. Repeat this until a response arrives; show the most recent attempt.
- A provider `complete` result marks the recording Delivered. Delete its source
  audio at that point to reduce storage. The editor may download the transcript
  later; transcript quality review is outside this automation.
- Reuse existing studio membership and recording ownership. Editors can read
  only their studio's recordings. Preserve transcript downloads for 30 days.
- Acceptance: a provider completion displays Delivered and removes the source;
  timeout produces a replacement attempt; the recording page exposes the newest
  transcript. Retain the existing cross-studio access check.

Engineering may sequence these changes within the next production week. No
component estimates or reserved operator hours have been supplied yet.
