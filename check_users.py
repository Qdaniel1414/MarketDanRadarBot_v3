import sqlite3

conn = sqlite3.connect("database/market.db")
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

cursor.execute("""
SELECT
    telegram_id,
    first_name,
    username,
    phone,
    referral_code,
    referrer_id,
    referrals_count,
    credit
FROM users
""")

users = cursor.fetchall()

print("=" * 80)

for user in users:
    print(dict(user))

print("=" * 80)

conn.close()