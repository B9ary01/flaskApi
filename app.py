from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from  werkzeug import exceptions
from controllers import cities

app=Flask(__name__)
CORS(app)



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

@app.route('/cities',methods=['GET','POST'])
def city():
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

if __name__ == '__main__':
   app.run(debug=True)
