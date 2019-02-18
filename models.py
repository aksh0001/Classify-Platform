from datetime import datetime
from flask_login import UserMixin
from run import db

def load_user(user_id):
    return User.query.get(int(user_id))

class Lawfirm(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    #email = db.Column(db.String(120), unique=True, nullable=False)
    #image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    #password = db.Column(db.String(60), nullable=False)
    class_action = db.relationship('Lawsuit', backref='defendant')

    def __repr__(self):
        return f"User('{self.username}', '{self.class_action}')"


class Lawsuit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    #content = db.Column(db.Text, nullable=False)
    defendant_id = db.Column(db.Integer, db.ForeignKey('lawfirm.id'), nullable=False)
    #plantiff = db.Column(db.String(100), nullable=False)
    #date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.title}', '{self.defendant_id}')"
