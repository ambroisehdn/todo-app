from flask_restful import Resource, Api, reqparse, abort ,fields, marshal_with
from model import User as UserModel,db
from error import HttpError

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
    def get(self, id):
        hasRecord = UserModel.query.filter_by(
            id=int(id)).first()

        if not hasRecord:
            return HttpError(404, "The record with id").raise_error("not_found", identifier=str(id))
        
        return hasRecord
        
    def delete(self, id):
        hasRecord = UserModel.query.filter_by(
            id=int(id)).first()

        if not hasRecord:
            return HttpError(404, "The record with id").raise_error("not_found", identifier=str(id))
        db.session.delete(hasRecord)
        db.session.commit()
        return 'The record with {} has been deleted '.format(str(id)),204


    @marshal_with(userRessource())
    def put(self, id):
        data = userRequestBody().parse_args()

        hasRecord = UserModel.query.filter_by(
            id=int(id)).first()

        if not hasRecord:
            return HttpError(404, "The record with id").raise_error("not_found", identifier=str(id))
        hasRecord.username = data["username"]
        hasRecord.fullName = data["fullName"]
        hasRecord.password = data["password"]
        
        db.session.commit()
        
        return hasRecord
 
class UserList(Resource) :
    
    def get(self):
        returnData = []
        users = UserModel.query.all()
        for user in users :
            returnData.append({
				'id':user.id,
				'fullName': user.fullName,
				'username':user.username,
				'password': user.password,
			})
        return returnData
    
    @marshal_with(userRessource())
    def post(self):
        data = userRequestBody().parse_args()
        usernameExist = UserModel.query.filter_by(
            username=data['username']).first()
        
        if usernameExist:
            error = HttpError(400, "The username with")
            return error.raise_error("already_exists", identifier=data['username'])
        
        user = UserModel(
            fullName=data["fullName"], username=data['username'], password=data['password'])
        db.session.add(user)
        db.session.commit()
        
        return user, 201


class Task(Resource):

	def get(self,id):
     
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

