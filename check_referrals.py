import sqlite3

conn = sqlite3.connect("database/market.db")
conn.row_factory = sqlite3.Row

rows = conn.execute(
    "SELECT * FROM referrals ORDER BY id"
).fetchall()

print("=" * 80)
print("REFERRALS")
print("=" * 80)

if not rows:
    print("NO REFERRALS FOUND")
else:
    for row in rows:
        print(dict(row))

print("=" * 80)

conn.close()