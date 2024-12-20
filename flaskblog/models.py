from flaskblog import db, login_manager 
from datetime import datetime
from flask_login import UserMixin #provide the default authentications when logging

#we need a decorator function that can find the user by id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin): #the table of the users
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(20), default='default.jpg', nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    #these are the columns for the table

    def __repr__(self):
        return f'User({self.username}, {self.email}, {self.image})'

class Post(db.Model): #the table for posts
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self) -> str:
        return f'Post({self.title}, {self.date_posted})'

def __initdb__():
    db.create_all()
__initdb__()