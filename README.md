# Secure Login System (Flask + SQLite + 2FA)

A secure login web application built with **Flask**, featuring:

- User registration and login with **bcrypt password hashing**
- **SQL injection protection** via SQLAlchemy ORM
- **Session management** with login/logout
- Optional **Two-Factor Authentication (2FA)** using TOTP (Google Authenticator, Authy)
- Modern **Bootstrap 5 UI**

---

## Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/yourusername/secure-login.git
cd secure-login

---
2. Setup Environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac

3. Install Dependency
```bash
pip install -r requirements.txt

4. Run the application
```bash
python app.py
