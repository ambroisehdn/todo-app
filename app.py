from flask import Flask, jsonify
import psycopg2
from flask_restful import Resource, Api
from user.app import User,UserList
from config import DevelopmentConfig as devConf

app = Flask(__name__)
api = Api(app)

connection = psycopg2.connect(devConf.SQLALCHEMY_DATABASE_URI)


@app.route('/')
def index():
    return jsonify({"message": "flask app :) "})

api.add_resource(UserList, '/user')
api.add_resource(User, '/user/<int:id>',endpoint='user_ep')

if __name__ == '__main__':
    app.run(debug=devConf.FLASK_DEBUG)
