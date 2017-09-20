from . import admin
from flask import render_template,flash,redirect,url_for,request
from .forms import CreateLesson
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


    if request.method == 'POST':
        body = request.form.get('body')
        lessons = request.form.get("lessons")

        day.body = body
        day.lessons = lessons
        db.session.commit()
        return redirect(url_for('.dashboard'))

    title = f'Update {day.day_name} day {day.day_number}'
    return render_template('admin/update.html',title=title,day=day)


@admin.route('/delete/<int:id>',methods = ['POST'])
@login_required
def delete(id):
    day = Lesson.query.filter_by(id = id).first()
    db.session.delete(day)
    db.session.commit()
    return redirect(url_for('.dashboard'))





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
        doc_num = get_doc_number(week,day)

        if validate_new_lesson(doc_num):
            new_day = Lesson(day_number=doc_num,week_number=week,day_name=weekday,body=body,lessons=lessons)
            new_day.save_lesson()
        else:
            return redirect(url_for('.newLesson'))


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
    else:
        weekday = 'Weekend'

    return weekday


def validate_new_lesson(day_num):

    lesson = Lesson.query.filter_by(day_number =day_num).first()

    if lesson:
        flash("That day already has lessons Try editing it")
        return False
    else:
        return True

def get_doc_number(week,day):
    num_sum = None
    if week == 1:
        num_sum =0
    elif week == 2:
        num_sum = 7
    elif week == 3:
        num_sum = 14
    elif week == 4:
        num_sum = 15
    elif week == 5:
        num_sum =21

    sum=day+num_sum

    return sum
