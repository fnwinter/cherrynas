from email_validator import validate_email, EmailSyntaxError
from flask_classful import FlaskView, route
from flask import render_template, redirect, session

from web.account.signup_form import SignUpForm
from web.common.decorator import login_required
from web.database.account_db import Account
from web import DB

class SignupView(FlaskView):
    default_methods = ['GET', 'POST']

    @route("/")
    @login_required
    def show(self):
        _form = SignUpForm()
        return render_template('/account/signup.html', form=_form)

    def post(self):
        _form = SignUpForm()
        _result = None
        if _form.validate_on_submit():
            _email = _form['email'].data
            _nick_name = _form['nick_name'].data
            _password = _form['password'].data
            _password_confirm = _form['password_confirm'].data

            if _password == _password_confirm:
                _result = self.signup(_email, _nick_name, _password)
                if not _result:
                    return redirect("/")
            else:
                _result = "password is not same"
        else:
            _result = "email or form is not valid"
        return render_template('/account/signup.html', form=_form, error_msg=_result)

    def signup(self, email, nick_name, password):
        form = SignUpForm()
        error_msg_ = None
        if form.validate_on_submit():
            query_ = DB.session.query(Account).filter_by(email=f"{email}")
            if query_.first():
                error_msg_ = "email already exists"
            else:
                new_account = Account(email=\
                    f"{email}", nick_name=f"{nick_name}", password=f"{password}")
                DB.session.add(new_account)
                DB.session.commit()
        return error_msg_

    def validate_email(self, email):
        try:
            validate_email(email)
        except EmailSyntaxError as e:
            return False
        return True

