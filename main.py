import json
import smtplib
import ssl

#data = {}
with open("email.json") as file:
    data = json.load(file)
    port = 465
    email = data["address"]
    password = data["password"]
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        receiver = input("receiver: ")
        subject = input("subject: ")
        subject = "Subject: " + subject
        #message_body = input("message: ")
        print("message:\n")
        lines = []
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break

        message_body = '\n'.join(lines)
        message = subject + "\n\n" + message_body
        server.login(email, password)
        server.sendmail(email, receiver, message)
        print("Message sent!")