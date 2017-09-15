from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import SubmitField,SelectField,StringField,TextAreaField



class CreateLesson(FlaskForm):

    days = SelectField('Day',choices =[("1","Monday"),("2","Tuesday"),("3","Wednesday"),("4","Thursday"),("5","Friday")],validators = [Required()])
    weeks =  SelectField('Week',choices = [("1","Week 1"),("2","Week 2"),("3","Week 3 "),("4","Week 4"),("5","Week 5")],validators = [Required()])
    body = TextAreaField("Edit your content Markdown")
    lessons = StringField('Enter the lessons on this day separated by commas',validators = [Required()])
    submit = SubmitField("Submit Lesson")


class UpdateLesson(FlaskForm):

    body = TextAreaField()
    lessons = StringField('Update lessons on this day separated by commas',validators = [Required()])
    submit = SubmitField("Submit Lesson")
