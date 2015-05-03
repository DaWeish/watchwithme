from flask import render_template, flash, redirect, request, session
from flaskext.mysql import MySQL
from app import myApp
from .forms import LoginForm, RegisterForm

#can use variable parts to url with <variable_name> or convertor with <convertor:varname>
# can use int, float, and path as convertor (path accepts slashes)
# urls endind in / will work both with and without slash, without slash, it has to match

#mysql = MySQL()
#myApp.config['MYSQL_DATABASE_USER'] = 'root'
#myApp.config['MYSQL_DATABASE_PASSWORD'] = 'Comawa15'
#myApp.config['MYSQL_DATABASE_DB'] = 'watchwithme'
#myApp.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(myApp)

# cursor = mysql.connect().cursor()
# cursor.execute("SQL STATEMENT GOES HERE")
# data = cursor.fetchone()
# if data is None:
#   returned nothing

@myApp.route('/')
@myApp.route('/index')
def index():
 #   if 'userName' in session:     
    events = [
    {'title' : 'Tuesday Movie Night', 'media' : 'The Imitation Game', 'owner': 'Connor', 'attending': 20},
    {'title' : 'Hump Day Celebration', 'media' : 'Shawshank Redemption', 'owner': 'Dillon', 'attending': 15}
    ]

    return render_template('index.html', title='Home', events=events)

@myApp.route('/login', methods = ['GET', 'POST'])
def login():
    loginForm = LoginForm(request.form)

    if loginForm.validate() and request.method == 'POST':
        flash('Login requested for Username="%s", Password=%s' %
              (loginForm.username.data, loginForm.password.data))
        session['userName'] = loginForm.username.data
        return redirect('/index')

    return render_template('login.html', title="Sign In", login=loginForm)

@myApp.route('/newEvent', methods = ['GET', 'POST'])
def createEvent():
    return render_template('newevent.html', title="Create Event")

@myApp.route('/logout')
def logout():
    session.pop('userName', None)
    return redirect('/login')

@myApp.route('/register', methods = ['GET', 'POST'])
def register():
    registerForm = RegisterForm(request.form)

    if registerForm.validate() and request.method == 'POST':
        flash('Register requested for Username="%s", Password=%s' %
              (registerForm.username.data, registerForm.password.data))
        session['userName'] = registerForm.username.data
        return redirect('/index')

    return render_template('register.html', title="Sign Up", register=registerForm)