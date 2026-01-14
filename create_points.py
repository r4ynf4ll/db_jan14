import sqlite3
conn = sqlite3.connect('points.db')
cursor = conn.cursor()

# create table with 3 colums, each point has x and y coordinates with an id
# a row in the table is called a record
query = """
CREATE TABLE IF NOT EXISTS points (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    x REAL NOT NULL,
    y REAL NOT NULL
);
"""
cursor.execute(query)
conn.commit()
conn.close()