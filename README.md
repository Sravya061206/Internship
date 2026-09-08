# Secure Login System (Flask + SQLite + 2FA)

A secure login web application built with **Flask**, featuring:

- User registration and login with **bcrypt password hashing**
- **SQL injection protection** via SQLAlchemy ORM
- **Session management** with login/logout
- Optional **Two-Factor Authentication (2FA)** using TOTP (Google Authenticator, Authy)
- Modern **Bootstrap 5 UI**

---

##  Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Sravya061206/Internship.git
   cd Internship

2. Create a virtual environment
   ```bash
    python3 -m venv venv
    source venv/bin/activate   # Linux/macOS
    venv\Scripts\activate      # Windows

3. Install dependencies:
   ```bash
    pip install -r requirements.txt

4. Run the Flask app:
   ```bash
    python app.py
