import smtplib

EMAIL = "jjtesttestjj@gmail.com"
PASSWORD = "bnpw qbye cjsz kzzi"

class EmailClient:
    def __init__(self):
        smtp_connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
        smtp_connection.starttls()
        smtp_connection.login(user=EMAIL, password=PASSWORD)
        self.smtp_connection = smtp_connection





