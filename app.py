# import library
from flask import Flask,request
from flask_restful import Resource, Api
from flask_cors import CORS


# init flask object
app = Flask(__name__)

# init flask_restful object
api  = Api(app)

# init flask_cors object
CORS(app)

# empty var
identity = {}

# resource class
class Resource(Resource):
    # get method
    def get(self):
        return identity
    
    # post method
    def post(self):
        name = request.form["name"]
        age = request.form["age"]
        identity["name"] = name
        identity["age"] = age
        response = {"msg": "Succesfully"}
        return response
    
# resource setup
api.add_resource(Resource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True)