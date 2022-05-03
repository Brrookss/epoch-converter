"""Takes a non-negative integer representing to the number of seconds since
the Unix epoch on January 1st, 1970 and returns the corresponding date in
the following format: MM-DD-YYYY.

Dates pre-Unix epoch are not supported; only non-negative integer values
are considered valid input.

Usage: python3 epoch_converter.py seconds
"""

import sys

import constants
import conversions


def epoch_converter(seconds: int) -> str:
    """Takes a non-negative integer representing to the number of seconds since
    the Unix epoch on January 1st, 1970 and returns the corresponding date in
    the following format: MM-DD-YYYY.

    :param seconds: number of seconds since epoch
    :return: formatted date
    """
    years, seconds_remaining = conversions.get_years_since_epoch(seconds)
    year = constants.EPOCH + years

    month, seconds_remaining = conversions.get_month(seconds_remaining, year)
    day = conversions.get_day(seconds_remaining)

    month += 1  # Converts to 1-based indexing
    return f"{month:02d}-{day:02d}-{year}"


def main() -> None:
    """Driver function for epoch conversion program.

    :return: None
    """
    try:
        seconds = int(sys.argv[1])
        if seconds < 0:
            raise ValueError
    except IndexError:
        sys.exit(f"Usage: python3 {sys.argv[0]} seconds")
    except ValueError:
        sys.exit("Argument must be a non-negative integer")
    date = epoch_converter(seconds)
    print(date)


if __name__ == "__main__":
    main()
