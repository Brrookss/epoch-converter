"""Takes a non-negative integer representing to the number of seconds since
the Unix epoch on January 1, 1970 and returns the corresponding date in the
following format: MM-DD-YYYY.

Dates pre-Unix epoch are not supported; only non-negative integer values
are considered valid input.

usage: python3 epoch.py [-h] seconds
"""

import argparse
import sys

import constants
import calculations


def get_arguments() -> int:
    """Parses command line arguments.

    :return: number of seconds provided by user
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("seconds", type=int,
                        help="number of seconds since the Unix epoch"
                        )

    args = parser.parse_args()
    return args.seconds


def converter(seconds: int) -> str:
    """Takes a non-negative integer representing to the number of seconds since
    the Unix epoch on January 1, 1970 and returns the corresponding date in the
    following format: MM-DD-YYYY.

    :param seconds: number of seconds since the Unix epoch
    :return: formatted date
    """
    years, seconds_remaining = calculations.get_years_since_epoch(seconds)
    year = constants.EPOCH + years

    month, seconds_remaining = calculations.get_month(seconds_remaining, year)
    day = calculations.get_day(seconds_remaining)

    month += 1  # Converts to 1-based indexing
    return f"{month:02d}-{day:02d}-{year}"


def main() -> None:
    """Driver function for epoch program.

    :return: None
    """
    try:
        seconds = get_arguments()
        if seconds < 0:
            raise ValueError
    except ValueError:
        sys.exit("argument must be a non-negative integer")

    date = converter(seconds)
    print(date)


if __name__ == "__main__":
    main()