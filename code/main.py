# A prototype binary file archive
# 
import sqlite3

from play import play

print("hi")

con = sqlite3.connect('audio.db')
cur = con.cursor()

play(cur.execute('SELECT content FROM clips WHERE path=?', 
        ('orac on.wav',)).fetchone()[0])

# What does our table look like?
for row in cur.execute('SELECT sql FROM sqlite_master WHERE name = "clips"'):
    print(row)

# Table name clips
for row in cur.execute('SELECT path, size FROM clips ORDER BY random() LIMIT 1'):
        print(row)

name = row[0]
print(name)

# Now get the binary content
# Passing a single arg to execute is tricky, must use a list or tuple.
#for row in cur.execute('SELECT path, size, content FROM clips WHERE path=?', (name,)):
#        print(row[1],len(row[2]))

#blob = row[2]
#play(blob)

#play(cur.execute('SELECT content FROM clips WHERE path=?', 
#        ('orac off.wav',)).fetchone()[0])


for row in cur.execute('PRAGMA table_info(clips)'):
        print(row)

