DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Non-leap year
SECONDS_PER_DAY = 86_400
SECONDS_PER_YEAR = 31_536_000


def epoch_converter(num_sec):
	"""Takes an integer representing the number of seconds since
	the Unix epoch (January 1, 1970) and returns the formatted date
	"""
	sec_rem_in_years = num_sec
	years_since_epoch, sec_rem_in_months = get_years_since_epoch(sec_rem_in_years)
	year = years_since_epoch + 1970

	month, sec_rem_in_days = get_month(sec_rem_in_months, year)
	day = get_day(sec_rem_in_days, month)

	date = format_date(day, month, year)
	return date


def get_years_since_epoch(num_sec):
	sec_rem = num_sec
	years_since_epoch = 0

	sec_in_year = get_seconds_in_year(years_since_epoch + 1970)
	while sec_rem >= sec_in_year:
		sec_rem -= sec_in_year

		years_since_epoch += 1
		sec_in_year = get_seconds_in_year(years_since_epoch + 1970)
	return years_since_epoch, sec_rem


def get_seconds_in_year(year):
	sec_in_year = 0

	if is_leap_year(year):
		sec_in_leap_day = SECONDS_PER_DAY
		sec_in_year += sec_in_leap_day
	sec_in_year += SECONDS_PER_YEAR
	return sec_in_year


def is_leap_year(year):
	skipped_leap_year = year % 100 == 0 and year % 400 != 0
	return year % 4 == 0 and not skipped_leap_year


def get_month(num_sec, year):
	sec_rem = num_sec
	month = 0

	sec_in_month = get_sec_in_month(month, year)
	while sec_rem >= sec_in_month and month < 11:
		sec_rem -= sec_in_month

		month += 1
		sec_in_month = get_sec_in_month(month, year)
	month += 1  # Convert to 1-based indexing
	return month, sec_rem


def get_sec_in_month(month, year):
	num_days = 0

	if month == 1 and is_leap_year(year):
		leap_day = 1
		num_days += leap_day
	num_days += DAYS_PER_MONTH[month]
	return num_days * SECONDS_PER_DAY


def get_day(num_sec, month):
	sec_rem = num_sec
	day = 1

	while sec_rem >= SECONDS_PER_DAY:
		sec_rem -= SECONDS_PER_DAY
		day += 1
	return day


def format_date(day, month, year):
	day_str = ''
	if day < 10:
		day_str += '0'
	day_str += str(day)

	month_str = ''
	if month < 10:
		month_str += '0'
	month_str += str(month)

	date = f'{month_str}-{day_str}-{year}'
	return date
