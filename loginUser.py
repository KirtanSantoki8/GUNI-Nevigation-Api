import sqlite3

def loginUser(email,password):
    conn = sqlite3.connect('GUNI Navigation.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM users WHERE email = ? AND password = ?''',(email,password))
    user = cur.fetchone()
    conn.close()
    return user