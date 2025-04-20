from flask import Flask , jsonify , request
from createTableOperation import createTables
from createUser import createUser
from loginUser import loginUser
from loginAdmin import loginAdmin
from allLocation import addLocation , getAllLocation , writeMainLocation, getSpecificLocation
from imageToUrl import getImage
from allSubLocations import getAllMainLocations , uploadSubPlaces , getSubLocations
from dashboard import location_categry, total_sub_locations, category_wise_sub_location
from updateData import update_location_info

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
        description = request.form['description']
        phone_no = request.form['phone_no']
        longitude = request.form['longitude']
        latitude = request.form['latitude']

        thumbnail = getImage(image_data)
        sub_location = uploadSubPlaces(str(thumbnail),name,mainLocation,description,phone_no,longitude,latitude)

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
            return jsonify({'message':'No sub locations found','status':400})
    
    except Exception as e:
        return jsonify({'message':str(e), 'status':400})
    
@app.route('/dashboard',methods=['GET'])
def dashboard():
    try:
        location_count = location_categry()
        sub_location_count = total_sub_locations()
        category_wise_sub_location_data = category_wise_sub_location()

        return jsonify({
            'location_count':location_count,
            'sub_location_count':sub_location_count,
            'category_wise_sub_location_data':category_wise_sub_location_data,
            'status':200
        })
    
    except Exception as e:
        return jsonify({'message':str(e), 'status':400})
    
@app.route('/updateLocationCategory',methods=['POST'])
def update_location_category():
    try:
        old_name = request.form['old_name']
        new_name = request.form.get('new_name')
        new_thumbnail = request.files.get('new_thumbnail')
        thumbnail = None

        if new_thumbnail:
            image_data = new_thumbnail.read()
            thumbnail = str(getImage(image_data))

        if new_name is None and new_thumbnail is None:
            return jsonify({'message': 'No new data provided for update', 'status': 400})
        
        update_location_info(old_name, new_name=new_name, new_thumbnail=thumbnail)

        return jsonify({'message': 'Location category updated successfully', 'status': 200})

    except Exception as e:
        return jsonify({'message':str(e), 'status':400})
    
@app.route('/getSpecificLocation',methods=['POST'])
def get_all_location():
    try:
        location_name = request.form['location_name']

        locations = getSpecificLocation(location_name)
        
        if locations:
            return jsonify({'message':locations,'status':200})
        else:
            return jsonify({'message':'No locations found','status':400})
    
    except Exception as e:
        return jsonify({'message':str(e), 'status':400})

if __name__ == '__main__':
    createTables()
    app.run(debug=True)