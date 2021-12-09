from database.login_db import Account

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from util.singleton import Singleton

class DBManager(Singleton):
    initialized = False
    engine = None

    def __init__(self) -> None:
        super().__init__()
        if not self.initialized:
            # create db engine
            self.engine = create_engine('sqlite:///account.db', echo=True)
            self.session = sessionmaker(bind=self.engine)
            self.create_tables()

    def get_session(self):
        return self.session()

    def create_tables(self):
        Account.__table__.create(bind=self.engine, checkfirst=True)
