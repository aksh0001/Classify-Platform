from flask import Flask, render_template, url_for, flash, redirect, request

app = Flask(__name__)
app.config['FREEZER_RELATIVE_URLS'] = True

@app.route("/layout")
def layout():
    return render_template('layout.html')


@app.route("/")
@app.route("/home.html")
def home():
    return render_template('home.html')


@app.route("/signup.html")
def signup():
    return render_template('signup_form.html')


@app.route("/portal.html")
def portal():
    return render_template("portal.html")


@app.route("/expert.html")
def expert():
    return render_template("expert.html")


@app.route("/dash.html")
def dashboard():
    return render_template("dash.html")


@app.route("/firm.html")
def firm():
    return render_template("firm.html")


@app.route("/nonhome")
def nonhome():
    return render_template("non_home_layout.html")

from flask_frozen import Freezer

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
