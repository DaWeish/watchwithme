from flask import render_template, flash, redirect, request, session
from flaskext.mysql import MySQL
from app import myApp
from .forms import LoginForm, RegisterForm, EventForm

#can use variable parts to url with <variable_name> or convertor with <convertor:varname>
# can use int, float, and path as convertor (path accepts slashes)
# urls endind in / will work both with and without slash, without slash, it has to match

mysql = MySQL()
myApp.config['MYSQL_DATABASE_USER'] = 'connorw'
myApp.config['MYSQL_DATABASE_PASSWORD'] = 'watchwithmePass'
myApp.config['MYSQL_DATABASE_DB'] = 'watchWithMe'
myApp.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(myApp)


@myApp.route('/')
@myApp.route('/index')
def index():   
    db = mysql.connect()
    cursor = db.cursor()

    if 'userName' in session:
        cursor.execute("SELECT First, PID FROM Person WHERE Username=%s", [session['userName']])
        result = cursor.fetchone()
        name = "%s" % result[0]
        PID = "%s" % result[1]

        cursor.execute("""SELECT Name, Time, date, Title, Genre, e.EID
                        FROM Event as e, Media as m, EventHasMedia as ehm, Attend as a, Media_2 as mtwo
                        WHERE e.EID=ehm.EID AND m.MID=ehm.MID AND m.MID=mtwo.MID AND a.EID=e.EID AND a.PID=%s""", [PID])
        attendingEvents = [dict(Name=row[0], Time=row[1], Date=row[2], Title=row[3], Genre=row[4], Event=row[5]) for row in cursor.fetchall()]

        cursor.execute("""SELECT Name, Time, date, Title, Genre, e.EID
                        FROM Event as e, Media as m, EventHasMedia as ehm, Make_Event as me, Media_2 as mtwo
                        WHERE e.EID=ehm.EID AND m.MID=ehm.MID AND m.MID=mtwo.MID AND me.EID=e.EID AND me.PID=%s""", [PID])
        createdEvents = [dict(Name=row[0], Time=row[1], Date=row[2], Title=row[3], Genre=row[4], Event=row[5]) for row in cursor.fetchall()]

        cursor.execute("""SELECT Name, Time, date, Title, Genre, e.EID
                        FROM Event as e, Media as m, EventHasMedia as ehm, Media_2 as mtwo
                        WHERE e.EID=ehm.EID AND m.MID=ehm.MID AND m.MID=mtwo.MID;""")
        allEvents = [dict(Name=row[0], Time=row[1], Date=row[2], Title=row[3], Genre=row[4], Event=row[5]) for row in cursor.fetchall()]

        return render_template('index.html', title='Home', name=name, attendingEvents=attendingEvents, createdEvents=createdEvents, allEvents=allEvents)

    else:
        name = "Me"

    return render_template('index.html', title='Home', name=name)

@myApp.route('/login', methods = ['GET', 'POST'])
def login():
    loginForm = LoginForm(request.form)

    db = mysql.connect()
    cursor = db.cursor()

    if loginForm.validate() and request.method == 'POST':
 #       flash('Login requested for Username="%s", Password=%s' %
#              (loginForm.username.data, loginForm.password.data))

        user = loginForm.username.data
        cursor.execute("SELECT Password FROM Person WHERE Username=%s;", [user])
        inputPass = cursor.fetchone()
        print inputPass
#        flash('Password in Database is %s' % inputPass)

        if "%s" % inputPass == "%s" % loginForm.password.data:
#            flash('Password is correct! Logged in!')
            session['userName'] = loginForm.username.data
        else:
            return render_template('login.html', title="Sign In", login=loginForm)
        
        return redirect('/index')

    return render_template('login.html', title="Sign In", login=loginForm)

@myApp.route('/newEvent', methods = ['GET', 'POST'])
def createEvent():

    db = mysql.connect()
    cursor = db.cursor()

    if 'userName' in session:
        cursor.execute("SELECT First FROM Person WHERE Username=%s", [session['userName']])
        name = "%s" % cursor.fetchone()
    else:
        return redirect('/login')

    eventForm = EventForm(request.form)

    if eventForm.validate() and request.method == 'POST':
        name = "%s" % eventForm.eventname.data
        time = "%s" % eventForm.eventtime.data
        date = "%s" % eventForm.eventdate.data
        media = "%s" % eventForm.medianame.data
        genre = "%s" % eventForm.mediagenre.data

        cursor.execute("INSERT INTO Event(Time, Name, date) VALUES (%s, %s, %s);", [time, name, date])
        cursor.execute("SELECT LAST_INSERT_ID();")
        EID = "%s" % cursor.fetchone()
        print EID
        cursor.execute("SELECT PID FROM Person WHERE Username=%s", [session['userName']])
        PID = "%s" % cursor.fetchone()
        print PID
        cursor.execute("INSERT INTO Make_Event VALUES(%s, %s);", [PID, EID])
        cursor.execute("INSERT INTO Attend VALUES(%s, %s);", [PID, EID])
        cursor.execute("INSERT INTO Media(Title) VALUES(%s);", [media])
        cursor.execute("SELECT LAST_INSERT_ID();")
        MID = "%s" % cursor.fetchone()
        print MID
        cursor.execute("INSERT INTO Media_2 VALUES(%s, %s);", [MID, genre])
        cursor.execute("INSERT INTO EventHasMedia VALUES(%s, %s);", [EID, MID])
        db.commit()
 #       flash("Created Event with name: %s time: %s date: %s media: %s genre: %s" % (name, time, date, media, genre))
        return redirect('/index')

    return render_template('newevent.html', title="Create Event", name=name, event=eventForm)

@myApp.route('/logout')
def logout():
    session.pop('userName', None)
    return redirect('/login')

@myApp.route('/attend')
def attend():
    db = mysql.connect()
    cursor = db.cursor()

    if 'userName' in session:
        EID = request.args.get('EID', '')
#        flash('Eid is %s' % EID)

        cursor.execute("SELECT PID FROM Person WHERE Username=%s", [session['userName']])
        PID = "%s" % cursor.fetchone()

        cursor.execute("SELECT PID FROM Attend WHERE PID=%s AND EID=%s", [PID, EID])
        result = cursor.fetchone()

        if result is None:
            cursor.execute("INSERT INTO Attend VALUES(%s, %s);", [PID, EID])
        else:
            cursor.execute("DELETE FROM Attend WHERE PID=%s AND EID=%s;", [PID, EID])

        db.commit()

    return redirect('/index')

@myApp.route('/register', methods = ['GET', 'POST'])
def register():
    db = mysql.connect()
    cursor = db.cursor()

    registerForm = RegisterForm(request.form)

    if registerForm.validate() and request.method == 'POST':
 #       flash('Register requested for Username="%s", Password=%s' %
 #             (registerForm.username.data, registerForm.password.data))

        first = "%s" % registerForm.firstname.data
        last = "%s" % registerForm.lastname.data
        user = "%s" % registerForm.username.data
        password = "%s" % registerForm.password.data

        cursor.execute("INSERT INTO Person(First, Last, Username, Password) VALUES (%s, %s, %s, %s);", [first, last, user, password])
        db.commit()

        session['userName'] = registerForm.username.data
        return redirect('/index')

    return render_template('register.html', title="Sign Up", register=registerForm)