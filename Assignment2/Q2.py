from datetime import datetime, timedelta

def pay_days(first_pay, interval):
    """Returns a list of all the pay days that will occur from the startdate until the end of the year."""
    answer = []
    pay_day = first_pay
    while pay_day.year == first_pay.year:
        answer.append(pay_day)
        pay_day = pay_day + interval
    return answer

from pprint import pprint
# A summer job paid fortnightly
pprint(pay_days(datetime(2024, 11,13), timedelta(days=14)))