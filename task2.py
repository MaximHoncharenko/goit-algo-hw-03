import random

def get_numbers_ticket(min_val, max_val, quantity):
    # Перевірка коректності вхідних параметрів
    if not (1 <= min_val <= max_val <= 1000) or not (1 <= quantity <= max_val - min_val + 1):
        print("Некоректні вхідні дані.")
        return []

    # Використання множини для забезпечення унікальності чисел
    unique_numbers_set = set()

    # Генерація випадкових унікальних чисел
    while len(unique_numbers_set) < quantity:
        unique_numbers_set.add(random.randint(min_val, max_val))

    # Перетворення множини у відсортований список
    sorted_numbers_list = sorted(list(unique_numbers_set))

    return sorted_numbers_list

# Приклад використання функції
lottery_numbers = get_numbers_ticket(1, 1000, 12)
print("Ваші лотерейні числа:", lottery_numbers)
