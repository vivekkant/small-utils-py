from datetime import date
from datetime import timedelta

def calc_no_of_days(date1, date2):
    delta = date2 - date1
    return delta.days

def days_option_one():
    today = date.today()
    four_years = date(2023, 9, 3) 
    date_to_resign = four_years - timedelta(weeks=17)
    return calc_no_of_days(today, date_to_resign), calc_no_of_days(today, four_years)

def days_option_two():
    today = date.today()
    date_to_leave = date(2023, 5, 15) 
    date_to_resign = date_to_leave - timedelta(weeks=17)
    return calc_no_of_days(today, date_to_resign), calc_no_of_days(today, date_to_leave)
