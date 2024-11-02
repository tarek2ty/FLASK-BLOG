#this will start the app and bring together the different components
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask(__name__)
app.config['SECRET_KEY'] = 'b48b31ba403d153e7a91cf92f7a7caeb'
#for TLS, we need a random set of chars
#we can get from secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#we need to provide a uri for our database
#sql is just a file in our system; simply site.db is in our path
#the three forward slashes: two for the uri like http://
#and one for the relative path
db = SQLAlchemy(app) #this is the db instance
                     #each db structure is a class
bcrypt = Bcrypt(app) #initialize the bcrypt class
                     #Change The Registration Logic in routes.py
login_manager = LoginManager(app)   #manage the logging mechanism
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.app_context().push()

from flaskblog import routes