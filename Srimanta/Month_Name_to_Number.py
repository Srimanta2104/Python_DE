def month_to_days(month):
    """
    Convert month name to number of days.

    Args:
        month (str): Month name (e.g., January, February, etc.).

    Returns:
        int: Number of days in the month.
    """
    month_days = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    return month_days[month.capitalize()]


# To account for leap years:
def is_leap_year(year):
    """
    Check if a year is a leap year.

    Args:
        year (int): Year.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def adjust_february_days(year):
    """
    Adjust February days for leap year.

    Args:
        year (int): Year.

    Returns:
        int: 29 if leap year, 28 otherwise.
    """
    return 29 if is_leap_year(year) else 28


# Example usage:
month = "February"
year = 2024

month = input("Enter Name of the Month")
year =int(input("Enter year"))

days = month_to_days(month)
if month == "February":
    days = adjust_february_days(year)
print(f"{month} {year} has {days} days.")