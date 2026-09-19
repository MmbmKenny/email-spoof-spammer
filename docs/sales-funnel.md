# Sales Funnel — Stage Definitions

These are the exact stage values used by the CRM (`sales/crm.py`). A lead moves
forward only when the real-world event has actually happened.

| Stage | Means | Enter when |
|-------|-------|-----------|
| `PROSPECT` | Researched, not yet contacted | Added to CRM with a genuine problem identified |
| `CONTACTED` | First message actually sent | You sent the approved outreach (record the date) |
| `REPLIED` | They responded (any response) | A real reply arrives |
| `INTERESTED` | Positive signal / wants to know more | They ask a question, want a demo, or say "tell me more" |
| `DEMO` | Shown a relevant demo | You shared a demo link or did a walkthrough |
| `QUOTE` | Sent a price/proposal | Proposal + quotation delivered |
| `NEGOTIATION` | Discussing scope/price | Back-and-forth on terms |
| `PAID` | Deposit or full payment received | Money actually received |
| `DELIVERING` | Building the project | Work started |
| `COMPLETED` | Delivered and accepted | Client has the finished work |
| `REFERRAL` | Asked for / gave an introduction | Post-delivery |
| `RETAINER` | Ongoing paid relationship | Recurring arrangement agreed |
| `LOST` | Not moving forward | They declined, ghosted after follow-ups, or asked to stop |

## Rules
- Never mark `CONTACTED` unless the message was truly sent.
- Never mark `PAID` unless money was truly received.
- `LOST` after: no reply following the Day-1 / Day-3 / Day-7 sequence, an explicit
  no, or a request not to be contacted (also set do-not-contact).
- A conversion rate is only meaningful on real recorded data. The dashboard
  computes rates from the CRM; it never invents numbers.
