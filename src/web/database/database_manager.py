from sqlalchemy import create_engine
from database.login_db import Account

engine = create_engine('sqlite:///account.db', echo=True)
Account.__table__.create(bind=engine, checkfirst=True)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
db_session = Session()
