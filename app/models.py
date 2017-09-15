from . import db
import bleach

class Lesson(db.Model):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer,primary_key = True)
    day_number = db.Column(db.Integer)
    day_name = db.Column(db.String)
    week_number = db.Column(db.Integer)
    body = db.Column(db.String)
    lessons = db.Column(db.String)


    def save_lesson(self):
        db.session.add(self)
        db.session.commit()
