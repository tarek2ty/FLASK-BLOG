from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

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

app.app_context().push()

class User(db.Model): #the table of the users
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

posts = [
    {
        'author':'Tarek Mohamed',
        'title': 'Post1',
        'content': 'First Post content',
        'date_posted': '30 Sep 2024'
    },
    {
        'author':'Anagram Steven',
        'title': 'Post2',
        'content': 'Second Post content',
        'date_posted': '29 Sep 2024'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title='about')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template("register.html",title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash(f'Logged In Successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Unsuccessful Login! Check Username and Password!', 'danger')
    return render_template("login.html",title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)