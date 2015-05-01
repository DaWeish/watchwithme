from flask import Flask

myApp = Flask(__name__)
myApp.config.from_object('config')

from app import views
