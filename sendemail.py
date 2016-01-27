import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_message():
    msg = MIMEMultipart('alternative')
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login('email', 'password')

    email_to_and_from = 'email'
    msg['Subject'] = 'subject'
    msg['From'] = 'email'
    body = 'This is the message'

    content = MIMEText(body, 'plain')
    msg.attach(content)
    filename = "test.txt"
    f = file(filename)
    attachment = MIMEText(f.read())
    attachment.add_header('Content-Disposition', 'attachment', filename=filename)            
    msg.attach(attachment)

    server.sendmail(email_to_and_from, email_to_and_from, msg.as_string())

send_message()