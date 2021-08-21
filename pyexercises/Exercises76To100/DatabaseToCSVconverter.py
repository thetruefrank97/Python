import sqlite3
import pandas

conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM countries WHERE area >= 2000000")
rows = cursor.fetchall()
conn.close()


dataFrame = pandas.DataFrame.from_records(rows)
dataFrame.columns = ["Rank", "Country", "Area", "Population"]
dataFrame.to_csv("countries_big_area.csv", index=False)


