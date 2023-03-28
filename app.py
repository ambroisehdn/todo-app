from flask import Flask
from flask_restful import Resource, Api
from user.app import User,UserList

app = Flask(__name__)
api = Api(app)

api.add_resource(UserList, '/user')
api.add_resource(User, '/user/<int:id>',endpoint='user_ep')

if __name__ == '__main__':
    app.run(debug=config.DevelopmentConfig().FLASK_DEBUG)
