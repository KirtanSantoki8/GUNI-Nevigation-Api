import sqlite3

def location_categry():
    conn = sqlite3.connect('GUNI Navigation.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM main_locations")
    count = cursor.fetchone()[0]
    return count

def total_sub_locations():
    conn = sqlite3.connect('GUNI Navigation.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM sub_locations")
    count = cursor.fetchone()[0]
    return count

def category_wise_sub_location():
    conn = sqlite3.connect('GUNI Navigation.db')
    cursor = conn.cursor()
    cursor.execute("SELECT main_location_name, COUNT(*) FROM sub_locations GROUP BY main_location_name")
    result = cursor.fetchall()
    return result