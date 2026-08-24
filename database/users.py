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

def create_referral_code_if_missing(telegram_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT referral_code
        FROM users
        WHERE telegram_id = ?
        """,
        (telegram_id,),
    )

    user = cursor.fetchone()

    if user is None:

        connection.close()

        return

    if user["referral_code"]:

        connection.close()

        return

    referral_code = generate_referral_code()

    cursor.execute(
        """
        UPDATE users
        SET referral_code = ?
        WHERE telegram_id = ?
        """,
        (
            referral_code,
            telegram_id,
        ),
    )

    connection.commit()

    connection.close()    

def save_pending_referral_code(telegram_id, referral_code):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users
        SET pending_referral_code = ?
        WHERE telegram_id = ?
        """,
        (
            referral_code,
            telegram_id,
        ),
    )

    connection.commit()

    connection.close()


def get_pending_referral_code(telegram_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT pending_referral_code
        FROM users
        WHERE telegram_id = ?
        """,
        (telegram_id,),
    )

    user = cursor.fetchone()

    connection.close()

    if user is None:
        return None

    return user["pending_referral_code"]


def clear_pending_referral_code(telegram_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users
        SET pending_referral_code = NULL
        WHERE telegram_id = ?
        """,
        (telegram_id,),
    )

    connection.commit()

    connection.close()
    # ==========================================
# Referral System
# ==========================================

def get_user_by_referral_code(referral_code):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT telegram_id
        FROM users
        WHERE referral_code = ?
        """,
        (referral_code,),
    )

    user = cursor.fetchone()

    connection.close()

    if user:
        return user["telegram_id"]

    return None


def has_referrer(telegram_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT referrer_id
        FROM users
        WHERE telegram_id = ?
        """,
        (telegram_id,),
    )

    user = cursor.fetchone()

    connection.close()

    if user is None:
        return False

    return user["referrer_id"] is not None


def set_referrer(invited_id, inviter_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users
        SET referrer_id = ?
        WHERE telegram_id = ?
        """,
        (
            inviter_id,
            invited_id,
        ),
    )

    connection.commit()
    connection.close()


def increase_referrals(inviter_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users
        SET referrals_count = referrals_count + 1
        WHERE telegram_id = ?
        """,
        (inviter_id,),
    )

    connection.commit()
    connection.close()


def add_referral_reward(inviter_id, amount):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users
        SET

            referral_reward = referral_reward + ?,

            wallet_balance = wallet_balance + ?

        WHERE telegram_id = ?
        """,
        (
            amount,
            amount,
            inviter_id,
        ),
    )

    connection.commit()
    connection.close()


def save_referral(inviter_id, invited_id, referral_code):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO referrals(

            inviter_id,

            invited_id,

            referral_code

        )

        VALUES (?, ?, ?)
        """,
        (
            inviter_id,
            invited_id,
            referral_code,
        ),
    )

    connection.commit()
    connection.close()