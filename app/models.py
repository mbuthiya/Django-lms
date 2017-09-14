from . import db

class Lesson(db.Model):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer,primary_key = True)
    lesson_title = db.Column(db.String(250))
    lesson_content = db.Column(db.String)
    lesson_day = db.Column(db.String)
    week_id = db.Column(db.Integer,db.ForeignKey('weeks.id'))


class Week(db.Model):
    __tablename__ = 'weeks'

    id = db.Column(db.Integer,primary_key = True)
    week_topic = db.Column(db.String(250))
    lessons = db.relationship('Lesson',backref = 'week', lazy ='dynamic')
