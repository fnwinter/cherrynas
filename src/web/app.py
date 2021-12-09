from flask import Flask, session
from flask import render_template

from main.main_view import MainView

from account.login_view import LoginView
from account.logout_view import LogoutView
from account.signup_view import SignupView

app = Flask(__name__)
app.config["SECRET_KEY"] = '12345643214321432143214321'

MainView.register(app, '/')
LoginView.register(app, '/login')
LogoutView.register(app, '/logout')
SignupView.register(app, '/signup')
