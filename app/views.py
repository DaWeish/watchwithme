from flask import render_template, flash, redirect, request, make_response
from app import myApp
from .forms import LoginForm

#can use variable parts to url with <variable_name> or convertor with <convertor:varname>
# can use int, float, and path as convertor (path accepts slashes)
# urls endind in / will work both with and without slash, without slash, it has to match

@myApp.route('/')
@myApp.route('/index')
def index():

    userName = request.cookies.get('username')
    events = [
    {'title' : 'Tuesday Movie Night', 'media' : 'The Imitation Game', 'owner': 'Connor', 'attending': 20},
    {'title' : 'Hump Day Celebration', 'media' : 'Shawshank Redemption', 'owner': 'Dillon', 'attending': 15}
    ]

    return render_template('index.html', title='Home', userName = userName, events=events)

@myApp.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested for Username="%s", Password=%s' %
              (form.username.data, form.password.data))
        response = make_response(redirect('/index'))
        response.set_cookie('username', form.username.data)
        return response

    return render_template('login.html', title="Sign In", form=form)

@myApp.route('/newEvent', methods = ['GET', 'POST'])
def createEvent():
    return render_template('newevent.html', title="Create Event")
