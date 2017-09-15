from . import db
from markdown import markdown
import bleach

class Lesson(db.Model):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer,primary_key = True)
    day_number = db.Column(db.Integer)
    week_number = db.Column(db.Integer)
    body = db.Column(db.String)
    body_html = db.Column(db.Text)
    lessons = db.Column(db.String)

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):

        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
        'h1', 'h2', 'h3', 'p']
        target.body_html = bleach.linkify(bleach.clean(
        markdown(value, output_format='html'),
        tags=allowed_tags, strip=True))


    def save_lesson(self):
        db.session.add(self)
        db.session.commit()
        
db.event.listen(Lesson.body,'set',Lesson.on_changed_body)
