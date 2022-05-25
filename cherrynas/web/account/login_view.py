# Copyright 2022 fnwinter@gmail.com

from config.config import Config
from config.version import get_full_version, get_commit_id
from utils.hash import hashed_password
from flask_classful import FlaskView, route
from flask import render_template, redirect, session

from web.account.login_form import LoginForm
from web.common.decorator import login_required
from web.database.account_db import Account
from web import DB

class LoginView(FlaskView):
    default_methods = ['GET', 'POST']

    @route("/")
    def show(self):
        _form = LoginForm()
        return render_template('/account/login.html',
            form=_form, error_msg=None,
            version=get_full_version())

    def post(self):
        _form = LoginForm()
        error_msg_ = 'email or password is wrong'
        if _form.validate_on_submit():
            _email = _form['email'].data
            _password = _form['password'].data

            login_result = self.login(_email, _password)
            if login_result == 'not_allowed':
                error_msg_ = 'this account is not permitted by admin yet.'
            elif login_result == 'success':
                return redirect("/cherry/")

        return render_template('/account/login.html',
            form=_form, error_msg=error_msg_,
            version=get_full_version())

    def login(self, email, password):
        try:
            # admin check first
            if self.is_admin(email, password):
                session['email'] = f"{email}"
                session['nick_name'] = 'admin'
                session['admin'] = 'yes'
                return 'success'
            else:
                session['admin'] = 'no'

            # db login
            result = DB.session.query(Account).filter_by(email=f"{email}", password=f"{password}")
            account = result.first()
            if account and not account.joined:
                return 'not_allowed'

            if account:
                session['email'] = f"{email}"
                session['nick_name'] = f"{account.nick_name}"
                return 'success'
        except Exception as e:
            print("login_view : " + e)
            return 'fail'
        return 'fail'

    def is_admin(self, email, password) -> bool:
        try:
            with Config() as c:
                email_ = c.get_value('ADMIN', 'ID')
                password_ = c.get_value('ADMIN', 'PASSWORD')
                if email == email_ and password_ == hashed_password(password):
                    return True
        except:
            return False
        return False
