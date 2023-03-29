from flask_restful import Resource, Api, reqparse, abort ,fields, marshal_with
from model import User as UserModel,db
from error import HttpError

# def notFound(id):
#     abort(404, message="ressource with id {} doesn't exist".format(id))

# def alreadyExist(field):
#     abort(400,message="Thi field {} with the same value already exist".format(field))

def userRequestBody():
	taskData = reqparse.RequestParser()
	taskData.add_argument("fullName", type=str,
                       help="Please provide the complete name", required=True)
	taskData.add_argument("username", type=str,
                       help="Please provide the username", required=True)
	taskData.add_argument("password", type=str,
                       help="Please provide the password", required=True)
	return taskData

def userRessource():
    return {
		"id":fields.Integer,
		"fullName":fields.String,
		"username":fields.String,
		"password": fields.String
	}
class User(Resource):

	@marshal_with(userRessource())
	def get(self,id):
        # elementNotFound(id)
		return {
			"Hello": "User ok ok "+str(id)
		},200

	def delete(self, id):
            # elementNotFound(id)
		return {
			"Hello": "User ok ok "
		}, 200

	@marshal_with(userRessource())
	def put(self, id):
            # elementNotFound(id)
		return {
			"Hello": "User ok ok "
		}, 201

class UserList(Resource) :
    
    def get(self):
        return {}
    
    @marshal_with(userRessource())
    def post(self):
        data = userRequestBody().parse_args()
        usernameExist = UserModel.query.filter_by(
            username=data['username']).first()
        
        if usernameExist:
            print(usernameExist)
            error = HttpError(400, "The username with")
            return error.raise_error("already_exists", identifier=data['username'])
        
        user = UserModel(
            fullName=data["fullName"], username=data['username'], password=data['password'])
        db.session.add(user)
        db.session.commit()
        
        return user, 201


class Task(Resource):

	def get(self,id):
        # elementNotFound(id)
		return {
			"Hello": "Task ok ok "+str(id)
		},200

	def delete(self, id):
            # elementNotFound(id)
		return {
			"Hello": "Task ok ok "
		}, 200

	def put(self, id):
            # elementNotFound(id)
		return {
			"Hello": "Task ok ok "
		}, 201

class TaskList(Resource) :
    
    def get(self):
        return {}
    
    def post(self):
        return '',201

