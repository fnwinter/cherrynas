from web import DB, create_app

DB.create_all(app=create_app())