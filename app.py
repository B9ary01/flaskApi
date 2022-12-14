from flask import Flask, request, jsonify, render_template
#from flask_cors import CORS
from  werkzeug import exceptions
from controllers import cities

app=Flask(__name__)
#CORS(app)



@app.route('/', methods=["GET"])
def welcome():
    return render_template("index.html")

'''
@app.route('/mycities',methods=['GET','POST'])
def city():
    if request.method=='GET' :
        return jsonify({'cities':['Dhatan','Chitwan','Kathmandu']}),200

    elif request.method=='POST':
        return "we have posted some cities",201
'''


@app.route('/cities', methods=["GET"])
def city():
    cities = [
    {'id': 1, 'name': 'Pokhara', 'population': 360000, 'region': 'hill'},
    {'id': 2, 'name': 'Dharan', 'population': 230000, 'region': 'terai'},
    {'id': 3, 'name': 'Chitwan', 'population': 310000, 'region': 'terai'},
    {'id': 4, 'name': 'Kathmandu', 'population': 3452000, 'region': 'hill'},
    {'id': 5, 'name': 'Birgunj', 'population': 350000, 'region': 'terai'},
    {'id': 6, 'name': 'Dadeldhura', 'population': 130000, 'region': 'terai'},
    {'id': 7, 'name': 'Nepalgunj', 'population': 249000, 'region': 'terai'}

]
    return render_template("cities.html" ,page_title="list of cities",cities=cities)


@app.route('/mycities',methods=['GET','POST'])
def mycity():
    fns={
        'GET': cities.index,
        'POST':cities.create
      
    }
    resp , code=fns[request.method](request)
    return jsonify(resp), code

@app.route('/cities/<int:city_id>',methods=['GET','PUT', 'DELETE'])
def cat_handler(city_id):
    fns={
        'GET':cities.show,
        'PUT':cities.update,
        'DELETE':cities.destroy
       
    }
    resp , code=fns[request.method](request, city_id)
    return jsonify(resp), code


@app.route('/city/new', methods=["GET","POST"])
def new_flower():
    if request.method=="GET":
        return "this is for post request"
    else:
        data=request.get_json()
        if data["region"]!="invisible":
            return "yes that is a flower",201
        else:
            return "absolutely not ",400

if __name__ == '__main__':
   app.run(debug=True)
