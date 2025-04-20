import sqlite3

def delete_location_cateory(location):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM location WHERE location = ?", (location,))
        
        conn.commit()
        conn.close()
        
    except Exception as e:
        print(f"Error deleting location: {e}")