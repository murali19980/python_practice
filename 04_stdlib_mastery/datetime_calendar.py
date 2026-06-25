"""
Practice: datetime & calendar
"""
import datetime
import calendar

def datetime_demo():
    today = datetime.date.today()
    print(f"Today: {today.strftime('%Y-%m-%d')}")
    future = today + datetime.timedelta(days=100)
    print(f"100 days from now: {future}")
    birthday = datetime.date(1990, 6, 15)  # change this
    print(f"Birthday: {birthday.strftime('%A')}")

def calendar_demo():
    print(calendar.month(2026, 6))

if __name__ == "__main__":
    datetime_demo()
    calendar_demo()
