from flask_restful import Resource, Api, reqparse, abort ,fields, marshal_with
from model import User as UserModel,db,Task as TaskModel,TaskStatus
from error import HttpError

class User(Resource):

    ressource = {
		"id": fields.Integer,
		"fullName": fields.String,
		"username": fields.String,
		"password": fields.String
	}

    def requestBody(self):
        data = reqparse.RequestParser()
        data.add_argument("fullName", type=str,
                       help="Please provide the complete name", required=True)
        data.add_argument("username", type=str,
                       help="Please provide the username", required=True)
        data.add_argument("password", type=str,
                       help="Please provide the password", required=True)
        return data
    
    
    @marshal_with(ressource)
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


    @marshal_with(ressource)
    def put(self, id):
        data = self.requestBody().parse_args()

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
    ressource = User.ressource
    requestBody = User.requestBody
    
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
    
    @marshal_with(ressource)
    def post(self):
        data = self.requestBody().parse_args()
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
    ressource = {
        "id": fields.Integer,
      	"title": fields.String,
      	"description": fields.String,
      	"status": fields.Raw(attribute=lambda TaskStatus: TaskStatus),
		"due_date": fields.String,
		"due_time": fields.String,
		"user_id":fields.Integer
    }

    def requestBody(self):
        data = reqparse.RequestParser()
        data.add_argument("title", type=str,
                          help="Please provide the title", required=True)
        data.add_argument("description", type=str,
                              help="Please provide the description", required=True)
        data.add_argument("due_date", type=reqparse.inputs.date,
                          help="Please provide the due_date", required=True)
        data.add_argument("due_time", type=reqparse.inputs.time,
                          help="Please provide the due_time", required=True)
        data.add_argument("user_id", type=int,
                          help="Please provide the user_id", required=True)
        data.add_argument("status", type=TaskStatus)
        
        return data
    
    @marshal_with(ressource)
    def get(self,id):
        return {
			"Hello": "Task ok ok "+str(id)
		},200
        
    def delete(self, id): 
     	return {
			"Hello": "Task ok ok "
		}, 200
      
    @marshal_with(ressource)
    def put(self, id):
        return {
			"Hello": "Task ok ok "
		}, 201

class TaskList(Resource) :
    ressource = Task.ressource
    requestBody = Task.requestBody
    
    def get(self):
        return {}
    
    @marshal_with(ressource)
    def post(self):
        return '',201

