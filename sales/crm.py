#!/usr/bin/env python3
"""
Simple, honest CRM for the agency. SQLite-backed. Real data only.

Usage:
  python3 sales/crm.py init
  python3 sales/crm.py add --name "Bella Foods" --industry restaurant \
      --location "Lagos" --website none --social "@bellafoods" \
      --contact whatsapp --problem "Menu only in bio; customers DM for prices" \
      --offer "WhatsApp Ordering System" --pitch "I noticed customers DM to..." \
      --channel instagram
  python3 sales/crm.py list [--stage INTERESTED] [--industry restaurant]
  python3 sales/crm.py show <id>
  python3 sales/crm.py stage <id> CONTACTED [--response "..."] [--result "..."]
  python3 sales/crm.py note <id> "text to append to result"
  python3 sales/crm.py followups            # due today or overdue
  python3 sales/crm.py stopcontact <id>     # mark do-not-contact + LOST
  python3 sales/crm.py paid <id> --amount 30000
  python3 sales/crm.py export                # write leads.csv
  python3 sales/crm.py stats                 # quick funnel snapshot

Every write refuses fabricated shortcuts: it stores exactly what you pass.
"""
import argparse
import csv
import os
import sqlite3
import sys
from datetime import date, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, "leads", "crm.db")
CSV_PATH = os.path.join(HERE, "leads", "leads.csv")

STAGES = ["PROSPECT", "CONTACTED", "REPLIED", "INTERESTED", "DEMO", "QUOTE",
          "NEGOTIATION", "PAID", "DELIVERING", "COMPLETED", "REFERRAL",
          "RETAINER", "LOST"]

COLUMNS = ["id", "business_name", "industry", "location", "website", "social",
           "contact_method", "contact_value", "problem", "recommended_offer",
           "pitch_angle", "channel", "stage", "response", "follow_up_date",
           "result", "do_not_contact", "revenue", "created_at", "updated_at"]


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def connect():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    os.makedirs(os.path.dirname(DB), exist_ok=True)
    conn = connect()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            business_name TEXT NOT NULL,
            industry TEXT,
            location TEXT,
            website TEXT,
            social TEXT,
            contact_method TEXT,
            contact_value TEXT,
            problem TEXT,
            recommended_offer TEXT,
            pitch_angle TEXT,
            channel TEXT,
            stage TEXT DEFAULT 'PROSPECT',
            response TEXT,
            follow_up_date TEXT,
            result TEXT,
            do_not_contact INTEGER DEFAULT 0,
            revenue REAL DEFAULT 0,
            created_at TEXT,
            updated_at TEXT
        )
    """)
    conn.commit()
    conn.close()
    print(f"CRM database ready at {DB}")


def cmd_add(a):
    init_db()
    conn = connect()
    conn.execute("""
        INSERT INTO leads (business_name, industry, location, website, social,
            contact_method, contact_value, problem, recommended_offer,
            pitch_angle, channel, stage, follow_up_date, created_at, updated_at)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (a.name, a.industry, a.location, a.website, a.social, a.contact,
          a.contact_value, a.problem, a.offer, a.pitch, a.channel,
          "PROSPECT", a.followup, now(), now()))
    conn.commit()
    lead_id = conn.execute("SELECT last_insert_rowid() AS id").fetchone()["id"]
    conn.close()
    print(f"Added lead #{lead_id}: {a.name} (PROSPECT)")


def _print_row(r):
    dnc = "  [DO-NOT-CONTACT]" if r["do_not_contact"] else ""
    print(f"#{r['id']:>3}  {r['stage']:<11} {r['business_name']}{dnc}")
    print(f"      {r['industry'] or '-'} | {r['location'] or '-'} | "
          f"{r['contact_method'] or '-'} {r['contact_value'] or ''}")
    if r["problem"]:
        print(f"      problem : {r['problem']}")
    if r["recommended_offer"]:
        print(f"      offer   : {r['recommended_offer']}")
    if r["follow_up_date"]:
        print(f"      follow-up: {r['follow_up_date']}")


