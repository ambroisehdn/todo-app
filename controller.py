from flask_restful import Resource, reqparse ,fields, marshal_with
from model import TaskStatus, User as UserModel,db,Task as TaskModel
from error import HttpError
from helper import TaskUtil
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


class Task(Resource,TaskUtil):

    def getUser(self,user_id):
        return User.get(self,user_id)

    # @marshal_with(TaskUtil.ressource)
    def get(self, id):
        record = TaskModel.query.filter_by(
            id=int(id)).first()

        if not record:
            return HttpError(404, "The record with id").raise_error("not_found", identifier=str(id))

        return self.customResponse(record)

    def delete(self, id):
        record = TaskModel.query.filter_by(
            id=int(id)).first()

        if not record:
            return HttpError(404, "The record with id").raise_error("not_found", identifier=str(id))
        db.session.delete(record)
        db.session.commit()
        return 'The record with {} has been deleted '.format(str(id)),204

    # @marshal_with(ressource)
    def put(self, id):
        data = self.requestBody().parse_args()

        record = TaskModel.query.filter_by(
            id=int(id)).first()

        user_id = data['user_id']

        self.getUser(user_id) #check if user exist

        status = TaskList.statusIsSet(self,data=data)

        if not record:
            return HttpError(404, "The record with id").raise_error("not_found", identifier=str(id))
        record.title = data["title"]
        record.description = data["description"]
        record.due_date = data["due_date"]
        record.due_time = data["due_time"]
        record.status = status

        db.session.commit()

        return self.customResponse(record),201


class TaskList(Resource,TaskUtil) :

    def get(self):
        data = []
        tasks = TaskModel.query.all()
        for task in tasks :
            data.append(self.customResponse(task))
        return data

    def getUser(self,user_id):
        return User.get(self,user_id)

    # @marshal_with(ressource)
    def post(self):
        data = self.requestBody().parse_args()

        userId = data['user_id']

        status = self.statusIsSet(data)

        self.getUser(userId) #check if user exist

        task = TaskModel(
            title=data["title"], description=data['description'], due_date=data['due_date'],
            due_time=data["due_time"], user_id=userId, status=status,
            )
        db.session.add(task)
        db.session.commit()

        return self.customResponse(task), 201

class TaskStatusList(Resource):

    def get(self):
        return TaskStatus.list()

class Todo(Resource) :

    def requestBody(self):
        data = reqparse.RequestParser()
        data.add_argument("user_id", type=int,
                          help="Please provide the user_id", required=True)
        data.add_argument("task_id", type=int,
                              help="Please provide the task_id", required=True)
        data.add_argument("status", type=TaskStatus,required=True)

        return data

    def getUser(self,user_id):
        return User.get(self,user_id)

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int,help="Please provide the user_id",location="args",required=True)
        parser.add_argument('status', type=TaskStatus,location="args")

        data = parser.parse_args()

        user_id = data['user_id']
        status = data['status']

        queryChain= TaskModel.query.filter_by(user_id=user_id)

        if status :
            queryChain = queryChain.filter_by(status=status)

        records = queryChain.all()

        todos = []
        for record in records :
            todos.append({
            "id":record.id,
            "title":record.title,
            "description":record.description,
            "status":str(record.status),
            "due_date":str(record.due_date),
            "due_time":str(record.due_time),
            })

        return {"user":self.getUser(user_id),"todos":todos}

    def put(self):
        data = self.requestBody().parse_args()

        user_id = data['user_id']
        id = data['task_id']
        status = data['status']

        record = TaskModel.query.filter_by(id=id).filter_by(user_id=user_id).first()

        if not record:
            return HttpError(404, "The task don't found").raise_error("not_found")

        record.status = status

        db.session.commit()

        return {"message":"Your task status is set to {}".format(status)},201