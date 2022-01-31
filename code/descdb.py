# Examine and describe the clips table.
# 
import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)

logging.info("DESCDB")

con = sqlite3.connect('temporary.db')
cur = con.cursor()

# What are the columns for this table?
for row in cur.execute('PRAGMA table_info(clips)'):
    logging.info(row)

# What SQL command would recreate this table?
for row in cur.execute('SELECT sql FROM sqlite_master WHERE name = "clips"'):
    logging.info(row)

con.close()
