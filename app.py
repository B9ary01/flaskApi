from flask import Flask, request, jsonify
from flask_cors import CORS
from  werkzeug import exceptions
from controllers import cities

app=Flask(__name__)
CORS(app)

@app.route('/')
def welcome():
    return "welcome to home page."

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
      
    }
    resp , code=fns[request.method](request)
    return jsonify(resp), code

if __name__ == '__main__':
   app.run(debug=True)
