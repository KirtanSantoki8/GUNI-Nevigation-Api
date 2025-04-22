import sqlite3

def update_sub_location_info(old_name, main_location_name=None, sub_location_thumbnail=None, sub_location_name=None, sub_location_description=None, sub_location_phone_no=None, longitude=None, latitude=None):
    conn = sqlite3.connect('GUNI Navigation.db')
    cur = conn.cursor()

    updates = []
    params = []

    if main_location_name is not None:
        updates.append("main_location_name = ?")
        params.append(main_location_name)

    if sub_location_thumbnail is not None:
        updates.append("sub_location_thumbnail = ?")
        params.append(sub_location_thumbnail)
    
    if sub_location_name is not None:
        updates.append("sub_location_name = ?")
        params.append(sub_location_name)
    
    if sub_location_description is not None:
        updates.append("sub_location_description = ?")
        params.append(sub_location_description)
    
    if sub_location_phone_no is not None:
        updates.append("sub_location_phone_no = ?")
        params.append(sub_location_phone_no)
    
    if longitude is not None:
        updates.append("longitude = ?")
        params.append(longitude)
    
    if latitude is not None:
        updates.append("latitude = ?")
        params.append(latitude)

    if not updates:
        print("Nothing to update.")
        conn.close()
        return
    
    query = f"UPDATE sub_locations SET {', '.join(updates)} WHERE sub_location_name  = ?"
    params.append(old_name)

    cur.execute(query, params)
    conn.commit()
    conn.close()