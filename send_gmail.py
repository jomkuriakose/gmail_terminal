import smtplib

def iitm_gmail_send_msg(receiver_email, name, pwd):

    sender_email = "smtiitm@gmail.com"
    password = "qhiogbjtwdzgcima"

    body = f"Hi {name}\n\nHere are your login details\n\nUsername: {receiver_email}\nPassword: {pwd}\n\nBest regards,\nTTS Team\nIIT Madras"

    message = f"Subject: Indic TTS Database -- Access Details\n\n{body}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print ('Email sent!')
        return True
    except Exception as e:
        print ('Something went wrong...', e)
        return False
    finally:
        server.quit()

if __name__ == "__main__":
    receiver_email = 'gupta.ishika08@gmail.com'
    name = 'Ishika Gupta'
    pwd = 'asdfgh'
    if iitm_gmail_send_msg(receiver_email, name, pwd):
        print('Success')
    else:
        print('Error')