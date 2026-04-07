from days_in_month import days_in_month

def is_valid_date(year: int, month: int, day: int) -> bool:
    """Determines if a calendar date is valid."""
    return year >= 0 and 1 <= month <= 12 and \
        1 <= day <= days_in_month(year, month)


if __name__ == "__main__":
    # --- Tests ---
    assert is_valid_date(2000, 1, 1)
    assert is_valid_date(2000, 12, 1)
    assert not is_valid_date(-1, 1, 1)
    assert not is_valid_date(2000, 0, 1)
    assert not is_valid_date(2000, 1, 0)
    assert not is_valid_date(2001, 2, 29)