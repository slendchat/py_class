import datetime
import calendar
import math
import re

def calculate_age_in_days():
    while True:
        date_of_birth = input("Введите дату своего рождения в формате ДД-ММ-ГГГГ: ")
        if re.match(r'^\d{2}-\d{2}-\d{4}$', date_of_birth):
            break
        else:
            print("Некорректный формат даты. Повторите ввод.")

    day_of_birth, month_of_birth, year_of_birth = map(int, date_of_birth.split('-'))

    current_date = datetime.date.today()

    date_of_birth = datetime.date(year_of_birth, month_of_birth, day_of_birth)
    age_in_days = (current_date - date_of_birth).days

    return age_in_days

def get_weekday_for_date():
    while True:
        date_input = input("Введите дату в формате ДД-ММ-ГГГГ: ")
        if re.match(r'^\d{2}-\d{2}-\d{4}$', date_input):
            break
        else:
            print("Некорректный формат даты. Повторите ввод.")

    day, month, year = map(int, date_input.split('-'))

    weekday_number = calendar.weekday(year, month, day)

    weekdays = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    weekday_name = weekdays[weekday_number]

    return weekday_name  
  
def calculate_fall_time():
    while True:
        try:
            height = float(input("Введите высоту падения объекта в метрах: "))
            break
        except ValueError:
            print("Вы ввели некорректное значение. Повторите ввод.")
    g = 9.8

    fall_time = math.sqrt(2 * height / g)

    return fall_time




