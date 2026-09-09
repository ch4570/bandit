# Slotlet scheduling policy

Synthetic fixture. Adopted product requirements in this fictional project;
not statements about real bookings or customers.

- A booking belongs to one authenticated customer, studio and 60-minute slot.
  Account login, booking lookup and ordinary cancellation already exist.
- The same studio cannot have two confirmed bookings for overlapping time.
- Only the booking's owner can request a reschedule. Rescheduling is available
  until 24 hours before the existing booking starts, using server time.
- A customer previews available target slots. Selecting a target can create a
  two-minute hold. A hold temporarily removes that target from availability
  for other customers; browsing alone creates no hold. Capacity belongs to the
  physical studio and slot, not to a particular browser tab.
- Hold expiry uses server time; displayed times use Asia/Seoul. All times sent
  to users identify the date and timezone. The visible countdown is advisory.
- A reschedule succeeds only when the new slot is confirmed and the old slot
  is released together. If the attempt fails or its hold expires, the original
  confirmed booking remains valid. The customer must be able to discover the
  actual confirmed booking after a failed network response.
- Payment, refunds, recurring bookings, calendar sync and new account systems
  are excluded. This studio charges the same prepaid entitlement per slot;
  existing entitlement is carried to the replacement on success.

The policy does not yet specify multiple simultaneous holds by the same owner,
the exact expiry boundary, or how a second browser tab should report an attempt
against an old booking state. Product may recommend these small rules.
