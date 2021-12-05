from flask import Flask
from flask import render_template, redirect

from sqlalchemy import create_engine

from account.login_form import LoginForm
from account.signup_form import SignUpForm
from database.login_db import Account

app = Flask(__name__)
app.config["SECRET_KEY"] = '12345643214321432143214321'

engine = create_engine('sqlite:///account.db', echo=True)
Account.__table__.create(bind=engine, checkfirst=True)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

@app.route("/")
def main():
    return render_template('/main/main.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        q = session.query(Account).filter_by(email="%s" % form.email, password="%s"%form.password)
        if q.first():
            print("found")
        else:
            print("not found")
        return redirect('/')
    return render_template('/account/login.html', form=form)

@app.route("/logout")
def logout():
    return render_template('/account/logout.html')

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print(form.email, form.password)
        account = Account(email="%s" % form.email, password="%s"%form.password)
        session.add(account)
        session.commit()
        return redirect('/')
    return render_template('/account/signup.html', form=form)
