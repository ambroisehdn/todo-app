from flask_apscheduler import APScheduler
from model import Task as TaskModel
from datetime import date,datetime
from helper import timeDiff

scheduler = APScheduler()


# def specificDeadLine(): with user id and task id

@scheduler.task('interval', id='do_job_1', seconds=5, misfire_grace_time=900)
def globalDeadLine(): #all tasks
    with scheduler.app.app_context():
        tasks = TaskModel.query.all()
        for task in tasks :
            today = date.today()
            if today == task.due_date:
                current_time = datetime.time(datetime.now())
                diffResult = timeDiff(task.due_time,current_time) # sec , min ,hours
                if(diffResult["sec"] <= 5) : #for 5 second ! it is apply to all task
                    print("Your time is ready ! Say no to procrastination and get your work done")