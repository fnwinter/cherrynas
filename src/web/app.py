import hashlib
import os

from datetime import date

from flask import Flask

from main.main_view import MainView

from explorer.explorer_view import ExplorerView

from account.login_view import LoginView
from account.logout_view import LogoutView
from account.signup_view import SignupView
from account.reset_view import ResetView

md5_hash = hashlib.md5()
md5_hash.update( f"date.today()".encode("utf-8") )
hash_key = md5_hash.digest()
print(f" * Hash key : {hash_key}")

file_path = os.path.dirname(os.path.realpath(__file__))
static_path = os.path.join(file_path, "static")
print(static_path)
app = Flask(__name__, static_folder=static_path)
app.config["SECRET_KEY"] = hash_key

MainView.register(app, '/')
LoginView.register(app, '/login')
LogoutView.register(app, '/logout')
SignupView.register(app, '/signup')
ResetView.register(app, '/reset_password')

ExplorerView.register(app, '/explorer')