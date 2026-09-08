from flask_sqlalchemy import SQLAlchemy
import pyotp

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    otp_secret = db.Column(db.String(16), nullable=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.otp_secret = pyotp.random_base32()