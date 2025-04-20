import sqlite3
import uuid
from datetime import date

def addLocation(image,name):
    conn = sqlite3.connect('GUNI Navigation.db')
    cur = conn.cursor()
    location_id = str(uuid.uuid4())
    dateOfCreation = date.today()
    cur.execute('''INSERT INTO location (location_id,location_thumbnail,location,date_of_location_creation) VALUES (?,?,?,?)''',(location_id,image,name,dateOfCreation))
    conn.commit()
    conn.close()

def getAllLocation():
    conn = sqlite3.connect('GUNI Navigation.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM location''')
    locations = cur.fetchall()
    conn.close()
    return locations

def writeMainLocation(name):
    conn = sqlite3.connect('GUNI Navigation.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO main_locations (main_location_names) VALUES (?)''',(name,))
    conn.commit()
    conn.close()

def getSpecificLocation(name):
    conn = sqlite3.connect('GUNI Navigation.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM location where location = ?''',(name,))
    location = cur.fetchall()
    conn.close()
    return location