from flask import Flask, render_template, url_for, flash, redirect, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/signup")
def signup():
    return render_template('signup_form.html')

if __name__ == '__main__':
    app.run(debug=True)
