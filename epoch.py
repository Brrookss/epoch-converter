"""Takes a non-negative integer representing to the number of seconds since
the Unix epoch on January 1, 1970 and returns the corresponding date in the
following format: MM-DD-YYYY.

Dates pre-Unix epoch are not supported; only non-negative integer values
are considered valid input.

Usage: python3 epoch.py [-h] seconds
"""

import argparse

import calculations
import constants


def get_arguments() -> argparse.Namespace:
    """Parses command line arguments.

    :return: command line arguments object
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("seconds", type=int,
                        help="number of seconds since the Unix epoch")

    args = parser.parse_args()
    return args


def converter(seconds: int) -> str:
    """Takes a non-negative integer representing to the number of seconds since
    the Unix epoch on January 1, 1970 and returns the corresponding date in the
    following format: MM-DD-YYYY.

    :param seconds: number of seconds since the Unix epoch
    :raises ValueError: when provided a negative value
    :return: formatted date
    """
    if seconds < 0:
        raise ValueError("Argument must be non-negative")

    years, seconds_remaining = calculations.get_years_since_epoch(seconds)
    year = constants.EPOCH_YEAR + years

    month, seconds_remaining = calculations.get_month(seconds_remaining, year)
    day = calculations.get_day(seconds_remaining)

    month += 1  # Converts to 1-based indexing
    return f"{month:02d}-{day:02d}-{year}"


def main() -> None:
    """Driver function for epoch program.

    :return: None
    """
    args = get_arguments()
    try:
        date = converter(args.seconds)
    except ValueError as e:
        print(e)
    else:
        print(date)


if __name__ == "__main__":
    main()
