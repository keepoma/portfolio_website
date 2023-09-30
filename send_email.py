import smtplib, ssl


def send_email(message_local):
    host = "smtp.gmail.com"
    port = 465
    username = "nikita.karuzin@gmail.com"
    password = "bnmu pkmj beki kzfu"
    receiver = "nikita.karuzin@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message_local)


