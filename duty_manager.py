# ============================================================================
# duty_manager.py
# אחריות: לוגיקה עסקית של ניהול תורנויות
# ============================================================================
from utils import *


def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str, data:list) -> None:
    """
    מוסיפה תורנות חדשה לחייל.

    סוג: לוגיקה עסקית (Business Logic)

    מקבלת:
        soldier_id (int): מספר אישי של החייל
        duty_name (str): שם התורנות
        day (str): יום בשבוע (sunday/monday/tuesday/wednesday/thursday)

    מחזירה:
        None - הפונקציה מוסיפה את התורנות או זורקת exception

    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
        ValueError: אם תורנות עם שם זה כבר קיימת לחייל
        ValueError: אם day לא חוקי (friday/saturday או ערך לא תקין)

    למה הפונקציה קיימת:
    לוגיקה עסקית של הוספת תורנות.
    מבצעת בדיקות ומוסיפה תורנות לחייל.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    soldier = find_soldier_by_id(soldier_id, data)
    if not soldier:
        raise KeyError("Soldier not in system - non exist ID")
    if soldier_has_duty(soldier, duty_name):
        raise ValueError("Soldier already has this duty")
    if not is_valid_day(day):
        raise ValueError("Invalid day")
    soldier["duties"].append({"name": duty_name, "day": day, "status": "pending"})


def update_duty_status(soldier_id: int, duty_name: str, new_status: str, data:list) -> None:
    """
    מעדכנת את הסטטוס של תורנות.

    סוג: לוגיקה עסקית (Business Logic)

    מקבלת:
        soldier_id (int): מספר אישי של החייל
        duty_name (str): שם התורנות
        new_status (str): סטטוס חדש (pending/completed/missed)

    מחזירה:
        None - הפונקציה מעדכנת את הסטטוס או זורקת exception

    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
        KeyError: אם תורנות עם שם זה לא נמצאה לחייל
        ValueError: אם new_status לא חוקי (לא pending/completed/missed)

    למה הפונקציה קיימת:
    לוגיקה עסקית של עדכון סטטוס.
    מבצעת בדיקות ומעדכנת את הסטטוס.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    soldier = find_soldier_by_id(soldier_id, data)
    if not soldier:
        raise KeyError("Soldier not in system - non exist ID")
    if not soldier_has_duty(soldier, duty_name):
        raise KeyError("Soldier don't has this duty")
    if not is_valid_status(new_status):
        raise ValueError("Invalid status")
    duty = [d for d in soldier["duties"] if d["name"] == duty_name][0]
    duty["status"] = new_status


def get_soldier_duties(soldier_id: int, data:list) -> list:
    """
    מחזירה את רשימת התורנויות של חייל.

    סוג: גישה לנתונים (Data Access)

    מקבלת:
        soldier_id (int): מספר אישי של החייל

    מחזירה:
        list: רשימת תורנויות (מילונים)
              רשימה ריקה אם אין תורנויות

    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת

    למה הפונקציה קיימת:
    גישה מבוקרת לתורנויות של חייל.
    מפרידה בין הנתונים לבין הגישה אליהם.
    זורקת exception אם החייל לא קיים (במקום להחזיר רשימה ריקה).
    """
    soldier = find_soldier_by_id(soldier_id, data)
    if not soldier:
        raise KeyError("Soldier not in system - non exist ID")
    return soldier["duties"]

