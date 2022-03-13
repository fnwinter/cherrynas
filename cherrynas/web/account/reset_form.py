from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class RequestPinForm(FlaskForm):
    email = StringField("email",
                        validators=[DataRequired(), Email()])
    submit = SubmitField("request pin numebr")
    email_remember = None

class ResetForm(FlaskForm):
    reset_pin = StringField("pin number")
    password = PasswordField("new password",
                             validators=[DataRequired(), Length(min=4, max=20)])
    password_confirm = PasswordField("password confirm",
                                     validators=[DataRequired(), Length(min=4, max=20)])

    submit = SubmitField("submit")
