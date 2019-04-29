from flask import Flask, render_template, url_for, flash, redirect, request

app = Flask(__name__)
app.config['FREEZER_RELATIVE_URLS'] = True

@app.route("/layout.html")
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


@app.route("/nonhome.html")
def nonhome():
    return render_template("non_home_layout.html")

@app.route("/mail_communication.html")
def mail():
    return render_template("mail_communication.html")


@app.route("/video_communication.html")
def video():
    return render_template("video_communication.html")

from flask_frozen import Freezer

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
