import smtplib
import sys

def iitm_gmail_send_msg(receiver_email, name, pwd):

    sender_email = ""
    password = ""

    body = "Hi "+name+"\n\nHere are your login details\n\nUsername: "+receiver_email+"\nPassword: "+pwd+"\n\nBest regards,\nTTS Team\nIIT Madras"

    message = "Subject: Indic TTS Database -- Access Details\n\n"+body

    try:
        server = smtplib.SMTP("smtp.gmail.com", 465)
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
    if len(sys.argv) == 4:
        receiver_email = sys.argv[1]
        name = sys.argv[2]
        pwd = sys.argv[3]
    else:
        print('Command: python3 send_gmail.py <receiver_email> <name> <password>')
        sys.exit()
    if iitm_gmail_send_msg(receiver_email, name, pwd):
        print('Done!!')
    else:
        print('Error!!')
