from flask_classful import FlaskView, route
from flask import render_template, redirect, session
from flask import current_app as app

from web.account.login_form import LoginForm
from web.database.account_db import Account
from web import db

class LoginView(FlaskView):
    default_methods = ['GET', 'POST']

    @route("/")
    def show(self):
        if session.get('email'):
            return redirect('/')

        _form = LoginForm()
        return render_template('/account/login.html', form=_form)

    def post(self):
        _form = LoginForm()
        if _form.validate_on_submit():
            _email = _form['email'].data
            _password = _form['password'].data
            
            if self.login(_email, _password):
                return redirect("/")
        return render_template('/account/login.html', form=_form)

    def login(self, email, password):
        result = db.session.query(Account).filter_by(email=f"{email}", password=f"{password}")
        if result.first():
            print("email found, add email to session")
            session['email'] = f"{email}"
            return True
        return False
