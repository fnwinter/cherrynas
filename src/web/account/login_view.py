from flask_classful import FlaskView, route
from flask import render_template, redirect, session

from web.account.login_form import LoginForm
from web.database.account_db import Account
from web import DB

class LoginView(FlaskView):
    default_methods = ['GET', 'POST']

    @route("/")
    def show(self):
        if session.get('email'):
            return redirect('/')

        _form = LoginForm()
        return render_template('/account/login.html', form=_form, error_msg=None)

    def post(self):
        _form = LoginForm()
        error_msg_ = None
        if _form.validate_on_submit():
            _email = _form['email'].data
            _password = _form['password'].data
         
            login_result = self.login(_email, _password)
            if login_result == 'not_allowed':
                error_msg_ = 'this account is not permitted by admin yet.'
            if login_result == 'success':
                return redirect("/")
        else:
            error_msg_ = 'email or password is wrong'

        return render_template('/account/login.html', form=_form, error_msg=error_msg_)

    def login(self, email, password):
        try:
            result = DB.session.query(Account).filter_by(email=f"{email}", password=f"{password}")
            account = result.first()
            if account and not account.allowed_by_admin:
                return 'not_allowed'

            if account:
                session['email'] = f"{email}"
                session['nick_name'] = f"{account.nick_name}"
                return 'success'
        except Exception as e:
            print("login_view : " + e)
            return 'fail'
        return 'fail'
