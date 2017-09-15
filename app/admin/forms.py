from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtform import SubmitField,SelectField,StringField
from flask_pagedown.fields import PageDownField

class CreateLesson(FlaskForm):
    title = StringField("Title for the lesson", validators = [Required()])
    days = SelectField('Day',choices =[("Monday","Monday"),("Tuesday","Tuesday"),("Wednesday","Wednesday"),("Thursday","Thursday"),("Friday","Friday")])
    body = PageDownField("Edit your content Markdown", validators = [Required()])
    submit = SubmitField("Submit Lesson")
