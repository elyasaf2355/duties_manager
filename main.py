# ============================================================================
# main.py
# אחריות: תפריט ראשי, קלט מהמשתמש, ניתוב לפונקציות
# ============================================================================
from soldier_manager import *
from duty_manager import *

def show_menu() -> None:
    """
    מציגה את התפריט הראשי למשתמש.

    מקבלת: כלום
    מחזירה: כלום (מדפיסה לקונסול)

    למה הפונקציה קיימת:
    הפרדה בין הצגת התפריט לבין הלוגיקה העסקית.
    אם נרצה לשנות את התצוגה, נשנה רק כאן.
    """
    print(
        f"""
{"=" * 40}
Soldiers Duties Managment
{"=" * 40}
1. Add soldier
2. Remove soldier
3. Show all soldiers
4. Add duty
5. Update duty status
6. Show soldier duties
{"-" * 40}
Enter '0' to EXIT
{"=" * 40}
        """
    )


def get_user_choice() -> str:
    """
    מקבלת בחירה מהמשתמש.

    מקבלת: כלום
    מחזירה: מחרוזת המייצגת את בחירת המשתמש

    למה הפונקציה קיימת:
    הפרדת קבלת קלט מהמשתמש מהלוגיקה של עיבוד הבחירה.
    מאפשר להחליף את שיטת הקלט בעתיד (למשל, GUI).
    """
    return input("Your choice: ")


def handle_add_soldier() -> None:
    """
    מטפלת בתהליך הוספת חייל חדש.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    מפרידה בין הקלט/פלט לבין הלוגיקה העסקית.
    main.py אחראי על אינטראקציה עם המשתמש,
    soldier_manager.py אחראי על הלוגיקה.
    """
    print("\n" * 100)
    print(
        f"""
{"=" * 40}
Add Soldier
{"=" * 40}
        """
    )
    soldier_name = input("Soldier name: ")
    soldier_id = int(input("Soldier ID: "))
    add_soldier(soldier_id, soldier_name)


def handle_remove_soldier() -> None:
    """
    מטפלת בתהליך הסרת חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    print("\n" * 100)
    print(
        f"""
{"=" * 40}
Remove Soldier
{"=" * 40}
            """
    )
    soldier_id = int(input("Soldier ID: "))
    remove_soldier(soldier_id)


def handle_view_soldiers() -> None:
    """
    מטפלת בתהליך הצגת כל החיילים.
    קוראת לפונקציה המתאימה ומציגה את התוצאה.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין קבלת הנתונים לבין הצגתם.
    """
    print("\n" * 100)
    print(
        f"""
{"=" * 40}
Soldiers list
{"=" * 40}
            """
    )
    soldiers = get_all_soldiers()
    for i in soldiers:
        print(i)
        print("-" * 100)


def handle_add_duty() -> None:
    """
    מטפלת בתהליך הוספת תורנות לחייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    print("\n" * 100)
    print(
        f"""
{"=" * 40}
Add Duty
{"=" * 40}
            """
    )
    soldier_id = int(input("Soldier ID: "))
    duty_name = input("Duty name: ")
    duty_day = input("Day: ")

    add_duty_to_soldier(soldier_id, duty_name, duty_day)


def handle_update_duty_status() -> None:
    """
    מטפלת בתהליך עדכון סטטוס תורנות.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    print("\n" * 100)
    print(
        f"""
{"=" * 40}
Update Duty Status
{"=" * 40}
            """
    )
    soldier_id = int(input("Soldier ID: "))
    duty_name = input("Duty name: ")
    duty_status = input("Status: ")
    update_duty_status(soldier_id, duty_name, duty_status)


def handle_view_soldier_duties() -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    print("\n" * 100)
    print(
        f"""
{"=" * 40}
View Soldiers Duties
{"=" * 40}
            """
    )
    soldier_id = int(input("Soldier ID: "))
    l = get_soldier_duties(soldier_id)
    print(l)


def main() -> None:
    """
    הפונקציה הראשית של התוכנית.
    מריצה לולאה ראשית שמציגה תפריט, מקבלת בחירה ומפעילה פעולה.

    מקבלת: כלום
    מחזירה: כלום

    למה הפונקציה קיימת:
    נקודת הכניסה לתוכנית. מנהלת את הזרימה הראשית.
    """
    running = True
    while running:
        show_menu()
        user_choice = get_user_choice()
        match user_choice:
            case '1':
                handle_add_soldier()
            case '2':
                handle_remove_soldier()
            case '3':
                handle_view_soldiers()
            case '4':
                handle_add_duty()
            case '5':
                handle_update_duty_status()
            case '6':
                handle_view_soldier_duties()
            case '0':
                running = False

main()