from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворення рядка дати у форматі 'РРРР-ММ-ДД' в об'єкт datetime
        date_object = datetime.strptime(date, '%Y-%m-%d')

        # Отримання поточної дати
        today = datetime.today()

        # Розрахунок різниці у днях
        days_difference = (date_object - today).days

        return days_difference
    except ValueError:
        print("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")
        return None

# Приклад використання функції
current_date = datetime.today().strftime('%Y-%m-%d')  # Поточна дата у форматі 'РРРР-ММ-ДД'
result = get_days_from_today("2021-10-09")

if result is not None:
    print(f"Різниця в днях між {current_date} та 2021-10-09: {result} днів.")
