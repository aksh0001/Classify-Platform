from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Johnny1/Documents/GitHub/flask101/classify.db'
db = SQLAlchemy(app)
from models import Lawfirm, Lawsuit


if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
