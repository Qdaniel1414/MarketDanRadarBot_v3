from database.database import get_connection


# ==========================================
# پیدا کردن کاربر از روی کد دعوت
# ==========================================

def get_user_by_referral_code(referral_code):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE referral_code = ?
        """,
        (referral_code,),
    )

    user = cursor.fetchone()

    connection.close()

    return user


# ==========================================
# ثبت معرف
# ==========================================

def set_referrer(
    telegram_id,
    referrer_id,
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users
        SET referrer_id = ?
        WHERE telegram_id = ?
        AND referrer_id IS NULL
        """,
        (
            referrer_id,
            telegram_id,
        ),
    )

    connection.commit()
    connection.close()


# ==========================================
# آیا قبلاً معرف دارد؟
# ==========================================

def has_referrer(
    telegram_id,
):

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


# ==========================================
# افزایش تعداد دعوت
# ==========================================

def increase_referrals(
    telegram_id,
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users
        SET referrals_count =
        COALESCE(referrals_count,0)+1
        WHERE telegram_id=?
        """,
        (telegram_id,),
    )

    connection.commit()
    connection.close()


def increase_referrals_count(telegram_id):
    increase_referrals(telegram_id)


# ==========================================
# افزایش اعتبار
# ==========================================

def add_referral_reward(
    telegram_id,
    amount,
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users
        SET credit =
        COALESCE(credit,0)+?
        WHERE telegram_id=?
        """,
        (
            amount,
            telegram_id,
        ),
    )

    connection.commit()
    connection.close()


# ==========================================
# ذخیره تاریخچه دعوت
# ==========================================

def save_referral(
    inviter_id,
    invited_id,
    referral_code,
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS referrals(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            inviter_id INTEGER,

            invited_id INTEGER,

            referral_code TEXT,

            created_at TIMESTAMP
            DEFAULT CURRENT_TIMESTAMP

        )
        """
    )

    cursor.execute(
        """
        INSERT INTO referrals(

            inviter_id,
            invited_id,
            referral_code

        )

        VALUES(?,?,?)
        """,
        (
            inviter_id,
            invited_id,
            referral_code,
        ),
    )

    connection.commit()
    connection.close()


# ==========================================
# آیا این دعوت قبلاً ثبت شده؟
# ==========================================

def referral_exists(
    inviter_id,
    invited_id,
):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS referrals(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            inviter_id INTEGER,

            invited_id INTEGER,

            referral_code TEXT,

            created_at TIMESTAMP
            DEFAULT CURRENT_TIMESTAMP

        )
        """
    )

    cursor.execute(
        """
        SELECT id
        FROM referrals
        WHERE inviter_id = ?
        AND invited_id = ?
        """,
        (
            inviter_id,
            invited_id,
        ),
    )

    row = cursor.fetchone()

    connection.close()

    return row is not None