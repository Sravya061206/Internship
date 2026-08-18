Password Strength Analyzer
A Flask‑based web application with a strict password policy. It analyses user‑entered passwords in real time and enforces strong security rules.

Features
	• Length and complexity scoring (uppercase, lowercase, digits, special characters).
	• Immediate Weak classification for:
		○ Short passwords (<8 chars).
		○ Repeated characters (case‑insensitive).
		○ Continuous sequences (forward or reverse).
		○ Common dictionary words (password, admin, etc.).
		○ Reused passwords (already saved in DB).
	• SQLite database to track old passwords.
	• Strong password suggestions.
	• Real‑time feedback in the UI.


Setup
	• pip install flask or pip install -r requirements.txt
  • python app.py
