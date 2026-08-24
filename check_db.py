import sqlite3
import os

db = os.path.abspath("database/market.db")

print("DATABASE:")
print(db)
print()

print("FILE EXISTS:")
print(os.path.exists(db))
print()

print("FILE SIZE:")
print(os.path.getsize(db))
print()

conn = sqlite3.connect(db)

print("DATABASE LIST:")

rows = conn.execute(
    "PRAGMA database_list"
).fetchall()

for row in rows:
    print(row)

print()

print("TABLES:")

rows = conn.execute(
    "SELECT type, name, tbl_name "
    "FROM sqlite_master "
    "ORDER BY type, name"
).fetchall()

for row in rows:
    print(row)

print()

print("USERS COUNT:")

try:
    count = conn.execute(
        "SELECT COUNT(*) FROM users"
    ).fetchone()[0]

    print(count)

except Exception as e:
    print("USERS TABLE ERROR:", repr(e))

conn.close()