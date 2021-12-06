from flask import Flask, session
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
db_session = Session()

@app.route("/")
def main():
    email_ = None
    if 'email' in session:
        print("loggined")
        email_ = "%s" % session['email']

    return render_template('/main/main.html', email=email_)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        q = db_session.query(Account).filter_by(email="%s" % form.email.data, password="%s"%form.password.data)
        if q.first():
            print("found", form['email'].data )
            session['email'] = "%s" % form['email'].data
        else:
            print("not found")
        return redirect('/')
    return render_template('/account/login.html', form=form)

@app.route("/logout")
def logout():
    session.pop('email', None)
    return render_template('/account/logout.html')

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    error_msg_ = None
    if form.validate_on_submit():
        q = db_session.query(Account).filter_by(email="%s" % form.email.data)
        if q.first():
            error_msg_ = "email already exists"
        else:
            account = Account(email="%s" % form.email.data, password="%s"%form.password.data)
            db_session.add(account)
            db_session.commit()
    return render_template('/account/signup.html', form=form, error_msg=error_msg_)
