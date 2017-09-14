from . import db

class Lesson(db.Model):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer,primary_key = True)
    lesson_title = db.Column(db.String(250))
    lesson_content = db.Column(db.String)
    day_id = db.Column(db.Integer,db.ForeignKey('days.id'))
    week_id = db.Column(db.Integer,db.ForeignKey('weeks.id'))


class Day(db.Model):
    __tablename__ = 'days'

    id = db.Column(db.Integer,primary_key = True)
    day_name = db.Column(db.String(250))
    lessons = db.relationship('Lesson',backref = 'day', lazy ='dynamic')




class Week(db.Model):
    __tablename__ = 'weeks'

    id = db.Column(db.Integer,primary_key = True)
    week_topic = db.Column(db.String(250))
    lessons = db.relationship('Lesson',backref = 'week', lazy ='dynamic')
