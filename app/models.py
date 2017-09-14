from . import db

class Lesson(db.Model):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(250))
    content = db.Column(db.String)
    day = db.Column(db.String)
