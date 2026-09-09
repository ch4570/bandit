# Staff walkthrough notes

Synthetic fixture. Fictional walkthrough observations, not executed product
tests or real support incidents. The team used clickable screens only.

- Hana used two tabs. Tab A selected Tuesday 10:00 and Tab B selected Wednesday
  11:00 for the same original booking. Both tabs still showed a Confirm button.
- Joon asked whether pressing Confirm again after a dropped connection would
  create another booking. The mockup had no answer about the server's state.
- Mina's browser was backgrounded. On return, its countdown still showed eight
  seconds, although more than two minutes had passed on the wall clock.
- A studio manager asked what another customer sees when trying to take the
  same target while the first hold is active or precisely when it expires.
- The team has not measured integration work against the existing cancellation
  service, and has not tested any reservation concurrency or network recovery.
