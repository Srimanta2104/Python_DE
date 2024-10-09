from datetime import datetime, timedelta

def text_to_date(text, format):
    """
    Convert text to date.

    Args:
        text (str): Date text.
        format (str): Date format.

    Returns:
        datetime: Date object.
    """
    try:
        return datetime.strptime(text, format)
    except ValueError:
        return "Invalid date format."

def add_days(date_text, days, date_format):
    """
    Add days to a date.

    Args:
        date_text (str): Date text.
        days (int): Number of days to add.
        date_format (str): Date format.

    Returns:
        str: New date text.
    """
    date = datetime.strptime(date_text, date_format)
    new_date = date + timedelta(days=days)
    return new_date.strftime(date_format)
# Example usage:

vyear = int(input("Input a year: YYYY " )  )                                                  
vmonth = int(input("Input a month [1-12]: MM ") )                                              
vday = int(input("Input a day [1-31]: DD ") )

text = "2022-09-01"



text = str(vyear) +"-"+ str(vmonth)+"-"+ str(vday)
format = "%Y-%m-%d"
#date = text_to_date(text, format)

date =add_days(text,1,format)
print(date)  # Output: 2022-09-01 00:00:00