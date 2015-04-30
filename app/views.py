from flask import render_template
from app import myApp

#can use variable parts to url with <variable_name> or convertor with <convertor:varname>
# can use int, float, and path as convertor (path accepts slashes)
# urls endind in / will work both with and without slash, without slash, it has to match

@myApp.route('/')
@myApp.route('/index')
def index():
    events = [
    {'title' : 'Tuesday Movie Night', 'media' : 'The Imitation Game'},
    {'title' : 'Hump Day Celebration', 'media' : 'Shawshank Redemption'}
    ]

    return render_template('index.html', title='Home', events=events)
