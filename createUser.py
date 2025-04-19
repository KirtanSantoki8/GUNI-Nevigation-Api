import sqlite3
import uuid
from datetime import date

def createUser(name,email,password,phone_no):
    conn = sqlite3.connect('GUNI Navigation.db')
    cur = conn.cursor()
    user_id = str(uuid.uuid4())
    dateOfCreation = date.today()
    cur.execute('''INSERT INTO users (user_id,name,email,password,phone_no,date_of_account_creation) VALUES (?,?,?,?,?,?)''',(user_id,name,email,password,phone_no,dateOfCreation))
    conn.commit()    
    conn.close()
    return user_id