from datetime import datetime, timedelta

def days_until_next_month(date):
    """returns the number of days (as an integer) until the next month begins"""
    next_month = date.month + 1
    next_year = date.year
    if next_month == 13:
        next_month = 1
        next_year += 1
    
    end = datetime(next_year, next_month, 1)
    period = end - date
    return period.days

print(days_until_next_month(datetime(2024, 12, 25)))
