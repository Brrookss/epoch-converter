import constants
from enumerations import Month


def get_day(seconds: int) -> int:
    day = 1
    while seconds >= constants.SECONDS_PER_DAY:
        seconds -= constants.SECONDS_PER_DAY
        day += 1
    return day

def get_month(seconds: int, year: int) -> tuple:
    month = Month.JANUARY.value
    seconds_in_month = get_seconds_in_month(month, year)
    while seconds >= seconds_in_month and month < constants.MONTHS_PER_YEAR:
        seconds -= seconds_in_month
        month += 1
        seconds_in_month = get_seconds_in_month(month, year)
    return month, seconds

def get_seconds_in_month(month: int, year: int) -> int:
    days = constants.DAYS_PER_MONTH[month]
    if month == Month.FEBRUARY.value and is_leap_year(year):
        days += 1
    return days * constants.SECONDS_PER_DAY

def get_seconds_in_year(year: int) -> int:
    days = constants.DAYS_PER_YEAR
    if is_leap_year(year):
        days += 1
    return days * constants.SECONDS_PER_DAY

def get_years_since_epoch(seconds: int) -> tuple:
    years = 0
    seconds_in_year = get_seconds_in_year(constants.EPOCH)
    while seconds >= seconds_in_year:
        seconds -= seconds_in_year
        years += 1
        seconds_in_year = get_seconds_in_year(constants.EPOCH + years)
    return years, seconds

def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and not is_skipped_leap_year(year)

def is_skipped_leap_year(year: int) -> bool:
    return year % 100 == 0 and year % 400 != 0
