def date(day: int, month: int, year: int) -> str:
    return f"{digits(month)}-{digits(day)}-{year}"

def digits(num: int) -> str:
    result = ""
    if num < 10:
        result += "0"
    result += str(num)
    return result
