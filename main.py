from flask import Flask , jsonify , request
from createTableOperation import createTables
from createUser import createUser
from loginUser import loginUser
from createAdmin import createAdmin
from loginAdmin import loginAdmin
from allLocation import addLocation , getAllLocation , writeMainLocation
from imageToUrl import getImage
from allSubLocations import getAllMainLocations , uploadSubPlaces , getSubLocations

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
            return jsonify({'message':list(admin[1:3]),'status':200})
        else:
            return jsonify({'message':['Invalid credentials'],'status':400})
    
    except Exception as e:
        return jsonify({'message':[str(e)], 'status':400})
    
@app.route('/uploadLocation',methods=['POST'])
def upload_location():
    try:
        location_thumbnail = request.files['image']
        image_data = location_thumbnail.read()
        location = request.form['location']

        thumbnail = getImage(image_data)
        locations = addLocation(str(thumbnail),location)

        writeMainLocation(location)
        
        return jsonify({'message':str(locations),'status':200})
    
    except Exception as e:
        return jsonify({'message':str(e), 'status':400})
    
@app.route('/getAllLocation',methods=['GET'])
def get_all_location():
    try:
        locations = getAllLocation()
        
        if locations:
            return jsonify({'message':locations,'status':200})
        else:
            return jsonify({'message':'No locations found','status':400})
    
    except Exception as e:
        return jsonify({'message':str(e), 'status':400})
    
@app.route('/getAllMainLocations',methods=['GET'])
def get_all_main_locations():
    try:        
        allMainLocations = getAllMainLocations()

        if allMainLocations:
            return jsonify({'message':allMainLocations,'status':200})
        else:
            return jsonify({'message':'No main locations found','status':400})
    
    except Exception as e:
        return jsonify({'message':str(e), 'status':400})
    
@app.route('/uploadSubPlaces',methods=['POST'])
def upload_sub_places():
    try:
        image = request.files['image']
        image_data = image.read()
        name = request.form['subLocation']
        mainLocation = request.form['mainLocation']
        longitude = request.form['longitude']
        latitude = request.form['latitude']

        thumbnail = getImage(image_data)
        sub_location = uploadSubPlaces(str(thumbnail),name,mainLocation,longitude,latitude)

        return jsonify({'message':str(sub_location),'status':200})
    
    except Exception as e:
        return jsonify({'message':str(e), 'status':400})
    
@app.route('/getSubLocations',methods=['POST'])
def get_sub_locations():
    try:
        mainLocation = request.form['mainLocation']

        subLocations = getSubLocations(mainLocation)

        if subLocations:
            return jsonify({'message':subLocations,'status':200})
        else:
            return jsonify({'message':list(list('No sub locations found')),'status':400})
    
    except Exception as e:
        return jsonify({'message':str(e), 'status':400})

if __name__ == '__main__':
    createTables()
    app.run(debug=True)