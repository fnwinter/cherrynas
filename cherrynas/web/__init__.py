# Copyright 2022 fnwinter@gmail.com

import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.datastructures import Headers

from config import ACCOUNT_DB_PATH
from utils.hash import get_today_hash

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
STATIC_PATH = os.path.join(SCRIPT_PATH, "static")

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

    MainView.register(app, '/cherry/')
    ExplorerView.register(app, '/cherry/explorer/')
    ImageView.register(app, '/cherry/image/')
    MovieView.register(app, '/cherry/movie/')
    MusicView.register(app, '/cherry/music/')
    BookView.register(app, '/cherry/book/')
    SyncView.register(app, '/cherry/sync/')
    ProxyView.register(app, '/cherry/proxy/')

    # create account view
    from web.account.login_view import LoginView
    from web.account.logout_view import LogoutView
    from web.account.signup_view import SignupView
    from web.account.reset_view import ResetView

    LoginView.register(app, '/cherry/login/')
    LogoutView.register(app, '/cherry/logout/')
    SignupView.register(app, '/cherry/signup/')
    ResetView.register(app, '/cherry/reset_password/')

    # admin view
    from web.admin.admin_view import AdminView
    AdminView.register(app, '/cherry/admin/')

def create_db(app):
    DB.init_app(app)
    MIGRATE.init_app(app, DB)

def create_app():
    app = Flask(__name__, static_folder=STATIC_PATH, static_url_path='/cherry/static')
    app.config['debug'] = True
    app.config["SECRET_KEY"] = get_today_hash()
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{ACCOUNT_DB_PATH}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app, resources={r'/*': {'origins': '*'}})

    create_view(app)

    create_db(app)

    from web.proxy.proxy_handler import proxy_handler
    proxy_handler(app)

    return app
