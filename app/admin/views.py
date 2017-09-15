from . import admin
from flask import render_template,redirect,url_for
from .forms import CreateLesson
from ..models import Lesson # soon to update to day
from .. import db

@admin.route('/dashboard/newLesson',methods = ['GET','POST'])
def newLesson():
    form = CreateLesson() # create a day
    if form.validate_on_submit():
        day = int(form.days.data)
        week = int(form.weeks.data)
        body = form.body.data
        lessons = form.lessons.data
        weekday = get_week_day(day)
        doc_num = day * week

        new_day = Lesson(day_number=doc_num,week_number=week,day_name=weekday,body=body,lessons=lessons)
        new_day.save_lesson()
        return redirect(url_for('main.index'))



    return render_template('admin/newLesson.html',form = form)

def get_week_day(day_num):

    weekday = None
    if day_num == 1:
        weekday = 'Monday'
    elif day_num == 2:
        weekday = 'Tuesday'
    elif day_num == 3:
        weekday = 'Wednesday'
    elif day_num == 4:
        weekday = 'Thursday'
    elif day_num == 5:
        weekday = 'Friday'

    return weekday
