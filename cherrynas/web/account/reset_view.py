# Copyright 2022 fnwinter@gmail.com

import random

from flask_classful import FlaskView, route
from flask import render_template, session, redirect

from utils.send_email import EMail
from web.account.reset_form import ResetForm, RequestPinForm
from web.database.account_db import Account
from web import DB

class ResetView(FlaskView):
    default_methods = ['GET', 'POST']

    @route("/")
    def show(self):
        request_form_ = RequestPinForm()
        reset_form_ = ResetForm()
        error_msg_ = None

        email_remember = session.get('reset_pwd_email')
        request_form_.email_remember = f"{email_remember}" if email_remember else ""

        return render_template('/account/reset.html',
                               reset_form=reset_form_, request_form=request_form_,
                               error_msg=error_msg_)

    def post(self):
        request_form_ = RequestPinForm()
        reset_form_ = ResetForm()
        error_msg_ = None

        if request_form_.validate_on_submit():
            email_ = request_form_['email'].data
            request_form_.email_remember = email_
            session['reset_pwd_email'] = f"{email_}"

            if email_ and self.check_email_exist(email_):
                self.send_email_with_pin(email_)
            else:
                error_msg_ = "email does not exist!"

        if reset_form_.validate_on_submit():
            email_ = f"{session.get('reset_pwd_email')}"

            request_form_.email_remember = email_
            reset_pin_ = reset_form_["reset_pin"].data
            password_ = reset_form_["password"].data
            password_confirm_ = reset_form_["password_confirm"].data
            if password_ == password_confirm_ and password_ != "":
                if self.change_password(email_, password_, reset_pin_):
                    return redirect('/')
                else:
                    error_msg_ = "pin number is not correct"
            else:
                error_msg_ = "confirm password does not match"

        return render_template('/account/reset.html',
                                request_form=request_form_,
                                reset_form=reset_form_,
                                error_msg=error_msg_)

    def get_pin_number(self, email):
        pin = None
        try:
            member = DB.session.query(Account).filter_by(email=f"{email}").first()
            pin = member.reset_pin
        except Exception as e:
            print(e)
        return pin

    def change_password(self, email, new_password, pin_number):
        db_pin = self.get_pin_number(email)
        if pin_number == db_pin:
            try:
                DB.session.query(Account).filter_by(email=f"{email}").update({"password" : new_password})
                DB.session.commit()
            except Exception as e:
                print(e)
            return True
        return False

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

    def check_email_exist(self, email):
        try:
            result = DB.session.query(Account).filter_by(email=f"{email}").first()
            if result:
                return True
        except Exception as e:
            print(e)
        return False
