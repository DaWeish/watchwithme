#from flask.ext.wtf import Form
from wtforms import Form, TextField, PasswordField, validators, RadioField

class LoginForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.Required()])

class RegisterForm(Form):
	firstname = TextField('First Name', [validators.Length(min=2, max=30)])
	lastname = TextField('Last Name', [validators.Length(min=2, max=30)])
	username = TextField('Username', [validators.Length(min=4, max=25)])
   	password = PasswordField('Password', [validators.Required()])

class EventForm(Form):
	eventname = TextField('Event Name', [validators.Length(min=4, max=40), validators.Required()])
	eventtime = TextField('Time', [validators.Required()])
	eventdate = TextField('Date', [validators.Required()])
	medianame = TextField('What you\' watching', [validators.Required()])
	mediagenre = TextField('Genre')