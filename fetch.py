import sqlite3
conn = sqlite3.connect('points.db')
cursor = conn.cursor()

query = """
    SELECT *
    FROM points;
"""

cursor.execute(query)
# difference is the line below, need to fetch
results = cursor.fetchall()
conn.close()

print(results)
# comes back as a list of tuples