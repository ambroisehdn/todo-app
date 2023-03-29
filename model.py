import datetime
from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String())
    username = db.Column(db.String(),unique=True)
    password = db.Column(db.String())
    created_at = db.Column(db.DateTime,nullable=False,server_default=db.func.now())
    update_at = db.Column(db.DateTime, nullable=False,
                          server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, fullName, username, password):
        self.fullName = fullName
        self.username = username
        self.password = password
        super(User, self).__init__()

    def __repr__(self):
        return '<id {}>'.format(self.id)

class TaskStatus(enum.Enum):

    Pending = "Pending"
    InProgress = "In progress"
    OnHold = "On hold"
    Completed = "Completed"
    Cancelled = "Cancelled"

    def __str__(self):
        return '%s' % self.value

    @classmethod
    def list(cls):
        #return list({i.name: i.value for i in TaskStatus})
        return list(map(lambda c: c.value, cls))

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.Text())
    status = db.Column(db.Enum(TaskStatus))
    due_date = db.Column(db.Date, nullable=False)
    due_time = db.Column(db.Time, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship("User", foreign_keys=[user_id])
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    update_at = db.Column(db.DateTime, nullable=False,
                          server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, title, description,due_date,due_time,status,user_id):
        self.title = title
        self.description = description
        self.status = status
        self.due_date = datetime.date.fromisoformat(due_date)
        self.due_time = datetime.time.fromisoformat(due_time)
        self.user_id = user_id
        super(Task, self).__init__()

    def __repr__(self):
        return '<id {}>'.format(self.id)
