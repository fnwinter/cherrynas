# Copyright 2022 fnwinter@gmail.com
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    """
    LoginForm
    """
    email = StringField("email",
                        validators=[DataRequired(), Email()])
    password = PasswordField("password",
                             validators=[DataRequired(), Length(min=4, max=20)])
    submit = SubmitField("login")
