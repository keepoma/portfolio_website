import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "nikita.karuzin@gmail.com"
password = "tptf zgwd pjdr anmj"

receiver = "nikita.karuzin@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: This is a test
Please do nos panic!
Thanks
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)


