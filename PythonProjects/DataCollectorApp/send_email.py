import smtplib
from email.mime.text import MIMEText


def send_email(email, height, average_height, count):
    from_email = "chavezfrancisco308@gmail.com"
    from_password = "beqt10cq"
    to_email = email

    subject = "Height data"
    message = "Hey there, your height is <strong>%s</strong>. Average height of all is %s and that is calculated out " \
              "<strong> %s</strong> of people." % (height, average_height, count)

    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["from"] = from_email

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
