from flask_restful import fields
from datetime import time,date

from flask_restful import reqparse

from model import TaskStatus

class DateFormat(fields.Raw):
    def format(self, value):
        return date.strftime(value,'%Y-%m-%d')

class TimeFormat(fields.Raw):
    def format(self, value):
        return time.strftime(value, "%H:%M")



class TaskUtil():

    ressource = {
        "id": fields.Integer,
      	"title": fields.String,
      	"description": fields.String,
      	"status": fields.Raw(attribute=lambda TaskStatus: TaskStatus),
		"due_date": DateFormat,
		"due_time": TimeFormat,
		"user_id":fields.Integer,
		# "user":fields.Raw,
    }

    def requestBody(self):
        data = reqparse.RequestParser()
        data.add_argument("title", type=str,
                          help="Please provide the title", required=True)
        data.add_argument("description", type=str,
                              help="Please provide the description", required=True)
        data.add_argument("due_date", type=str,
                          help="Please provide the due_date", required=True)
        data.add_argument("due_time", type=str,
                          help="Please provide the due_time", required=True)
        data.add_argument("user_id", type=int,
                          help="Please provide the user_id", required=True)
        data.add_argument("status", type=TaskStatus)

        return data

    def statusIsSet(self, data):
        if not data['status'] :
            status = TaskStatus.OnHold
        else : status = data['status']

        return status

    def customResponse(self, task):
        status = task.status
        dataReturn = {
            "id":task.id,
            "title":task.title,
            "description":task.description,
            "status":str(status),
            "due_date":str(task.due_date),
            "due_time":str(task.due_time),
            'user':self.getUser(task.user_id)}

        return dataReturn

