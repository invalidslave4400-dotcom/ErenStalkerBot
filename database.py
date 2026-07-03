import sqlite3

conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

# Users
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    first_name TEXT,
    credits INTEGER DEFAULT 0,
    referrals INTEGER DEFAULT 0,
    premium INTEGER DEFAULT 0,
    free_referrals INTEGER DEFAULT 2
)
""")

# Referrals
cursor.execute("""
CREATE TABLE IF NOT EXISTS referrals(
    referrer_id INTEGER,
    referred_id INTEGER UNIQUE
)
""")

# Protected Numbers
cursor.execute("""
CREATE TABLE IF NOT EXISTS protected_numbers(
    phone TEXT UNIQUE,
    protected_by TEXT
)
""")

conn.commit()


def add_user(user_id, username, first_name):
    cursor.execute(
        "INSERT OR IGNORE INTO users VALUES(?,?,?,?,?,?,?)",
        (user_id, username, first_name, 0, 0, 0, 2)
    )
    conn.commit()


def get_credits(user_id):
    cursor.execute(
        "SELECT credits FROM users WHERE user_id=?",
        (user_id,)
    )
    data = cursor.fetchone()
    return data[0] if data else 0


def add_credits(user_id, amount):
    cursor.execute(
        "UPDATE users SET credits=credits+? WHERE user_id=?",
        (amount, user_id)
    )
    conn.commit()


def remove_credit(user_id):
    cursor.execute(
        "UPDATE users SET credits=credits-1 WHERE user_id=?",
        (user_id,)
    )
    conn.commit()
