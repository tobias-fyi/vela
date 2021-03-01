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
    # * by 0 (Monday) means no change
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
def monday_gen(start: datetime, end: datetime) -> List[str]:
    """Generator version of the above, just for fun."""
    start += timedelta(((7 * start.weekday()) + (7 - start.weekday())) % 7)

    def mon_gen(start, end):
        while start <= end:
            yield start.strftime("%Y-%m-%d")
            start += timedelta(7)

    return [date for date in mon_gen(start, end)]


print("Start on a monday; end on a Wednesday:")
print(monday_gen(datetime(2018, 1, 1), datetime(2018, 1, 31)))

print("\nStart on a Wednesday; end on a Monday:")
print(monday_gen(datetime(2018, 1, 3), datetime(2018, 1, 29)))

# %% Separate / unnested generator func version
# Note: Not typed quite right - it "returns" a generator
def monday_generator(start: datetime, end: datetime, sep: str = "-") -> str:
    """Generator function for Mondays between two dates, inclusive."""
    start += timedelta(((7 * start.weekday()) + (7 - start.weekday())) % 7)
    while start <= end:
        yield start.strftime(f"%Y{sep}%m{sep}%d")
        start += timedelta(7)


print("Start on a monday; end on a Wednesday:")
print([m for m in monday_generator(datetime(2018, 1, 1), datetime(2018, 1, 31))])

print("\nStart on a Wednesday; end on a Monday:")
print([m for m in monday_generator(datetime(2018, 1, 3), datetime(2018, 1, 29), "/")])


# %% Parsing datetime strings
print(datetime.fromisoformat("2018-01-01"))

# %%
def monday_genr(start, end, sep: str = "-") -> str:
    """Generator function for Mondays between two dates, inclusive.
    Accepts ISO-formatted strings or datetime objects.
    """
    if type(start) == str:
        start = datetime.fromisoformat(start)
    if type(end) == str:
        end = datetime.fromisoformat(end)
    start += timedelta(((7 * start.weekday()) + (7 - start.weekday())) % 7)
    while start <= end:
        yield start.strftime(f"%Y{sep}%m{sep}%d")
        start += timedelta(7)


print("Start on a monday; end on a Wednesday (string):")
print([m for m in monday_genr("2018-01-01", "2018-01-31")])

print("\nStart on a Wednesday; end on a Monday (datetime):")
print([m for m in monday_genr(datetime(2018, 1, 3), datetime(2018, 1, 29), "/")])


# %% Weekly date generator
def day_date_generator(start, end, sep: str = "-") -> str:
    """Generator function for weekly dates between two dates.
    Accepts date strings or datetime objects.
    """
    if type(start) == str:
        start = datetime.fromisoformat(start.replace("/", "-"))
    if type(end) == str:
        end = datetime.fromisoformat(end.replace("/", "-"))
    while start <= end:
        yield start.strftime(f"%Y{sep}%m{sep}%d")
        start += timedelta(7)  # Weekly increments

