import sqlite3
import pandas as pd

df = pd.read_csv('buddymove_holidayiq.csv')
df = df.rename(columns={'User Id': 'User_ID'})

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()
curs.execute("DROP TABLE IF EXISTS review")
df.to_sql('review', conn)

print('Q1: Count how many rows you have - it should be 249!')
curs.execute('SELECT count(*) from review;')
print(curs.fetchall()[0][0])

print('Q2:How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category? ')
query = """SELECT count(*)
FROM review
WHERE Nature >99
AND Shopping >99;"""
curs.execute(query)
print(curs.fetchall()[0][0])