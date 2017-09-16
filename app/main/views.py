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
            html_doc = markdown2.markdown(day.body,extras=["code-friendly","fenced-code-blocks"])
            return render_template('main/index.html',weeks=weeks,day=day,html_doc = html_doc)
        else:
            abort(404)



def get_weeks():
    week1 =Lesson.query.filter_by(week_number = 1).order_by(Lesson.day_number).all()
    weeks = {"Introduction To flask":week1}

    return weeks
