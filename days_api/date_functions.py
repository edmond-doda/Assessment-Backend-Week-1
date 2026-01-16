"""Functions for working with dates."""

from datetime import datetime, date, timedelta


def convert_to_datetime(date_val: str) -> datetime:
    date_object = datetime.strptime(date_val, "%d.%m.%Y")
    return date_object


def get_days_between(first: datetime, last: datetime) -> int:
    delta = last - first
    return delta.days


def get_day_of_week_on(date_val: datetime) -> str:
    day = datetime.strftime(date_val, '%A')
    return day


def get_current_age(birthdate: date) -> int:
    today = date.today()
    age = today.year - birthdate.year
    if today.month < birthdate.month:
        age -= 1
    if ((today.month == birthdate.month) and
            today.day < birthdate.day):
        age -= 1
    return age
