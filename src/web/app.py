from flask import Flask
from flask import render_template, redirect

from account.login_form import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = '12345643214321432143214321'

@app.route("/")
def main():
    return render_template('/main/main.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('/account/login.html', form=form)

@app.route("/logout")
def logout():
    return render_template('/account/logout.html')

@app.route("/signup")
def signup():
    return render_template('/account/signup.html')
