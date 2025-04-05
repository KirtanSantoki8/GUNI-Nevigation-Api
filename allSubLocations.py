import sqlite3
import uuid
from datetime import date

def getAllMainLocations():
    conn = sqlite3.connect('GUNI Nevigation.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM main_locations''')
    locations = cur.fetchall()
    conn.close()
    return locations

def uploadSubPlaces(image,name,mainLocation):
    conn = sqlite3.connect('GUNI Nevigation.db')
    cur = conn.cursor()
    sub_location_id = str(uuid.uuid4())
    dateOfCreation = date.today()
    cur.execute('''INSERT INTO sub_locations (sub_location_id,main_location_name,sub_location_thumbnail,sub_location_name,date_of_sub_location_creation) VALUES (?,?,?,?,?)''',(sub_location_id,mainLocation,image,name,dateOfCreation))
    conn.commit()
    conn.close()