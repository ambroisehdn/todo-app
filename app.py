from model import User as UserModel
from flask import Flask, jsonify
from flask_restful import Api
from flask_migrate import Migrate
from model import db

from controller import User ,UserList,Task,TaskList

from config import DevelopmentConfig as devConf


app = Flask(__name__)
app.config.from_object(devConf.APP_SETTINGS)

api = Api(app)

migrate = Migrate(app,db)

db.init_app(app)

@app.route('/')
def index():
    return jsonify({"message": "flask app :) "})


api.add_resource(UserList, '/user')
api.add_resource(User, '/user/<int:id>',endpoint='user_ep')

api.add_resource(TaskList, '/task')
api.add_resource(Task, '/task/<int:id>', endpoint='task_ep')

if __name__ == '__main__':
    app.run(debug=devConf.FLASK_DEBUG)
