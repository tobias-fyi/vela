"""Extract messages from iMessage / the Apple Messages app."""

# %% imports
import sqlite3
import pandas as pd

# %% Connect to messages database
# conn = sqlite3.connect("/Users/Tobias/Library/Messages/chat.db")
# Above gives this error -> OperationalError: unable to open database file
# Copied chat.db onto my desktop and it worked!
conn = sqlite3.connect("/Users/Tobias/Desktop/chat.db")
cur = conn.cursor()

# query the database to get all the table names
cur.execute(" select name from sqlite_master where type = 'table' ")

for name in cur.fetchall():
    print(name)

# %% Look at a few messages
a_few_messages = pd.read_sql_query("select * from message limit 10", conn)
a_few_messages

# %% Create dataframe with relevant tables

# High Sierra and above
messages = pd.read_sql_query(
    """select *, datetime(date/1000000000 + strftime("%s", "2001-01-01") ,"unixepoch","localtime")  as date_utc from message""",
    conn,
)
messages = messages.rename(columns={"ROWID": "message_id"})
# Get handles to map apple_ids
handles = pd.read_sql_query("select * from handle", conn)
handles = handles.rename(columns={"id": "phone_number", "ROWID": "handle_id"})

merge_1 = pd.merge(messages["text",])

chat_message_joins = pd.read_sql_query("select * from chat_message_join", conn)
