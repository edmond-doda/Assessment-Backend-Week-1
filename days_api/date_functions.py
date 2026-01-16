"""Functions for working with dates."""

from datetime import datetime, date, timedelta


def convert_to_datetime(date_val: str) -> datetime:
    try:
        date_object = datetime.strptime(date_val, "%d.%m.%Y")
        return date_object
    except ValueError:
        raise ValueError("Unable to convert value to datetime.")


def get_days_between(first: datetime, last: datetime) -> int:
    try:
        delta = last - first
        return delta.days
    except TypeError:
        raise TypeError("Datetimes required.")


def get_day_of_week_on(date_val: datetime) -> str:
    try:
        day = datetime.strftime(date_val, '%A')
        return day
    except TypeError:
        raise TypeError('Datetime required.')


def get_current_age(birthdate: date) -> int:
    if not isinstance(birthdate, date):
        raise TypeError("Date required.")

    today = date.today()
    age = today.year - birthdate.year
    if today.month < birthdate.month:
        age -= 1
    elif ((today.month == birthdate.month) and
            today.day < birthdate.day):
        age -= 1
    return age
