import sqlite3

def delete_sub_location_data(sub_location_name):
    conn = sqlite3.connect('GUNI Navigation.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM sub_locations WHERE sub_location_name = ?", (sub_location_name,))

    conn.commit()
    conn.close()