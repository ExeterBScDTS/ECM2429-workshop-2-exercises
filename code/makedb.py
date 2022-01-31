# Create a SQLite database with a table for storing audio clips
# To add clips use addblob.py
# 
import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)

logging.info("MAKEDB")

database = 'temporary.db'

con = sqlite3.connect(database)
cur = con.cursor()

# Identifiers don't need to be quoted, unless they are a keyword, however it's good practice to quote.
# https://www.sqlite.org/lang_keywords.html
cur.execute('CREATE TABLE "clips" ("path" TEXT PRIMARY KEY, "content" BLOB, "size" INTEGER, "loud" INTEGER, "music" INTEGER)')

con.commit()
con.close()

logging.info(f"Created database: {database}")