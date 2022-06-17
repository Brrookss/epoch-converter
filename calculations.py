"""Calculations used for epoch conversion."""

from typing import Tuple

import constants


def get_day(seconds: int) -> int:
    """Converts number of seconds to days.

    :param seconds: number of seconds since start
    :return: day number
    """
    day = 1
    while seconds >= constants.SECONDS_PER_DAY:
        seconds -= constants.SECONDS_PER_DAY
        day += 1
    return day


def get_month(seconds: int, year: int) -> Tuple[int, int]:
    """Converts number of seconds to months.

    :param seconds: number of seconds since start of current year
    :param year: year in consideration
    :return: month number, seconds remaining at start of following year
    """
    month = constants.JANUARY
    seconds_in_month = get_seconds_in_month(month, year)
    while seconds >= seconds_in_month and month < constants.MONTHS_PER_YEAR:
        seconds -= seconds_in_month
        month += 1
        seconds_in_month = get_seconds_in_month(month, year)
    return month, seconds


def get_seconds_in_month(month: int, year: int) -> int:
    """Determines number of seconds in month.

    :param month: month in consideration
    :param year: year in consideration
    :return: number of seconds in current month
    """
    days = constants.DAYS_PER_MONTH[month]
    if month == constants.FEBRUARY and is_leap_year(year):
        days += 1
    seconds = days * constants.SECONDS_PER_DAY
    return seconds


def get_seconds_in_year(year: int) -> int:
    """Determines number of seconds in year.

    :param year: year to consider
    :return: number of seconds in current year
    """
    days = constants.DAYS_PER_YEAR
    if is_leap_year(year):
        days += 1
    seconds = days * constants.SECONDS_PER_DAY
    return seconds


def get_years_since_epoch(seconds: int) -> Tuple[int, int]:
    """Calculates number of years since the Unix epoch on January 1, 1970.

    :param seconds: number of seconds since epoch
    :return: year number, seconds remaining at start of calculated year
    """
    years = 0
    seconds_in_year = get_seconds_in_year(constants.EPOCH_YEAR)
    while seconds >= seconds_in_year:
        seconds -= seconds_in_year
        years += 1
        seconds_in_year = get_seconds_in_year(constants.EPOCH_YEAR + years)
    return years, seconds


def is_leap_year(year: int) -> bool:
    """Determines if year is a leap year.

    :param year: year in consideration
    :return: bool
    """
    return year % 4 == 0 and not is_skipped_leap_year(year)


def is_skipped_leap_year(year: int) -> bool:
    """Determines if year is a skipped leap year.

    :param year: year in consideration
    :return: bool
    """
    return year % 100 == 0 and year % 400 != 0
