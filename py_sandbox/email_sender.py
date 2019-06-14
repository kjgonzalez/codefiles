import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "kjg.notify@gmail.com"
receiver_email = "kjg9190@hotmail.com"
password = input("Type your password and press enter: ")
message = """\
Subject: test

hope this works.

"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
