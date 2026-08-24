import random
import string

from database.database import get_connection


def generate_referral_code(length=8):

    characters = string.ascii_uppercase + string.digits

    while True:

        code = "".join(
            random.choice(characters)
            for _ in range(length)
        )

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id
            FROM users
            WHERE referral_code = ?
            """,
            (code,),
        )

        exists = cursor.fetchone()

        connection.close()

        if not exists:
            return code


def add_user(
    telegram_id,
    first_name,
    last_name,
    username,
    phone,
):

    referral_code = generate_referral_code()

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO users
        (
            telegram_id,
            first_name,
            last_name,
            username,
            phone,
            role,
            subscription_type,
            wallet_balance,
            credit,
            referral_code
        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            telegram_id,
            first_name,
            last_name,
            username,
            phone,
            "member",
            "free",
            0,
            0,
            referral_code,
        ),
    )

    connection.commit()

    connection.close()


def is_registered(telegram_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id
        FROM users
        WHERE telegram_id = ?
        """,
        (telegram_id,),
    )

    user = cursor.fetchone()

    connection.close()

    return user is not None


def get_user(telegram_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE telegram_id = ?
        """,
        (telegram_id,),
    )

    user = cursor.fetchone()

    connection.close()

    return user


def update_login(telegram_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users
        SET
            login_count = login_count + 1,
            last_login = CURRENT_TIMESTAMP,
            updated_at = CURRENT_TIMESTAMP
        WHERE telegram_id = ?
        """,
        (telegram_id,),
    )

    connection.commit()

    connection.close()


def initialize_user_data(telegram_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users
        SET
            subscription_type = COALESCE(subscription_type, 'free'),
            wallet_balance = COALESCE(wallet_balance, 0),
            credit = COALESCE(credit, 0),
            role = COALESCE(role, 'member')
        WHERE telegram_id = ?
        """,
        (telegram_id,),
    )

    connection.commit()

    connection.close()