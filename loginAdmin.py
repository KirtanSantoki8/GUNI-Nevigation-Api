import sqlite3

def loginAdmin(name,password):
    conn = sqlite3.connect('GUNI Navigation.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM admin WHERE name = ? AND password = ?''',(name,password))
    admin = cur.fetchone()
    conn.close()
    return admin