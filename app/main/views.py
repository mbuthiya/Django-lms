from . import main
from flask import render_template
from ..models import Lesson
from .. import db

@main.route('/')
def index():
    weeks = get_weeks()
    day = Lesson.query.filter_by(day_number = 1).first()
    return render_template('main/index.html',weeks=weeks,day=day)

@main.route('/<int:day_num>')
def day_content(day_num):
    weeks = get_weeks()
    day = Lesson.query.filter_by(day_number = day_num).first()
    return render_template('main/index.html',weeks=weeks,day=day)

def get_weeks():
    week1 =Lesson.query.filter_by(week_number = 1).order_by(Lesson.day_number).all()
    weeks = {"Introduction To flask":week1}

    return weeks
