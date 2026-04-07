"""An implementation of a leap year calculator."""

def is_leap_year(year: int) -> bool:
    """
    Determines if a year is a leap year.

    Parameters
    ----------
    year: int
        The year to check.

    Returns
    -------
    bool
        Whether the year is a leap year.
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == "__main__":
    # --- Tests ---

    # Main leap year case
    assert is_leap_year(4)
    assert is_leap_year(8)

    # Main non leap year case
    assert not is_leap_year(5)
    assert not is_leap_year(1953)

    # 100 & 400 year clauses
    assert not is_leap_year(100)
    assert is_leap_year(400)
