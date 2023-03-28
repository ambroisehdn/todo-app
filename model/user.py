# import datetime as dt

# from marshmallow import Schema, fields,  post_load

# from your_orm import Model, Column, Integer, String, DateTime

# class User(object):
#     def __init__(self, username, password, fullName):
#         self.fullName = fullName
#         self.username = username
#         self.password = password
#         self.created_at = dt.datetime.now()
#         self.update_at = dt.datetime.now()

#     def __repr__(self):
#         return '<User(name={self.username!r})>'.format(self=self)


# class UserSchema(Schema):
#     fullName = fields.Str()
#     username = fields.Str()
#     password = fields.Number()
#     created_at = fields.Date()
#     update_at = fields.Date()
