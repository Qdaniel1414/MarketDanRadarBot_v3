import sqlite3

conn = sqlite3.connect("database/market.db")

tables = conn.execute(
    "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
).fetchall()

print("=" * 60)
print("TABLES")
print("=" * 60)

for table in tables:
    print(table[0])

print("=" * 60)

conn.close()