from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {"nickname" : "Amy"}
    posts = [
        {
            'author' : {'nickname' : 'John'},
            'body' : 'Here is some fake content!'
        },
        {
            'author' : {'nickname' : 'Mary'},
            'body' : 'Really excellent blog post from Mary.'
        }
    ]
    return render_template("index.html", 
        title="Home", 
        user=user, 
        posts=posts)