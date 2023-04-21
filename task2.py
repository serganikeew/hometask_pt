import datetime
import calendar

def findDay(day):
    born = datetime.datetime.strptime(day, '%d %m %Y').weekday()
    return (calendar.day_name[born])

day = input('Введите дату в формате ДД/ММ/ГГГГ:')
print(findDay(day))