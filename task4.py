from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Конвертуємо дату народження з рядка у об'єкт datetime
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Визначаємо дату народження на наступний рік, якщо вона вже минула в цьому році
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        # Розраховуємо різницю між днем народження та поточним днем
        days_until_birthday = (birthday - today).days

        # Перевіряємо, чи народження випадає на наступний тиждень
        if 0 <= days_until_birthday <= 7:
            # Переносимо дату привітання на наступний понеділок, якщо потрібно
            if birthday.weekday() in [5, 6]:  # Якщо вихідний
                days_until_birthday += (7 - birthday.weekday())
            congratulation_date = today + timedelta(days=days_until_birthday)

            # Додаємо інформацію про користувача та дату привітання до результату
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Приклад використання функції
users = [
    {"name": "John", "birthday": "2000.05.15"},
    {"name": "Alice", "birthday": "1995.11.30"},
    # Додайте інші записи користувачів за необхідності
]

result = get_upcoming_birthdays(users)
print("Список користувачів та їхніх дат привітань:", result)
