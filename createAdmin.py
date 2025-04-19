import sqlite3

def createAdmin(name,password):
    conn = sqlite3.connect('GUNI Navigation.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO admin (name,password) VALUES (?,?)''',(name,password))
    conn.commit()
    conn.close()