from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    # Створюємо словник, де ключами є назви днів тижня, а значеннями - порожні списки
    days_of_week = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": [],
    }
    
    today = date.today()

    for user in users:
        birthday = user["birthday"].date()
        # Перевіряємо, чи день народження вже відбувся цього року
        if birthday < today:
            # Якщо так, то додаємо день народження на наступний рік
            next_birthday = birthday.replace(year=today.year + 1)
        else:
            next_birthday = birthday
        
        # Знаходимо різницю між сьогоднішньою датою та датою народження
        days_until_birthday = (next_birthday - today).days
        # Отримуємо назву дня тижня для дати народження
        day_name = next_birthday.strftime("%A")

        if days_until_birthday <= 7:
            # Якщо день народження відбудеться протягом наступного тижня, додаємо користувача до відповідного дня тижня
            days_of_week[day_name].append(user["name"])

    return days_of_week

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        # Додайте інших користувачів до списку
    ]

    result = get_birthdays_per_week(users)
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
