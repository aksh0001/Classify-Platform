from flask import Flask, render_template, url_for, flash, redirect, request

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/signup")
def signup():
    return render_template('signup_form.html')


@app.route("/portal")
def portal():
    return render_template("portal.html")

<<<<<<< HEAD
@app.route("/expert")
def expert():
    return render_template("expert.html")

@app.route("/dash")
def dashboard():
    return render_template("dash.html")

@app.route("/firm")
def firm():
    return render_template("firm.html")
>>>>>>> 27d832ebb4e0a8669e4c4038b0927ab7de3af6f4

if __name__ == '__main__':
    app.run(debug=True)
