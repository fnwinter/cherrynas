from flask_classful import FlaskView, route
from flask import render_template, redirect, session

from account.signup_form import SignUpForm

from database.account_db import Account
from database.database_manager import DBManager

class SignupView(FlaskView):
    default_methods = ['GET', 'POST']

    @route("/")
    def show(self):
        if session.get('email'):
            return redirect('/')

        _form = SignUpForm()
        return render_template('/account/signup.html', form=_form)

    def post(self):
        _form = SignUpForm()
        if _form.validate_on_submit():
            _email = _form['email'].data
            _password = _form['password'].data
            _password_confirm = _form['password_confirm'].data
            if _password == _password_confirm:
                print(_password)
                print(_password_confirm)
                result = self.signup(_email, _password)
                if not result:
                    return redirect("/")
            else:
                result =  "password is not same"
        return render_template('/account/signup.html', form=_form, error_msg = result)

    def signup(self, email, password):
        form = SignUpForm()
        error_msg_ = None
        if form.validate_on_submit():
            db_session = DBManager().get_session()
            q = db_session.query(Account).filter_by(email=f"{email}")
            if q.first():
                error_msg_ = "email already exists"
            else:
                new_account = Account(email=f"{email}", password=f"{password}")
                db_session.add(new_account)
                db_session.commit()
        return error_msg_