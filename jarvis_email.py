# TODO

import smtplib  #simple mail transfer protocol

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "password"
subject = "Jarvis says Meow"
body = """Jarvis is here!

        This email was automatically sent by Jarvis
                                            Bye :P"""

# header
message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()   # transport layer security

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")