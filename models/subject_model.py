from models.db import get_db
from datetime import datetime

def add_subject(name, days, present, absent, goal):
    db = get_db()
    cursor = db.cursor()

    query = """
        INSERT INTO subjects (name, days, present, absent, goal)
        VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(query, (name, days, present, absent, goal))
    db.commit()

    cursor.close()
    db.close()


def get_all_subjects():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM subjects")
    subjects = cursor.fetchall()

    cursor.close()
    db.close()

    return subjects


def get_subject(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM subjects WHERE id=%s", (id,))
    subject = cursor.fetchone()

    cursor.close()
    db.close()

    return subject


def update_subject(id, name, days, present, absent, goal):
    db = get_db()
    cursor = db.cursor()

    query = """
        UPDATE subjects
        SET name=%s, days=%s, present=%s, absent=%s, goal=%s
        WHERE id=%s
    """

    cursor.execute(query, (name, days, present, absent, goal, id))
    db.commit()

    cursor.close()
    db.close()


def delete_subject(id):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("DELETE FROM subjects WHERE id=%s", (id,))
    db.commit()

    cursor.close()
    db.close()


def mark_attendance(id, action):
    db = get_db()
    cursor = db.cursor()

    if action == "present":
        cursor.execute(
            "UPDATE subjects SET present = present + 1 WHERE id=%s", (id,)
        )

    elif action == "absent":
        cursor.execute(
            "UPDATE subjects SET absent = absent + 1 WHERE id=%s", (id,)
        )

    db.commit()

    cursor.close()
    db.close()


def calculate_percentage(present, absent):
    total = present + absent

    if total == 0:
        return 0

    return round((present / total) * 100)


def get_summary():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            COALESCE(SUM(present),0) AS present,
            COALESCE(SUM(absent),0) AS absent
        FROM subjects
    """)

    summary = cursor.fetchone()

    cursor.close()
    db.close()

    return summary


def get_today_subjects():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    today = datetime.now().strftime("%A").lower()

    cursor.execute("""
        SELECT id, name, days, present, absent
        FROM subjects
    """)

    subjects = cursor.fetchall()

    today_subjects = []

    for s in subjects:
        if s["days"]:
            days_list = [d.strip().lower() for d in s["days"].split(",")]

            if today in days_list:
                today_subjects.append(s)

    cursor.close()
    db.close()

    return today_subjects


def attendance_advice(present, absent, goal):
    total = present + absent

    if total == 0:
        return {
            "percentage": 0,
            "can_bunk": 0,
            "need_attend": 0,
            "status": "No data"
        }

    percentage = (present / total) * 100
    required_present = (goal * total) / 100

    if percentage >= goal:
        can_bunk = int((present * 100 / goal) - total)

        return {
            "percentage": round(percentage, 1),
            "can_bunk": max(0, can_bunk),
            "need_attend": 0,
            "status": "Safe "
        }
    else:
        need_attend = int(required_present - present + 1)

        return {
            "percentage": round(percentage, 1),
            "can_bunk": 0,
            "need_attend": max(0, need_attend),
            "status": "Low "
        }
