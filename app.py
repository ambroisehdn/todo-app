from flask import Flask, jsonify
from flask_restful import Api
from flask_migrate import Migrate

from scheduler import scheduler

from model import db

from controller import User ,UserList,Task,TaskList,Todo,TaskStatusList

from config import DevelopmentConfig as devConf


app = Flask(__name__)
app.config.from_object(devConf.APP_SETTINGS)

api = Api(app)

migrate = Migrate(app,db)

db.init_app(app)

scheduler.init_app(app)
scheduler.start()

@app.route('/')
def index():
    return jsonify({"message": "flask app :) "})


api.add_resource(UserList, '/user')
api.add_resource(User, '/user/<int:id>',endpoint='user_ep')

api.add_resource(TaskList, '/task')
api.add_resource(Task, '/task/<int:id>', endpoint='task_ep')
api.add_resource(TaskStatusList, '/task-status')
api.add_resource(Todo, '/todo', endpoint='todo_ep')

if __name__ == '__main__':
    app.run(debug=devConf.FLASK_DEBUG)
