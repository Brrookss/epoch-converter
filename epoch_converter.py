import constants
from enumerations import Month


def epoch_converter(seconds: int) -> str:
	"""Takes an integer representing the number of seconds since the
	Unix epoch (1 January 1970) and returns the date in MM-DD-YYYY format
	"""
	years_since_epoch, seconds_remaining_in_months = get_years_since_epoch(seconds)
	year = years_since_epoch + constants.EPOCH
	month, seconds_remaining_in_days = get_month(seconds_remaining_in_months, year)
	day = get_day(seconds_remaining_in_days)
	return format_date(day, month + 1, year)  # Month converted to 1-based indexing

def get_years_since_epoch(seconds: int) -> int:
	years = 0

	seconds_in_year = get_seconds_in_year(years + constants.EPOCH)
	while seconds >= seconds_in_year:
		seconds -= seconds_in_year
		years += 1
		seconds_in_year = get_seconds_in_year(years + constants.EPOCH)
	return years, seconds

def get_seconds_in_year(year: int) -> bool:
	seconds = constants.SECONDS_PER_YEAR

	if is_leap_year(year):
		seconds += constants.SECONDS_PER_DAY
	return seconds

def is_leap_year(year: int) -> int:
	return year % 4 == 0 and not is_skipped_leap_year(year)

def is_skipped_leap_year(year: int) -> bool:
	return year % 100 == 0 and year % 400 != 0

def get_month(seconds: int, year: int) -> int:
	month = Month.JANUARY.value

	seconds_in_month = get_seconds_in_month(month, year)
	while seconds >= seconds_in_month and month < constants.MONTHS_PER_YEAR:
		seconds -= seconds_in_month
		month += 1
		seconds_in_month = get_seconds_in_month(month, year)
	return month, seconds

def get_seconds_in_month(month: int, year: int) -> int:
	days = 0

	if month == Month.FEBRUARY.value and is_leap_year(year):
		days += 1
	days += constants.DAYS_PER_MONTH[month]
	return days * constants.SECONDS_PER_DAY

def get_day(seconds: int) -> int:
	day = 1

	while seconds >= constants.SECONDS_PER_DAY:
		seconds -= constants.SECONDS_PER_DAY
		day += 1
	return day

def format_date(day: int, month: int, year: int) -> str:
	day_str = format_digits(day)
	month_str = format_digits(month)
	return f"{month_str}-{day_str}-{year}"

def format_digits(num: int) -> str:
	result = ""

	if num < 10:
		result += "0"
	result += str(num)
	return result

if __name__ == "__main__":
	try:
		seconds = int(input("Seconds: "))
		if seconds < 0:
			raise ValueError
		date = epoch_converter(seconds)
		print(date)
	except ValueError:
		print("Input must be a non-negative integer")
