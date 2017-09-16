from . import main
from flask import render_template,abort
from ..models import Lesson
from .. import db
import markdown2



@main.route('/')
def index():
    weeks = get_weeks()
    return display_day(1,weeks)


@main.route('/<int:day_num>')
def day_content(day_num):
    weeks = get_weeks()

    return display_day(day_num,weeks)



def display_day(day_num,weeks):

        day = Lesson.query.filter_by(day_number = day_num).first()
        if day:
            html_doc = markdown2.markdown(day.body,extras=["code-friendly", "fenced-code-blocks"])
            title = f'{day.day_name} day {day.day_number}'
            return render_template('main/index.html',weeks=weeks,day=day,html_doc = html_doc,title=title)
        else:
            abort(404)



def get_weeks():
    week1 =Lesson.query.filter_by(week_number = 1).order_by(Lesson.day_number).all()
    week2 =Lesson.query.filter_by(week_number = 2).order_by(Lesson.day_number).all()
    week3 =Lesson.query.filter_by(week_number = 3).order_by(Lesson.day_number).all()
    week4 =Lesson.query.filter_by(week_number = 4).order_by(Lesson.day_number).all()
    week5 =Lesson.query.filter_by(week_number = 5).order_by(Lesson.day_number).all()
    week6 =Lesson.query.filter_by(week_number = 6).order_by(Lesson.day_number).all()

    weeks = {"Precourse Work":['Pre-course Work',week1,"collapse1"],
            "OOP and Unittesting":['Week 1',week2,"collapse2"],
            "Introduction To Flask":["Week 2",week3,"collapse3"],
            "Working With Databases":["Week 3",week4,"collapse4"],
            "Pair Project Week":["Week 4",week5,"collapse5"],
            "Group Project":["Week 5",week6,"collapse6"]}

    return weeks
