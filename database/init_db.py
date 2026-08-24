from database.database import get_connection


def add_column(cursor, table_name, column_name, column_definition):

    cursor.execute(f"PRAGMA table_info({table_name})")

    columns = [column[1] for column in cursor.fetchall()]

    if column_name not in columns:

        cursor.execute(
            f"""
            ALTER TABLE {table_name}
            ADD COLUMN {column_name} {column_definition}
            """
        )


def create_tables():

    connection = get_connection()

    cursor = connection.cursor()

    # ==========================================================
    # USERS
    # ==========================================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            telegram_id INTEGER UNIQUE NOT NULL,

            first_name TEXT,

            last_name TEXT,

            username TEXT,

            phone TEXT,

            is_active INTEGER DEFAULT 1,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """
    )

    add_column(cursor, "users", "role", "TEXT DEFAULT 'member'")
    add_column(cursor, "users", "subscription_type", "TEXT DEFAULT 'free'")
    add_column(cursor, "users", "subscription_expire", "TIMESTAMP")
    add_column(cursor, "users", "wallet_balance", "INTEGER DEFAULT 0")
    add_column(cursor, "users", "credit", "INTEGER DEFAULT 0")

    add_column(cursor, "users", "referral_code", "TEXT")
    add_column(cursor, "users", "referred_by", "TEXT")
    add_column(cursor, "users", "pending_referral_code", "TEXT")

    add_column(cursor, "users", "referrer_id", "INTEGER")
    add_column(cursor, "users", "referrals_count", "INTEGER DEFAULT 0")
    add_column(cursor, "users", "referral_reward", "INTEGER DEFAULT 0")

    add_column(cursor, "users", "login_count", "INTEGER DEFAULT 0")
    add_column(cursor, "users", "last_login", "TIMESTAMP")
    add_column(cursor, "users", "updated_at", "TIMESTAMP")

    # ==========================================================
    # REFERRALS
    # ==========================================================

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS referrals (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            inviter_id INTEGER NOT NULL,

            invited_id INTEGER UNIQUE NOT NULL,

            referral_code TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """
    )

    connection.commit()

    connection.close()


if __name__ == "__main__":
    create_tables()