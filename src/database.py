import sqlite3
from datetime import datetime

DB_NAME = "water_tracker.db"  # file name for database

def create_table():
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS water_intake(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            intake_ml INTEGER,
            date TEXT,
            user_id TEXT
        )
    """)

    con.commit()
    con.close()


def log_intake(user_id, intake_ml):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    date_today = datetime.today().strftime('%Y-%m-%d')

    cur.execute(
        """INSERT INTO water_intake (intake_ml, date, user_id) VALUES (?, ?, ?)""",
        (intake_ml, date_today, user_id)
    )

    con.commit()
    con.close()


def get_intake_history(user_id, date=None):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    if date:
        cur.execute(
            """SELECT intake_ml, date FROM water_intake WHERE user_id=? AND date=?""",
            (user_id, date)
        )
    else:
        cur.execute(
            """SELECT intake_ml, date FROM water_intake WHERE user_id=?""",
            (user_id,)
        )

    records = cur.fetchall()
    con.close()
    return records


# Initialize table
create_table()

# Example usage:
# insert_table("user123", 500)
# print(get_intake_history("user123"))
