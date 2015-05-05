README For WatchWithMe
by Connor Walsh

---- Part 1: Setting up the Database ------

1. Make sure MySQL is installed on the machine.
2. Create a user for the database named 'connorw'@'localhost' with
	password=watchwithmePass  OR edit the views.py file at the top
	in the lines that say myApp.config(...) to mirror the values used
3. With the user logged into MySQL run the createTables.sql file to create
	the database and also all of the tables used in the schema

---- Part 2: Installing Flask framework ------

1. Make sure Python is installed on the machine.
2. Make sure pip (Pip installs Packages) is also installed
3. If virtualenv is not installed, run 'pip install virtualenv'
	or the equivalent command on your operating system.
4. Extract the source code files.
5. Navigate to the top level watchwithme folder.
6. Run the command '. venv/bin/activate' to select the virtualenv
7. Then install flask and its add-ons with:
	pip install flask flask-wtf flask-mysql

---- Part 3: Starting the Server -----
8. If everything installed correctly, you should be able to run
	./run.py in a terminal window which will start the server.
9. In a web browser, go to localhost:5000 to view the homepage
10. To shut down the server, use Ctrl-C