def cmd_list(a):
    if not os.path.exists(DB):
        print("No CRM yet. Run: python3 sales/crm.py add ...")
        return
    conn = connect()
    q = "SELECT * FROM leads WHERE 1=1"
    params = []
    if a.stage:
        q += " AND stage=?"
        params.append(a.stage.upper())
    if a.industry:
        q += " AND industry=?"
        params.append(a.industry)
    q += " ORDER BY updated_at DESC"
    rows = conn.execute(q, params).fetchall()
    conn.close()
    if not rows:
        print("No leads match. (This is real data — it's empty until you add some.)")
        return
    for r in rows:
        _print_row(r)
    print(f"\n{len(rows)} lead(s).")


def cmd_show(a):
    conn = connect()
    r = conn.execute("SELECT * FROM leads WHERE id=?", (a.id,)).fetchone()
    conn.close()
    if not r:
        print(f"No lead #{a.id}")
        return
    for c in COLUMNS:
        print(f"{c:>18}: {r[c]}")


def cmd_stage(a):
    if a.stage.upper() not in STAGES:
        print(f"Invalid stage. Use one of: {', '.join(STAGES)}")
        sys.exit(1)
    conn = connect()
    r = conn.execute("SELECT * FROM leads WHERE id=?", (a.id,)).fetchone()
    if not r:
        print(f"No lead #{a.id}")
        return
    if r["do_not_contact"] and a.stage.upper() not in ("LOST",):
        print("This lead is marked do-not-contact. Not advancing.")
        return
    fields = {"stage": a.stage.upper(), "updated_at": now()}
    if a.response:
        fields["response"] = a.response
    if a.result:
        fields["result"] = a.result
    if a.followup:
        fields["follow_up_date"] = a.followup
    sets = ", ".join(f"{k}=?" for k in fields)
    conn.execute(f"UPDATE leads SET {sets} WHERE id=?",
                 (*fields.values(), a.id))
    conn.commit()
    conn.close()
    print(f"Lead #{a.id} -> {a.stage.upper()}")


def cmd_note(a):
    conn = connect()
    r = conn.execute("SELECT result FROM leads WHERE id=?", (a.id,)).fetchone()
    if not r:
        print(f"No lead #{a.id}")
        return
    existing = (r["result"] + "\n") if r["result"] else ""
    stamped = f"{existing}[{now()}] {a.text}"
    conn.execute("UPDATE leads SET result=?, updated_at=? WHERE id=?",
                 (stamped, now(), a.id))
    conn.commit()
    conn.close()
    print(f"Note added to #{a.id}")


def cmd_followups(a):
    if not os.path.exists(DB):
        print("No CRM yet.")
        return
    today = date.today().isoformat()
    conn = connect()
    rows = conn.execute("""
        SELECT * FROM leads
        WHERE do_not_contact=0
          AND follow_up_date IS NOT NULL AND follow_up_date != ''
          AND follow_up_date <= ?
          AND stage NOT IN ('PAID','DELIVERING','COMPLETED','LOST','RETAINER')
        ORDER BY follow_up_date ASC
    """, (today,)).fetchall()
    conn.close()
    if not rows:
        print("No follow-ups due. (Add leads and set --followup dates.)")
        return
    print(f"Follow-ups due (on/before {today}):\n")
    for r in rows:
        print(f"#{r['id']} {r['business_name']} ({r['stage']}) "
              f"due {r['follow_up_date']} via {r['channel'] or r['contact_method']}")


def cmd_stopcontact(a):
    conn = connect()
    conn.execute("UPDATE leads SET do_not_contact=1, stage='LOST', "
                 "result=COALESCE(result,'')||? , updated_at=? WHERE id=?",
                 (f"\n[{now()}] Marked do-not-contact.", now(), a.id))
    conn.commit()
    conn.close()
    print(f"Lead #{a.id} marked do-not-contact and LOST. Will not be contacted.")


