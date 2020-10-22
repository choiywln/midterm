from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField


class SignUpForm(FlaskForm):
    username = StringField('title')
    password = PasswordField('writer')
    address = TextAreaField("Content")
    text = SelectField('Post List')
