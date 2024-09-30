from flask import Flask, render_template

app=Flask(__name__)

posts = [
    {
        'author':'Tarek Mohamed',
        'title': 'Post1',
        'content': 'First Post content',
        'date_posted': '30 Sep 2024'
    },
    {
        'author':'Anagram Mohamed',
        'title': 'Post2',
        'content': 'Second Post content',
        'date_posted': '29 Sep 2024'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title='about')

if __name__ == '__main__':
    app.run(debug=True)