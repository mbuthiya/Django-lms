from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
