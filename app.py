from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session
from models import db, User
from utils import hash_password, check_password
import pyotp, qrcode, io, base64

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config["SESSION_TYPE"] = "filesystem"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
Session(app)
db.init_app(app)

# Create tables once at startup
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Check if username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already taken. Please choose another.")
            return redirect(url_for("register"))

        if len(password) < 8:
            flash("Password must be at least 8 characters.")
            return redirect(url_for("register"))

        hashed = hash_password(password)
        user = User(username=username, password=hashed)
        db.session.add(user)
        db.session.commit()

        # Generate QR for 2FA setup
        otp_uri = pyotp.totp.TOTP(user.otp_secret).provisioning_uri(
            name=username, issuer_name="SecureLoginApp"
        )
        qr = qrcode.make(otp_uri)
        buf = io.BytesIO()
        qr.save(buf, format="PNG")
        qr_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")

        return render_template("show_qr.html", qr_b64=qr_b64)
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()
        if user and check_password(password, user.password):
            if user.otp_secret:
                session["pending_user"] = user.id
                return redirect(url_for("verify_2fa"))
            session["user_id"] = user.id
            return redirect(url_for("dashboard"))
        flash("Invalid credentials.")
    return render_template("login.html")

@app.route("/verify-2fa", methods=["GET", "POST"])
def verify_2fa():
    if request.method == "POST":
        code = request.form["code"]
        user = User.query.get(session["pending_user"])
        totp = pyotp.TOTP(user.otp_secret)
        if totp.verify(code):
            session["user_id"] = user.id
            session.pop("pending_user", None)
            return redirect(url_for("dashboard"))
        flash("Invalid 2FA code.")
    return render_template("verify_2fa.html")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))
    user = User.query.get(session["user_id"])
    return render_template("dashboard.html", username=user.username)

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.")
    return redirect(url_for("login"))

# Below is the code to run the Flask app. This should be placed at the end of your webapp.py file. 
# it will start the Flask development server when you run the script directly. 
# If you want run service on a public IP, you can change the host to ' app.run(host="0.0.0.0", port=5000, debug=True)
# If you want run service on localhost only, you can change the host to ' app.run(host="127.0.0.1", port=5000, debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)