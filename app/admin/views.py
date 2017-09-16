from . import admin
from flask import render_template,redirect,url_for
from .forms import CreateLesson,UpdateLesson
from ..models import Lesson # soon to update to day
from .. import db
from flask_login import login_required
import pyperclip



@admin.route('/dashboard')
@login_required
def dashboard():

    days = Lesson.query.order_by(Lesson.day_number).all()
    title = 'MS curriculum dashboard'
    return render_template('admin/dashboard.html',days=days)


@admin.route('/update/<int:id>',methods = ['GET','POST'])
@login_required
def update_lesson(id):

#  Getting the days lesson
    day = Lesson.query.filter_by(id = id).first()

    # Instanciate form
    form = UpdateLesson()
    pyperclip.copy(day.body)
    form.lessons.render_kw={'value':day.lessons}

    if form.validate_on_submit():
        body = form.body.data
        lessons = form.lessons.data

        day.body = body
        day.lessons = lessons
        db.session.commit()
        return redirect(url_for('.dashboard'))

    title = f'Update {day.day_name} day {day.day_number}'
    return render_template('admin/update.html',form=form,title=title)


@admin.route('/dashboard/newLesson',methods = ['GET','POST'])
@login_required
def newLesson():
    form = CreateLesson() # create a day
    if form.validate_on_submit():
        day = int(form.days.data)
        week = int(form.weeks.data)
        body = form.body.data
        lessons = form.lessons.data
        weekday = get_week_day(day)
        doc_num = day * week

        if validate_new_lesson(doc_num):
            new_day = Lesson(day_number=doc_num,week_number=week,day_name=weekday,body=body,lessons=lessons)
            new_day.save_lesson()

        return redirect(url_for('.dashboard'))
    title = 'New Lesson'
    return render_template('admin/newLesson.html',form = form,title=title)


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


def validate_new_lesson(day_num):

    lesson = Lesson.query.filter_by(day_number =day_num).first()

    if lesson:
        flash("That day already has lessons Go to edit it")
        return False
    else:
        return True
