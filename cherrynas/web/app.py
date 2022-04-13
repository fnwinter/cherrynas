import sys
import os

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_PATH = os.path.join(SCRIPT_PATH, os.path.pardir)
sys.path.append(ROOT_PATH)

from web import DB
from web import create_app, create_config

if __name__ == "__main__":
    create_config()

    app = create_app()
    app.app_context().push()

    DB.create_all(app=app)
    app.run(host='0.0.0.0', port='5000', debug=True)