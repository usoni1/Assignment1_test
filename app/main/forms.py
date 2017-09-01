from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('Enter Your name', validators=[DataRequired()])
    password = PasswordField('Provide Your password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SignUpForm(FlaskForm):
    name = StringField('Enter Your name', validators=[DataRequired()])
    password = PasswordField('Provide Your password', validators=[DataRequired()])
    submit = SubmitField('Submit')

