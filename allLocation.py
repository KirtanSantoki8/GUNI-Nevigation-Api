import sqlite3
import uuid
from datetime import date

def addLocation(image,name):
    conn = sqlite3.connect('GUNI Nevigation.db')
    cur = conn.cursor()
    location_id = str(uuid.uuid4())
    dateOfCreation = date.today()
    cur.execute('''INSERT INTO location (location_id,location_thumbnail,location,date_of_location_creation) VALUES (?,?,?,?)''',(location_id,image,name,dateOfCreation))
    conn.commit()
    conn.close()

def getAllLocation():
    conn = sqlite3.connect('GUNI Nevigation.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM location''')
    locations = cur.fetchall()
    conn.close()
    return locations