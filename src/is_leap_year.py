def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == "__main__":
    assert is_leap_year(4)
    assert not is_leap_year(5)
    assert is_leap_year(400)
    assert not is_leap_year(100)