# Copyright 2022 fnwinter@gmail.com

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class SignUpForm(FlaskForm):
    """
    SignUpForm
    """
    email = StringField("email",
                        validators=[DataRequired(), Email()])
    nick_name = StringField("nickname")
    password = PasswordField("password",
                             validators=[DataRequired(), Length(min=4, max=20)])
    password_confirm = PasswordField("password confirm",
                                     validators=[DataRequired(), Length(min=4, max=20)])
    submit = SubmitField("signUp")
