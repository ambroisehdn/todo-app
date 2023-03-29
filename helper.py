from flask_restful import fields
from datetime import time,date

class DateFormat(fields.Raw):
    def format(self, value):
        return date.strftime(value,'%Y-%m-%d')

class TimeFormat(fields.Raw):
    def format(self, value):
        return time.strftime(value, "%H:%M")