import sqlite3

con = sqlite3.connect('data/Chinook_Sqlite.sqlite')

cur = con.cursor()

que = '''SELECT * FROM Genre'''


result = cur.execute(que)
data = result.fetchall()

for line in data:
    print(line)

con.close()