from flask_classful import FlaskView, route
from flask import render_template, session

from web.account.reset_form import ResetForm, RequestPinForm
from utils.send_email import EMail

class ResetView(FlaskView):
    default_methods = ['GET', 'POST']

    @route("/")
    def show(self):
        _request_form = RequestPinForm()
        _reset_form = ResetForm()

        print(session.get('reset_pwd_email'))
        _email = session.get('reset_pwd_email')
        _request_form.email = f"{_email}" if _email else ""

        return render_template('/account/reset.html', reset_form=_reset_form, request_form=_request_form)

    def post(self):
        _request_form = RequestPinForm()
        _reset_form = ResetForm()

        if _request_form.validate_on_submit():
            print("request form")
            _email = _request_form['email'].data
            session['reset_pwd_email'] = f"{_email}"
            _request_form.email = f"{_email}"
            print(_email)
            if _email:
                self.send_email_with_pin(_email)
            
        if _reset_form.validate_on_submit():
            _email = f"{session.get('reset_pwd_email')}"
            _request_form.email = _email
            _password = _reset_form["password"].data
            _password_confirm = _reset_form["password_confirm"].data
            print("reset form")
            print("email", _email)
            print("reset_pin",_reset_form["reset_pin"].data)
            print("password", _password)
            print("password_confirm", _password_confirm)
            if _password == _password_confirm and _password != "":
                self.change_password(_email, _password)

        return render_template('/account/reset.html', reset_form=_reset_form, request_form=_request_form)

    def change_password(self, email, password):
        pass

    def send_email_with_pin(self, email):
        email = EMail(email)
        email.set_title("pin number")
        email.set_text("1234")
        email.send_mail()

    def update_pin_number(self):
        pass

    def get_pin_number(self):
        pass
