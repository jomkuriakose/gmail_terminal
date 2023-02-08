import smtplib

sender_email = "smtiitm@gmail.com"
receiver_email = "gupta.ishika08@gmail.com"
password = "qhiogbjtwdzgcima"

message = """\
Subject: Hi there

This message is sent from Python."""

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print ('Email sent!')
except Exception as e:
    print ('Something went wrong...', e)
finally:
    server.quit()
