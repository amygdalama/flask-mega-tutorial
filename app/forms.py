from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class LoginForm(Form):
    open_id = TextField('open_id', validators=[Required()])
    remember_me = BooleanField('remember_me', default=False)