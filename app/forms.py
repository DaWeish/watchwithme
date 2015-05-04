#from flask.ext.wtf import Form
from wtforms import Form, TextField, BooleanField, PasswordField, validators

class LoginForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.Required()])

class RegisterForm(Form):
	firstname = TextField('First Name', [validators.Length(min=2, max=30)])
	lastname = TextField('Last Name', [validators.Length(min=2, max=30)])
	username = TextField('Username', [validators.Length(min=4, max=25)])
   	password = PasswordField('Password', [validators.Required()])
