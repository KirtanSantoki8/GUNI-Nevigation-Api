import sqlite3
import uuid
from datetime import date

def getAllMainLocations():
    conn = sqlite3.connect('GUNI Navigation.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM main_locations''')
    locations = cur.fetchall()
    conn.close()
    return locations

def uploadSubPlaces(image,name,mainLocation,description,phone_no,longitude,latitude):
    conn = sqlite3.connect('GUNI Navigation.db')
    cur = conn.cursor()
    sub_location_id = str(uuid.uuid4())
    dateOfCreation = date.today()
    cur.execute('''INSERT INTO sub_locations (sub_location_id,main_location_name,sub_location_thumbnail,sub_location_name,sub_location_description,sub_location_phone_no,longitude,latitude,date_of_sub_location_creation) VALUES (?,?,?,?,?,?,?,?,?)''',(sub_location_id,mainLocation,image,name,description,phone_no,longitude,latitude,dateOfCreation))
    conn.commit()
    conn.close()

def getAllSubLocations():
    conn = sqlite3.connect('GUNI Navigation.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM sub_locations''')
    locations = cur.fetchall()
    conn.close()
    return locations

def getSubLocations(mainLocation):
    conn = sqlite3.connect('GUNI Navigation.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM sub_locations WHERE main_location_name = ?''',(mainLocation,))
    locations = cur.fetchall()
    conn.close()
    return locations

def getSpecificSubLocation(name):
    conn = sqlite3.connect('GUNI Navigation.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM sub_locations where sub_location_name = ?''',(name,))
    location = cur.fetchall()
    conn.close()
    return location

def getSubLocationCount(name):
    conn = sqlite3.connect('GUNI Navigation.db')
    cur = conn.cursor()
    cur.execute('''SELECT COUNT(*) FROM sub_locations WHERE main_location_name = ?''',(name,))
    count = cur.fetchone()[0]
    conn.close()
    return count