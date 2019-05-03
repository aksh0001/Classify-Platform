from flask import Flask, render_template, url_for, flash, redirect, request

app = Flask(__name__)


@app.route("/layout")
def layout():
    return render_template('layout.html')


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


@app.route("/expert")
def expert():
    return render_template("expert.html")


@app.route("/dash")
def dashboard():
    return render_template("dash.html")


@app.route("/firm")
def firm():
    return render_template("firm.html")


@app.route("/nonhome")
def nonhome():
    return render_template("non_home_layout.html")


@app.route("/mail_communication")
def mail():
    return render_template("mail_communication.html")


@app.route("/video_communication")
def video():
    return render_template("video_communication.html")


@app.route("/cluster.html")
def cluster():
    return render_template("cluster.html")


@app.route("/claimant_list.html")
def cl_list():
    return render_template("claimant_list.html")


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
