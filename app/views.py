from flask import flash, redirect, render_template
from app import app
from forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("OpenID=" + form.openid.data)
        flash("remember_me=" + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)