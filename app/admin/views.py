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

        new_day = Lesson(day_number=day,week_number=week,body=body,lessons=lessons)
        new_day.save_lesson()
        return redirect(url_for('main.index'))



    return render_template('admin/newLesson.html',form = form)
