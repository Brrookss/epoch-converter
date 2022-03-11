import constants
from enumerations import Month


def epoch_converter(seconds: int) -> str:
	"""
	Takes a non-negative integer representing the number of seconds since the Unix epoch
	on January 1st, 1970 and returns the date in the following format: MM-DD-YYYY
	"""
	years, seconds_remaining = get_years_since_epoch(seconds)
	year = years + constants.EPOCH
	month, seconds_remaining = get_month(seconds_remaining, year)
	day = get_day(seconds_remaining)
	return format_date(day, month + 1, year)  # Month converted to 1-based indexing

def format_date(day: int, month: int, year: int) -> str:
	return f"{format_digits(month)}-{format_digits(day)}-{year}"

def format_digits(num: int) -> str:
	result = ""
	if num < 10:
		result += "0"
	result += str(num)
	return result

def get_day(seconds: int) -> int:
	day = 1
	while seconds >= constants.SECONDS_PER_DAY:
		seconds -= constants.SECONDS_PER_DAY
		day += 1
	return day

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

def get_seconds_in_year(year: int) -> int:
	seconds = constants.SECONDS_PER_YEAR
	if is_leap_year(year):
		seconds += constants.SECONDS_PER_DAY
	return seconds

def get_years_since_epoch(seconds: int) -> int:
	years = 0
	seconds_in_year = get_seconds_in_year(constants.EPOCH)
	while seconds >= seconds_in_year:
		seconds -= seconds_in_year
		years += 1
		seconds_in_year = get_seconds_in_year(years + constants.EPOCH)
	return years, seconds

def is_leap_year(year: int) -> bool:
	return year % 4 == 0 and not is_skipped_leap_year(year)

def is_skipped_leap_year(year: int) -> bool:
	return year % 100 == 0 and year % 400 != 0

if __name__ == "__main__":
	try:
		seconds = int(input("Seconds: "))
		if seconds < 0:
			raise ValueError
		date = epoch_converter(seconds)
		print(date)
	except ValueError:
		print("Input must be a non-negative integer")
