#from flask.ext.wtf import Form
from wtforms import Form, TextField, BooleanField, PasswordField, validators

class LoginForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.Required()])

class RegisterForm(Form):
	username = TextField('Username', [validators.Length(min=4, max=25)])
   	password = PasswordField('Password', [validators.Required()])
