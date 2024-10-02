from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app=Flask(__name__)
app.config['SECRET_KEY'] = 'b48b31ba403d153e7a91cf92f7a7caeb'
#for TLS, we need a random set of chars
#we can get from secrets.token_hex(16)
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

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html",title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)