from . import main
from flask import render_template
from ..models import Lesson
from .. import db

@main.route('/')
def index():
    week1 =Lesson.query.filter_by(week_number = 1).all()
    weeks = {"Introduction To flask":week1}
    return render_template('main/index.html',weeks=weeks)
