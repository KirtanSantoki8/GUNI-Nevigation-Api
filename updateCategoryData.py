import sqlite3

def update_location_info(old_name, new_name=None, new_thumbnail=None):
    conn = sqlite3.connect('GUNI Navigation.db')
    cursor = conn.cursor()

    updates = []
    params = []

    if new_name is not None:
        updates.append("location = ?")
        params.append(new_name)

    if new_thumbnail is not None:
        updates.append("location_thumbnail = ?")
        params.append(new_thumbnail)

    if not updates:
        print("Nothing to update.")
        conn.close()
        return

    query = f"UPDATE location SET {', '.join(updates)} WHERE location = ?"
    params.append(old_name)

    cursor.execute(query, params)
    conn.commit()
    conn.close()
