from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class RequestPinForm(FlaskForm):
    email = StringField("이메일",
                        validators=[DataRequired(), Email()])
    submit = SubmitField("핀번호 요청")

class ResetForm(FlaskForm):
    reset_pin = StringField("핀번호")
    password = PasswordField("비밀번호",
                             validators=[DataRequired(), Length(min=4, max=20)])
    password_confirm = PasswordField("비밀번호 확인",
                                     validators=[DataRequired(), Length(min=4, max=20)])

    submit = SubmitField("전송")
