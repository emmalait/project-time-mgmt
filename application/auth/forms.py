from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, DecimalField, HiddenField, SelectField, validators

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=144)])
    username = StringField("Username", [validators.Length(min=2, max=144)])
    password = PasswordField("Password", [
        
        validators.EqualTo('confirm', message='Passwords must match'),
        validators.Length(min=6)
    ])
    confirm = PasswordField('Repeat Password')

    class Meta:
        csrf = False

class UserEditForm(FlaskForm):
    id = HiddenField()
    name = StringField("Name", [validators.Length(min=2, max=144)])
    salary = DecimalField("Price", places=2)
    role = SelectField("Role", choices=[('manager', 'manager'), ('employee', 'employee')])

    class Meta:
        csrf = False