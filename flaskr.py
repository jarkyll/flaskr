

# what are the imports required?

import sqlite3
from flask import Flask, request, session, g, redirect, url_for,  \
	abort, render_template, flash



# configurations

# what is our database?
DATABASE = 'tmp/flaskr.db'
# are we debugging?
DEBUG = True
# do we have a secret key?
SECRET_KEY = 'development key'
# who is the user?
USERNAME = 'admin'
# what is the password?
PASSWORD = 'default'


# create the app
app = Flask(__name__)
app.config.from_object(__name__)
# from object looks at the object and finds all the uppercase variables
# you can replace app.config.from_object with app.config.from_envvar('FLASKR_SETTINGS', silent = True)

# this way the environment variable can be called FLASKR_SETTINGS to be a file to be loaded and the silent being true tells flaskr to not complain if a file was not found

# time to connectt the database 

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])
# it uses brackets because you are accessing a map with key DATABASE


# now you want to have this be a main app where it can't be imported 
# into other modules 
if __name__ == '__main__':
	app.run()

