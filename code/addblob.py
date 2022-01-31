# A prototype binary file archive
# 
import sqlite3
import logging
import sys

logging.basicConfig(level=logging.DEBUG)

def add_blob(cursor, path:str, content:any, size:int, music:bool, loud:bool) -> bool:
    logging.debug(f'add_blob({path})')
    sql_insert = 'INSERT INTO "clips" ("path", "content", "size", "music", "loud") VALUES (?, ?, ?, ?, ?)'
    cursor.execute(sql_insert, (title, data, size, music, loud))


path = sys.argv[1]
con = sqlite3.connect('temporary.db')
cur = con.cursor()

try:
    title = path.split('/')[-1]
    vol = path.split('/')[-2]
    cat = path.split('/')[-3]
except IndexError as ex:
    logging.error(ex)
    sys.exit('Invalid path')

 # Use boolean values for category and volume.
music = (cat == "music")
loud = (vol == "loud")
logging.info(f'category:{cat} volume:{vol} size:{size} {title}')
logging.debug(f'music:{music} loud:{loud}')

with open(path, "rb") as f:
    data = f.read()
    size = len(data)
    add_blob(.....)
    con.commit()

con.close()