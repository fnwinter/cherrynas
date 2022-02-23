import random

from flask_classful import FlaskView, route
from flask import render_template, session

from web.account.reset_form import ResetForm, RequestPinForm
from web.database.account_db import Account
from web import DB

from utils.send_email import EMail

class ResetView(FlaskView):
    default_methods = ['GET', 'POST']

    @route("/")
    def show(self):
        _request_form = RequestPinForm()
        reset_form_ = ResetForm()
        _email = session.get('reset_pwd_email')
        _request_form.email = f"{_email}" if _email else ""

        return render_template('/account/reset.html',
                               reset_form=reset_form_, request_form=_request_form)

    def post(self):
        _request_form = RequestPinForm()
        reset_form_ = ResetForm()

        if _request_form.validate_on_submit():
            _email = _request_form['email'].data
            session['reset_pwd_email'] = f"{_email}"
            _request_form.email = f"{_email}"
            if _email:
                self.send_email_with_pin(_email)

        if reset_form_.validate_on_submit():
            email_ = f"{session.get('reset_pwd_email')}"
            _request_form.email = email_
            reset_pin_ = reset_form_["reset_pin"].data 
            password_ = reset_form_["password"].data
            _password_confirm = reset_form_["password_confirm"].data
            if password_ == _password_confirm and password_ != "":
                self.change_password(email_, password_, reset_pin_)

        return render_template('/account/reset.html',
                               reset_form=reset_form_, request_form=_request_form)

    def get_pin_number(self, email):
        try:
            member = DB.session.query(Account).filter_by(email=f"{email}").first()
            pin = member.reset_pin
            return pin
        except Exception as e:
            print(e)

    def change_password(self, email, new_password, pin_number):
        db_pin = self.get_pin_number(email)
        if pin_number == db_pin:
            try:
                DB.session.query(Account).filter_by(email=f"{email}").update( { "password" : new_password })
                DB.session.commit()
            except Exception as e:
                print(e)

    def send_email_with_pin(self, email):
        try:
            pin_number = self.update_pin_number(email)
            if pin_number:
                email = EMail(email)
                email.set_title("pin number")
                email.set_text("pin number is " + pin_number)
                email.send_mail()
            else:
                print("fail to generate pin number")
        except Exception as e:
            print(e)

    def update_pin_number(self, email):
        new_pin = self.make_new_pin_number()
        try:
            DB.session.query(Account).filter_by(email=f"{email}").update({
                "reset_pin": new_pin
            })
            DB.session.commit()
        except Exception as e:
            print(e)
        return new_pin

    def make_new_pin_number(self):
        new_pin = ''
        for _ in range(6):
            new_pin += '%d' % random.randint(0,9)
        return new_pin