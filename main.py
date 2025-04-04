from flask import Flask , jsonify , request
from createTableOperation import createTables
from createUser import createUser
from loginUser import loginUser
from createAdmin import createAdmin
from loginAdmin import loginAdmin
from dropTable import dropTables
from addLocation import addLocation
from imageToUrl import getImage

app = Flask(__name__)

@app.route('/')
def test_api():
    return 'Welcome to GUNI Navigation'

@app.route('/createUser',methods=['POST'])
def create_user():
    try:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        phone_no = request.form['phone_no']

        user_id = createUser(name=name,email=email,password=password,phone_no=phone_no)
        
        return jsonify({'message':str(user_id),'status':200})
    
    except Exception as e:
        return jsonify({'message':str(e), 'status':400})
    
@app.route('/login',methods=['POST'])
def login():
    try:
        email = request.form['email']
        password = request.form['password']

        user = loginUser(email,password)
        
        if user:
            return jsonify({'message':user[1],'status':200})
        else:
            return jsonify({'message':'Invalid credentials','status':400})
    
    except Exception as e:
        return jsonify({'message':str(e), 'status':400})
    
@app.route('/loginAdmin',methods=['POST'])
def login_admin():
    try:
        name = request.form['name']
        password = request.form['password']

        admin = loginAdmin(name,password)
        
        if admin:
            return jsonify({'message':admin[1],'status':200})
        else:
            return jsonify({'message':'Invalid credentials','status':400})
    
    except Exception as e:
        return jsonify({'message':str(e), 'status':400})
    
@app.route('/uploadLocation',methods=['POST'])
def upload_location():
    try:
        location_thumbnail = request.files['image']
        image_data = location_thumbnail.read()
        location = request.form['location']

        thumbnail = getImage(image_data)

        location_id = addLocation(thumbnail,location)
        
        return jsonify({'message':str(location_id),'status':200})
    
    except Exception as e:
        return jsonify({'message':str(e), 'status':400})

if __name__ == '__main__':
    dropTables()
    createTables()
    createAdmin("Admin","Admin@123")
    app.run(debug=True)