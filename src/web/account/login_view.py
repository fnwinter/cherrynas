from flask_classful import FlaskView
from flask import render_template, redirect, session

from account.login_form import LoginForm
from database.login_db import Account

class LoginView(FlaskView):
    default_methods = ['GET', 'POST']

    def index(self):
        form = LoginForm()
        if form.validate_on_submit():
            q = db_session.query(Account).filter_by(email="%s" % form.email.data, password="%s"%form.password.data)
            if q.first():
                print("found", form['email'].data )
                session['email'] = "%s" % form['email'].data
            else:
                print("not found")
            return redirect('/')
        return render_template('/account/login.html', form=form)