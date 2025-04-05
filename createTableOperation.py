import sqlite3

def createTables():
    conn = sqlite3.connect('GUNI Nevigation.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id VARCHAR(255) NOT NULL,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                phone_no VARCHAR(255) NOT NULL,
                date_of_account_creation DATE NOT NULL
                )
            ''')
    cur.execute('''CREATE TABLE IF NOT EXISTS admin (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
                )
            ''')
    cur.execute('''CREATE TABLE IF NOT EXISTS location (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                location_id VARCHAR(255) NOT NULL,
                location_thumbnail VARCHAR(255) NOT NULL,
                location VARCHAR(255) NOT NULL,
                date_of_location_creation DATE NOT NULL
                )
            ''')
    cur.execute('''CREATE TABLE IF NOT EXISTS location_details (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                location_name VARCHAR(255) NOT NULL,
                location_image VARCHAR(255) NOT NULL,
                location_date_of_creation DATE NOT NULL
                )
            ''')
    # cur.execute('''DROP TABLE IF EXISTS location''')
    conn.commit()    
    conn.close()