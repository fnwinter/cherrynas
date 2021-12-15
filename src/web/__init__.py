import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from web.util.today_hash import get_today_hash

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
STATIC_PATH = os.path.join(SCRIPT_PATH, "static")
HASH_KEY = get_today_hash()
print(f" * Hash key : {HASH_KEY}")

db = SQLAlchemy()
migrate = Migrate()

def create_view(app):
    from web.main.main_view import MainView

    from web.explorer.explorer_view import ExplorerView

    from web.account.login_view import LoginView
    from web.account.logout_view import LogoutView
    from web.account.signup_view import SignupView
    from web.account.reset_view import ResetView

    MainView.register(app, '/')

    ExplorerView.register(app, '/explorer')

    LoginView.register(app, '/login')
    LogoutView.register(app, '/logout')
    SignupView.register(app, '/signup')
    ResetView.register(app, '/reset_password')

def create_db(app):
    db.init_app(app)
    migrate.init_app(app, db)

def create_app():
    app = Flask(__name__, static_folder=STATIC_PATH)
    app.debug=True
    app.config["SECRET_KEY"] = "!@#$#"#HASH_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///account.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    create_view(app)

    create_db(app)

    return app