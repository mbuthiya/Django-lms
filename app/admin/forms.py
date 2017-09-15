from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import SubmitField,SelectField,StringField,TextAreaField


class CreateLesson(FlaskForm):
    title = StringField("Title for the lesson", validators = [Required()])
    days = SelectField('Day',choices =[("Monday","Monday"),("Tuesday","Tuesday"),("Wednesday","Wednesday"),("Thursday","Thursday"),("Friday","Friday")])
    body = TextAreaField("Edit your content Markdown", validators = [Required()])
    submit = SubmitField("Submit Lesson")
