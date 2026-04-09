from sys import argv

from is_valid_date import is_valid_date

def day_counter(date_1: tuple[int, int, int], date_2: tuple[int, int, int]):
    """Calculates the number of days between two dates."""
    if not is_valid_date(*date_1):
        raise ValueError(f"Invalid first date: {date_1}.")
    if not is_valid_date(*date_2):
        raise ValueError(f"Invalid second date: {date_2}.")
    if date_1 > date_2:
        raise ValueError(f"The first date provided {date_1} must precede the second date {date_2}.")
    
    year_1, month_1, day_1 = date_1
    year_2, month_2, day_2 = date_2

    current_year = year_1
    current_month = month_1
    current_day = day_1

    day_count = 0

    while (current_year, current_month, current_day) != (year_2, month_2, day_2):
        day_count += 1
        current_day += 1

        if not is_valid_date(current_year, current_month, current_day):
            current_day = 1
            current_month += 1

            if not is_valid_date(current_year, current_month, current_day):
                current_month = 1
                current_year += 1

    return day_count