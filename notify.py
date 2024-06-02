import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    from_email = "your_email@example.com"
    password = "your_password"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    server = smtplib.SMTP_SSL('smtp.example.com', 465)
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

def notify_users(available_spirits):
    for email, spirits in available_spirits.items():
        subject = "Available Spirits Notification"
        body = "The following spirits are available:\n" + "\n".join(spirits)
        send_email(subject, body, email)

# Example usage
if __name__ == "__main__":
    available_spirits = {'example@example.com': ['Spirit 1', 'Spirit 2']}
    notify_users(available_spirits)
