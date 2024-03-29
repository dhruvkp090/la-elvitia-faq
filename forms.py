from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class FAQform(FlaskForm):
    Question = StringField('Question', validators=[DataRequired()])
    Answer = TextAreaField('Answer', validators=[DataRequired()])
    submit = SubmitField('Add')
