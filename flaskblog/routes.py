from flaskblog.models import User, Post
from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app


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
