import smtplib

EMAIL = "***REMOVED***"
PASSWORD = "***REMOVED***"

class EmailClient:
    def __init__(self):
        smtp_connection = smtplib.SMTP(host="***REMOVED***", port=***REMOVED***)
        smtp_connection.starttls()
        smtp_connection.login(user=EMAIL, password=PASSWORD)
        self.smtp_connection = smtp_connection





