import sqlite3

def dropTables():
    conn = sqlite3.connect('GUNI Nevigation.db')
    cur = conn.cursor()
    cur.execute('''DROP TABLE IF EXISTS admin''')
    conn.commit()    
    conn.close()