import sqlite3

def delete_location_cateory(location):
    try:
        conn = sqlite3.connect('GUNI Navigation.db')
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM location WHERE location = ?", (location,))
        cursor.execute("DELETE FROM main_locations WHERE main_location_names = ?", (location,))
        
        conn.commit()
        conn.close()
        
    except Exception as e:
        print(f"Error deleting location: {e}")