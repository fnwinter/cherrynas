# Copyright 2022 fnwinter@gmail.com

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class AdminForm(FlaskForm):
    """
    AdminForm
    """
    data = StringField("data")
    submit = SubmitField("apply")
