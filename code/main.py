# A prototype binary file archive
# 
import sqlite3

from play import play

con = sqlite3.connect('temporary.db')
cur = con.cursor()

# Pick one clip at random
for row in cur.execute('SELECT path, size FROM clips ORDER BY random() LIMIT 1'):
        print(row)

name = row[0]
print("about to play:{name}")

# Now get the binary content
# Passing a single arg to execute is tricky, must use a list or tuple.
for row in cur.execute('SELECT path, size, content FROM clips WHERE path=?', (name,)):
        print(row[1],len(row[2]))

blob = row[2]
play(blob)


