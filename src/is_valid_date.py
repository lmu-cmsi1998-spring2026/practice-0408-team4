from days_in_month import days_in_month

def is_valid_date(year: int, month: int, day: int) -> bool:
    """Determines if a calendar date is valid."""
    return year >= 0 and 1 <= month <= 12 and \
        1 <= day <= days_in_month(year, month)


if __name__ == "__main__":
    print(is_valid_date(2020, 2, 29))  # True
    print(is_valid_date(2019, 2, 29))  # False
    print(is_valid_date(2020, 1, 31))  # True
    print(is_valid_date(2020, 4, 31))  # False
    print(is_valid_date(1938, 8, 31)) # True
    print(is_valid_date(1602, 9, 30)) # True
    print(is_valid_date(1602, 9, 31)) # False