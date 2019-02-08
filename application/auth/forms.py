from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=144)])
    username = StringField("Username", [validators.Length(min=2, max=144)])
    password = PasswordField("Password", [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(min=6)
    ])
    confirm = PasswordField('Repeat Password')

    class Meta:
        csrf = False