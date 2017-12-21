import datetime
import calendar


def meetup_day(year, month, day_of_the_week, which):
    weekday = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
    whichday = {'1st': 1, '2nd': 2, '3rd': 3, '4th': 4, '5th': 5, 'teenth': -1, 'last': -1}

    weekday_number = weekday[day_of_the_week]
    whichday_number = whichday[which]
    if weekday_number == None or whichday_number == None:
        raise Exception("The day is not valid")

    first_day_of_month = datetime.datetime(year, month, 1).weekday()

    number_of_days_in_month = calendar.monthrange(year, month)[1]

    month_days = [first_day_of_month]
    for i in range(1, number_of_days_in_month):
        month_days.append((month_days[i - 1] + 1) % 7)

    day = 0
    if which == 'teenth':
        for i in range(12, 19):
            if weekday_number == month_days[i]:
                day = i + 1
                break
    elif which == 'last':
        day = number_of_days_in_month
        while weekday_number != month_days[day - 1]:
            day -= 1
    else:
        i = 0
        while i < whichday_number:
            while weekday_number != month_days[day]:
                day += 1
            i += 1
            day += 1

    if day > number_of_days_in_month:
        raise Exception("The day is not valid")

    return datetime.date(year, month, day)
