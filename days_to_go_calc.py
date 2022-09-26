from datetime import date
from datetime import timedelta

def calc_no_of_days(date1, date2):
    delta = date2 - date1
    return delta.days

def five_years_to_go():
    today = date.today()
    target = date(2024, 9, 3)
    return calc_no_of_days(today, target)

def four_years_to_go():
    today = date.today()
    target = date(2023, 9, 3)
    return calc_no_of_days(today, target)

def days_to_decide():
    today = date.today()
    four_years = date(2023, 9, 3) 
    target = four_years - timedelta(weeks=17)
    return calc_no_of_days(today, target)

