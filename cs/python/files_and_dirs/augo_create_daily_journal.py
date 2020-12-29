"""
Augo :: Create Daily Journal

- Get current file name: "yyyy-mm-dd-nnn-day.md"
    - Create current file
- Get previous filename: "yyyy-mm-dd-nnn-day.md"
- Get current sprint: directory number + file name
    - If no sprint exists, then create it
- Selectively copy/extract from previous and copy to current, filling in info as needed:
    - Only up to first "---"
    - Only TODO items that are not complete
    - (Optional / in other script: move completed items to sprint sojourn)
    - (Optional / in other script: move Daily Backlog items/links to sprint backlog)
"""

# %%
from datetime import datetime, timedelta

# %% Get day (number) of the year: 1 - 365 (or 366 for leap years)
today = datetime.today()
doy = today.strftime("%j")
# doy = today.timetuple().tm_yday  # Alternate method
# And ISO date
date_iso = today.strftime("%Y-%m-%d")
# date_iso = today.isoformat()[:10]  # Alternate method
# Day of week, short version
dow = today.strftime("%a").lower()
# Current filename
today_filename = f"{date_iso}-{doy}-{dow}.md"

# %% Function to get filename
def get_daily_filename(date: datetime = datetime.today()) -> str:
    """Returns the filename for the given date in the format:
    'yyyy-mm-dd-nnn-day.md'

    :param date [datetime.datetime] : Date for filename, defaults to datetime.today().
    :return (str) : Filename
    """
    iso_date = date.strftime("%Y-%m-%d")  # ISO date
    doy = date.strftime("%j")  # Day of year
    dow = date.strftime("%a").lower()  # Day of week
    return f"{iso_date}-{doy}-{dow}.md"


# %% Get current and previous filenames
today = datetime.today()
today_filename = get_daily_filename()
yesterday_filename = get_daily_filename(today - timedelta(days=1))
print("Today:", today_filename)
print("Yesterday:", yesterday_filename)

# %%
