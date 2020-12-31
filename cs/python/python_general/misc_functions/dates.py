"""Fun(c) with dates"""

# %% Imports
from datetime import datetime, timedelta
from typing import List

# %% Mondays
def mondays_between_two_dates(start: datetime, end: datetime) -> List[str]:
    """Returns the dates of each Monday between two dates, inclusive.

    :param start (str) : ISO-formatted start date.
    :param end (str) : ISO-formatted end date.
    :return (List[str]) : List of dates of Mondays falling b/w the two.
    """
    mon_dates = []
    # Somewhat-convoluted way to find the first Monday
    # Multiplied in order to multiply by 0 in the case of start being on monday
    start += timedelta(((7 * start.weekday()) + (7 - start.weekday())) % 7)
    # # Interesting idea to get nearest Monday, but doesn't work
    # start += timedelta(days=-start.weekday(), weeks=1)

    while start <= end:  # Add timedelta of 7 until on or after end date
        mon_dates.append(start.strftime("%Y-%m-%d"))
        start += timedelta(7)

    return mon_dates  # Return list of dates


print("Start on a monday; end on a Wednesday:")
print(mondays_between_two_dates(datetime(2018, 1, 1), datetime(2018, 1, 31)))

print("\nStart on a Wednesday; end on a Monday:")
print(mondays_between_two_dates(datetime(2018, 1, 3), datetime(2018, 1, 29)))

# %% Mondays
def monday_generator(start: datetime, end: datetime) -> List[str]:
    """Generator version of the above, just for fun."""
    start += timedelta(((7 * start.weekday()) + (7 - start.weekday())) % 7)

    def mon_gen(start, end):
        while start <= end:
            yield start.strftime("%Y-%m-%d")
            start += timedelta(7)

    return [date for date in mon_gen(start, end)]


print("Start on a monday; end on a Wednesday:")
print(monday_generator(datetime(2018, 1, 1), datetime(2018, 1, 31)))

print("\nStart on a Wednesday; end on a Monday:")
print(monday_generator(datetime(2018, 1, 3), datetime(2018, 1, 29)))

# %%
