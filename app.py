from model import User as UserModel
from flask import Flask, jsonify
from flask_restful import Api
from flask_migrate import Migrate
from model import db
import psycopg2

from controller import User as UserController ,UserList as UserListController

from config import DevelopmentConfig as devConf


app = Flask(__name__)
app.config.from_object(devConf.APP_SETTINGS)

api = Api(app)

migrate = Migrate(app,db)

db.init_app(app)

connection = psycopg2.connect(devConf.SQLALCHEMY_DATABASE_URI)


from model import User as UserModel

@app.route('/')
def index():
    return jsonify({"message": "flask app :) "})

api.add_resource(UserListController, '/user')
api.add_resource(UserController, '/user/<int:id>',endpoint='user_ep')

if __name__ == '__main__':
    app.run(debug=devConf.FLASK_DEBUG)
