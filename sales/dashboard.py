#!/usr/bin/env python3
"""
Render sales/sales-dashboard.html from the CRM database.

Uses ONLY real recorded data. If the CRM is empty, the dashboard says so
honestly instead of showing invented numbers.

Usage: python3 sales/dashboard.py  ->  open sales/sales-dashboard.html
"""
import os
import sqlite3
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, "leads", "crm.db")
OUT = os.path.join(HERE, "sales-dashboard.html")

STAGES = ["PROSPECT", "CONTACTED", "REPLIED", "INTERESTED", "DEMO", "QUOTE",
          "NEGOTIATION", "PAID", "DELIVERING", "COMPLETED", "REFERRAL",
          "RETAINER", "LOST"]


def load():
    if not os.path.exists(DB):
        return None
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM leads").fetchall()
    conn.close()
    return rows


def pct(n, d):
    return f"{(n / d * 100):.1f}%" if d else "—"


def build_metrics(rows):
    total = len(rows)
    by_stage = {s: 0 for s in STAGES}
    by_industry = {}
    by_channel = {}
    by_offer = {}
    revenue = 0.0
    for r in rows:
        by_stage[r["stage"]] = by_stage.get(r["stage"], 0) + 1
        if r["industry"]:
            by_industry[r["industry"]] = by_industry.get(r["industry"], 0) + 1
        if r["channel"]:
            by_channel[r["channel"]] = by_channel.get(r["channel"], 0) + 1
        if r["recommended_offer"]:
            by_offer[r["recommended_offer"]] = by_offer.get(r["recommended_offer"], 0) + 1
        revenue += (r["revenue"] or 0)
    contacted = total - by_stage.get("PROSPECT", 0)
    replied = sum(by_stage.get(s, 0) for s in
                  ["REPLIED", "INTERESTED", "DEMO", "QUOTE", "NEGOTIATION",
                   "PAID", "DELIVERING", "COMPLETED", "REFERRAL", "RETAINER"])
    interested = sum(by_stage.get(s, 0) for s in
                     ["INTERESTED", "DEMO", "QUOTE", "NEGOTIATION", "PAID",
                      "DELIVERING", "COMPLETED", "REFERRAL", "RETAINER"])
    demos = sum(by_stage.get(s, 0) for s in
                ["DEMO", "QUOTE", "NEGOTIATION", "PAID", "DELIVERING",
                 "COMPLETED", "REFERRAL", "RETAINER"])
    proposals = sum(by_stage.get(s, 0) for s in
                    ["QUOTE", "NEGOTIATION", "PAID", "DELIVERING",
                     "COMPLETED", "REFERRAL", "RETAINER"])
    paid = sum(by_stage.get(s, 0) for s in
               ["PAID", "DELIVERING", "COMPLETED", "REFERRAL", "RETAINER"])
    return {
        "total": total, "contacted": contacted, "replied": replied,
        "interested": interested, "demos": demos, "proposals": proposals,
        "paid": paid, "revenue": revenue,
        "by_stage": by_stage, "by_industry": by_industry,
        "by_channel": by_channel, "by_offer": by_offer,
    }


def top(d):
    if not d:
        return "—"
    k = max(d, key=d.get)
    return f"{k} ({d[k]})"


def bars(d, total):
    if not d:
        return "<p class='muted'>No data yet.</p>"
    out = []
    for k, v in sorted(d.items(), key=lambda x: -x[1]):
        w = (v / total * 100) if total else 0
        out.append(
            f"<div class='row'><span class='lbl'>{k}</span>"
            f"<span class='bar'><i style='width:{w:.0f}%'></i></span>"
            f"<span class='val'>{v}</span></div>")
    return "\n".join(out)


