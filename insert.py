import sqlite3

conn = sqlite3.connect('points.db')
cursor = conn.cursor()
query = """
INSERT INTO points(x,y)
VALUES (3,5);
"""

cursor.execute(query)
conn.commit()
conn.close()