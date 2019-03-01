from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, DecimalField, HiddenField, SelectField, validators

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=144, message="Name must be between 2-144 characters.")])
    username = StringField("Username", [validators.Length(min=2, max=144, message="Username must be between 2-144 characters.")])
    password = PasswordField("Password", [
        
        validators.EqualTo('confirm', message='Passwords must match.'),
        validators.Length(min=6, message="Password length must be at least 6 characters.")
    ])
    confirm = PasswordField('Repeat Password')

    class Meta:
        csrf = False

class UserEditForm(FlaskForm):
    id = HiddenField()
    name = StringField("Name", [validators.Length(min=2, max=144, message="Name must be between 2-144 characters.")])
    salary = DecimalField("Price", [validators.NumberRange(min=0, max=500, message="Salary must be between 0.00-500.00 euros.")], places=2)
    role = SelectField("Role", choices=[('manager', 'manager'), ('employee', 'employee')])

    class Meta:
        csrf = False