def cmd_paid(a):
    conn = connect()
    conn.execute("UPDATE leads SET stage='PAID', revenue=?, updated_at=? "
                 "WHERE id=?", (a.amount, now(), a.id))
    conn.commit()
    conn.close()
    print(f"Lead #{a.id} -> PAID, revenue recorded: {a.amount}")


def cmd_export(a):
    if not os.path.exists(DB):
        print("No CRM yet.")
        return
    conn = connect()
    rows = conn.execute("SELECT * FROM leads ORDER BY id").fetchall()
    conn.close()
    with open(CSV_PATH, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(COLUMNS)
        for r in rows:
            w.writerow([r[c] for c in COLUMNS])
    print(f"Exported {len(rows)} lead(s) to {CSV_PATH}")


def cmd_stats(a):
    if not os.path.exists(DB):
        print("No CRM yet.")
        return
    conn = connect()
    total = conn.execute("SELECT COUNT(*) c FROM leads").fetchone()["c"]
    print(f"Total leads: {total}")
    if total == 0:
        conn.close()
        return
    print("\nBy stage:")
    for s in STAGES:
        c = conn.execute("SELECT COUNT(*) c FROM leads WHERE stage=?",
                         (s,)).fetchone()["c"]
        if c:
            print(f"  {s:<12} {c}")
    rev = conn.execute("SELECT COALESCE(SUM(revenue),0) r FROM leads").fetchone()["r"]
    paid = conn.execute("SELECT COUNT(*) c FROM leads WHERE revenue>0").fetchone()["c"]
    contacted = conn.execute(
        "SELECT COUNT(*) c FROM leads WHERE stage NOT IN ('PROSPECT')").fetchone()["c"]
    print(f"\nContacted: {contacted}  |  Paying clients: {paid}  |  "
          f"Revenue: ₦{rev:,.0f}")
    if contacted:
        print(f"Contacted -> paid conversion: {paid/contacted*100:.1f}%")
    conn.close()


def build_parser():
    p = argparse.ArgumentParser(description="Agency CRM (real data only).")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init")

    a = sub.add_parser("add")
    a.add_argument("--name", required=True)
    a.add_argument("--industry", default="")
    a.add_argument("--location", default="")
    a.add_argument("--website", default="")
    a.add_argument("--social", default="")
    a.add_argument("--contact", default="", help="channel: whatsapp/instagram/...")
    a.add_argument("--contact-value", dest="contact_value", default="")
    a.add_argument("--problem", default="")
    a.add_argument("--offer", default="")
    a.add_argument("--pitch", default="")
    a.add_argument("--channel", default="")
    a.add_argument("--followup", default="", help="YYYY-MM-DD")

    l = sub.add_parser("list")
    l.add_argument("--stage", default="")
    l.add_argument("--industry", default="")

    s = sub.add_parser("show")
    s.add_argument("id", type=int)

    st = sub.add_parser("stage")
    st.add_argument("id", type=int)
    st.add_argument("stage")
    st.add_argument("--response", default="")
    st.add_argument("--result", default="")
    st.add_argument("--followup", default="")

    n = sub.add_parser("note")
    n.add_argument("id", type=int)
    n.add_argument("text")

    sub.add_parser("followups")

    sc = sub.add_parser("stopcontact")
    sc.add_argument("id", type=int)

    pd = sub.add_parser("paid")
    pd.add_argument("id", type=int)
    pd.add_argument("--amount", type=float, required=True)

    sub.add_parser("export")
    sub.add_parser("stats")
    return p


def main():
    args = build_parser().parse_args()
    dispatch = {
        "init": lambda a: init_db(),
        "add": cmd_add, "list": cmd_list, "show": cmd_show, "stage": cmd_stage,
        "note": cmd_note, "followups": cmd_followups,
        "stopcontact": cmd_stopcontact, "paid": cmd_paid,
        "export": cmd_export, "stats": cmd_stats,
    }
    dispatch[args.cmd](args)


if __name__ == "__main__":
    main()
