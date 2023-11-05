from collections import defaultdict
from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    # Створюємо словник, де ключами є назви днів тижня, а значеннями - порожні списки
    days_of_week = defaultdict(list)
    
    today = date.today()

    for user in users:
        birthday = user["birthday"]
        # Перевіряємо, чи день народження вже відбувся цього року
        if birthday < today:
            # Якщо так, то додаємо день народження на наступний рік
            next_birthday = birthday.replace(year=today.year + 1)
        else:
            next_birthday = birthday
        
        # Знаходимо різницю між сьогоднішньою датою та датою народження
        days_until_birthday = (next_birthday - today).days
        # Отримуємо назву дня тижня для дати народження
        day_name = next_birthday.strftime("%A") if next_birthday.weekday() not in (5, 6) else "Monday"

        if days_until_birthday <= 7:
            # Якщо день народження відбудеться протягом наступного тижня, додаємо користувача до відповідного дня тижня
            days_of_week[day_name].append(user["name"])

    return days_of_week

if __name__ == "__main__":
    users = [
        {"name": "Alex Show", "birthday": datetime(1980, 5, 11).date()},
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Ki Plo Kun", "birthday": datetime(1991, 8, 14).date()},
        {"name": "Anakin Skywalker", "birthday": datetime(1999, 11, 20).date()},
        {"name": "Dean Winchester", "birthday": datetime(1953, 5, 12).date()}
    ]

    result = get_birthdays_per_week(users)
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
