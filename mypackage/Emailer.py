import ssl
import smtplib

class Emailer:
    port = 465

    def __init__(self, address, password):
        self.address = address
        self.password = password
        self.domain = address.split("@")[1]
        self.context = ssl.create_default_context()
        self.server = smtplib.SMTP_SSL("smtp." + self.domain, self.port, context=self.context)
        self.server.login(address, password)

    def send(self, receiver, subject, message):
        self.server.sendmail(self.address, receiver, "Subject: " + subject + "\n\n" + message)
