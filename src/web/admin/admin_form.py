from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class AdminForm(FlaskForm):
    data = StringField("data")
    submit = SubmitField("apply")
