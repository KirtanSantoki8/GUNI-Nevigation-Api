import sqlite3
import uuid

def addLocation(image,name):
    conn = sqlite3.connect('GUNI Nevigation.db')
    cur = conn.cursor()
    location_id = str(uuid.uuid4())
    cur.execute('''INSERT INTO location (location_id,location_thumbnail,location) VALUES (?,?,?)''',(location_id,image,name))
    conn.commit()
    conn.close()

def getAllLocation():
    conn = sqlite3.connect('GUNI Nevigation.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM location''')
    locations = cur.fetchall()
    conn.close()
    return locations