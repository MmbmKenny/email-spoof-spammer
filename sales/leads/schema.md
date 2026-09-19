# Lead Record Schema

Stored in `sales/leads/crm.db` (SQLite). Mirrored to `leads.csv` on export.
**Only real, observed data goes in here.** No fabricated leads.

| Field | Type | Notes |
|-------|------|-------|
| id | int | Auto |
| business_name | text | Required |
| industry | text | restaurant, salon, boutique, etc. |
| location | text | City/area |
| website | text | URL or "none" |
| social | text | Handle(s) |
| contact_method | text | whatsapp / instagram / facebook / email / linkedin / form |
| contact_value | text | number / handle / email (optional) |
| problem | text | The ONE observable problem |
| recommended_offer | text | One of the 7 offers |
| pitch_angle | text | Personalized opening line (based on the real problem) |
| channel | text | Best outreach channel |
| stage | text | See docs/sales-funnel.md |
| response | text | What they said (verbatim-ish) |
| follow_up_date | text | YYYY-MM-DD |
| result | text | Free text outcome |
| do_not_contact | int | 1 = never contact again |
| revenue | real | ₦ received (only when actually paid) |
| created_at | text | Auto timestamp |
| updated_at | text | Auto timestamp |

Stages: PROSPECT, CONTACTED, REPLIED, INTERESTED, DEMO, QUOTE, NEGOTIATION,
PAID, DELIVERING, COMPLETED, REFERRAL, RETAINER, LOST.
