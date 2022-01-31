# A prototype binary file archive
# 
import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)

logging.info("FIXDB")

con = sqlite3.connect('audio.db')
cur = con.cursor()

# What are the columns for this table?
for row in cur.execute('PRAGMA table_info(clips)'):
    logging.info(row)

# What SQL command would recreate this table?
for row in cur.execute('SELECT sql FROM sqlite_master WHERE name = "clips"'):
    logging.info(row)

# Add extra columns for loud/quiet and music/noise
# These are boolean, but it SQLite the INTEGER type is used, 0 false, 1 true.

cur.execute('ALTER TABLE clips ADD COLUMN "loud" INTEGER')

cur.execute('ALTER TABLE clips ADD COLUMN "music" INTEGER')

# What SQL command would recreate this table?
for row in cur.execute('SELECT sql FROM sqlite_master WHERE name = "clips"'):
    logging.info(row)


# Identifiers don't need to be quoted, unless they are a keyword, however it's good practice to quote.
# https://www.sqlite.org/lang_keywords.html
# 'CREATE TABLE [clips] ([path] TEXT PRIMARY KEY, [content] BLOB, [size] INTEGER, "loud" INTEGER, "music" INTEGER)'