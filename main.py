from datetime import date, datetime

def get_birthdays_per_week(users):

 if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
