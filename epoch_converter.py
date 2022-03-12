import constants
import conversions
import formatting


def epoch_converter(seconds: int) -> str:
    """
    Takes a non-negative integer representing to the number of seconds since the Unix epoch
    on January 1st, 1970 and returns the corresponding date in the following format: MM-DD-YYYY
    """
    years, seconds_remaining = conversions.get_years_since_epoch(seconds)
    year = constants.EPOCH + years
    month, seconds_remaining = conversions.get_month(seconds_remaining, year)
    day = conversions.get_day(seconds_remaining)
    return formatting.date(day, month + 1, year)  # Month converted to 1-based indexing

if __name__ == "__main__":
    try:
        seconds = int(input("Seconds: "))
        if seconds < 0:
            raise ValueError
        date = epoch_converter(seconds)
        print(date)
    except ValueError:
        print("Input must be a non-negative integer")
