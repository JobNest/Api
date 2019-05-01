import json
from flask import Flask, request
from flask.ext import restful
from flask.ext.restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = restful.Api(app)

class Login(restful.Resource):
    def post(self):
        json_data = request.get_json()

        f = open('log.txt', 'w')
        f.write(json.dumps(json_data))
        f.close()
        return json_data

api.add_resource(Login, '/login')

if __name__ == '__main__':
    app.run(debug=True)