CSS = """
:root{--bg:#0f1216;--card:#1a1f27;--ink:#e8ecf1;--muted:#8b95a3;
--accent:#3ba776;--line:#2a313c}
@media (prefers-color-scheme:light){:root:not([data-theme=dark]){
--bg:#f6f8fa;--card:#fff;--ink:#1a1f27;--muted:#5c6672;--accent:#2f8f63;--line:#e5e9ee}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);
font:15px/1.5 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;padding:24px}
h1{font-size:22px;margin:0 0 4px}.muted{color:var(--muted)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));
gap:12px;margin:20px 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px}
.card .n{font-size:28px;font-weight:700}.card .k{color:var(--muted);font-size:13px}
.panel{background:var(--card);border:1px solid var(--line);border-radius:12px;
padding:16px;margin:16px 0}
.row{display:flex;align-items:center;gap:10px;margin:6px 0}
.lbl{width:150px;font-size:13px}.val{width:36px;text-align:right;color:var(--muted)}
.bar{flex:1;background:var(--line);border-radius:6px;height:12px;overflow:hidden}
.bar i{display:block;height:100%;background:var(--accent)}
.empty{text-align:center;padding:60px 20px}
table{width:100%;border-collapse:collapse}td,th{padding:6px 8px;text-align:left;
border-bottom:1px solid var(--line);font-size:13px}
"""


def render(rows):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    if not rows:
        return f"""<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sales Dashboard</title><style>{CSS}</style></head><body>
<h1>Sales Dashboard</h1><p class="muted">Generated {ts}</p>
<div class="panel empty"><h2>No leads recorded yet</h2>
<p class="muted">This dashboard only ever shows real data from your CRM.<br>
Add prospects with <code>python3 sales/crm.py add ...</code>, then re-run
<code>python3 sales/dashboard.py</code>.</p></div></body></html>"""

    m = build_metrics(rows)
    cards = [
        ("Total prospects", m["total"]),
        ("Contacted", m["contacted"]),
        ("Replied", m["replied"]),
        ("Interested", m["interested"]),
        ("Demos shown", m["demos"]),
        ("Proposals", m["proposals"]),
        ("Paying clients", m["paid"]),
        ("Revenue", f"₦{m['revenue']:,.0f}"),
    ]
    card_html = "\n".join(
        f"<div class='card'><div class='n'>{v}</div><div class='k'>{k}</div></div>"
        for k, v in cards)

    conv_rows = [
        ("Contacted → Replied", pct(m["replied"], m["contacted"])),
        ("Replied → Interested", pct(m["interested"], m["replied"])),
        ("Interested → Proposal", pct(m["proposals"], m["interested"])),
        ("Proposal → Paid", pct(m["paid"], m["proposals"])),
        ("Contacted → Paid (overall)", pct(m["paid"], m["contacted"])),
    ]
    conv_html = "".join(
        f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in conv_rows)

    return f"""<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sales Dashboard</title><style>{CSS}</style></head><body>
<h1>Sales Dashboard</h1><p class="muted">Generated {ts} · real CRM data only</p>
<div class="grid">{card_html}</div>

<div class="panel"><h3>Conversion rates</h3>
<table>{conv_html}</table></div>

<div class="panel"><h3>By industry</h3>{bars(m['by_industry'], m['total'])}</div>
<div class="panel"><h3>Outreach channel performance</h3>{bars(m['by_channel'], m['total'])}</div>
<div class="panel"><h3>Recommended offer distribution</h3>{bars(m['by_offer'], m['total'])}</div>

<div class="panel"><h3>Highlights</h3>
<p>Most active industry: <b>{top(m['by_industry'])}</b><br>
Most used channel: <b>{top(m['by_channel'])}</b><br>
Most recommended offer: <b>{top(m['by_offer'])}</b></p></div>
</body></html>"""


def main():
    rows = load()
    html = render(rows or [])
    with open(OUT, "w") as f:
        f.write(html)
    n = len(rows) if rows else 0
    print(f"Dashboard written to {OUT} ({n} lead(s)).")


if __name__ == "__main__":
    main()
