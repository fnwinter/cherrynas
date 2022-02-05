import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from utils.today_hash import get_today_hash

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
STATIC_PATH = os.path.join(SCRIPT_PATH, "static")
HASH_KEY = get_today_hash()
print(f" * Hash key : {HASH_KEY}")

DB = SQLAlchemy()
MIGRATE = Migrate()

def create_view(app):
    # pages view
    from web.main.main_view import MainView
    from web.explorer.explorer_view import ExplorerView
    from web.image.image_view import ImageView
    from web.movie.movie_view import MovieView
    from web.music.music_view import MusicView
    from web.book.book_view import BookView
    from web.sync.sync_view import SyncView
    from web.proxy.proxy_view import ProxyView

    MainView.register(app, '/')
    ExplorerView.register(app, '/explorer/')
    ImageView.register(app, '/image/')
    MovieView.register(app, '/movie/')
    MusicView.register(app, '/music/')
    BookView.register(app, '/book/')
    SyncView.register(app, '/sync/')
    ProxyView.register(app, '/proxy/')

    # create account view
    from web.account.login_view import LoginView
    from web.account.logout_view import LogoutView
    from web.account.signup_view import SignupView
    from web.account.reset_view import ResetView

    LoginView.register(app, '/login/')
    LogoutView.register(app, '/logout/')
    SignupView.register(app, '/signup/')
    ResetView.register(app, '/reset_password/')

def create_db(app):
    DB.init_app(app)
    MIGRATE.init_app(app, DB)

def create_app():
    app = Flask(__name__, static_folder=STATIC_PATH)
    app.config['debug'] = True
    app.config["SECRET_KEY"] = "!@#$#"#HASH_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///account.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app, resources={r'/*': {'origins': '*'}})

    create_view(app)

    create_db(app)

    return app
