from twilio.rest import Client
import os

ACCOUNT_SID = str(os.environ.get("TWILIO_ACCOUNT_SID"))
AUTH_TOKEN = str(os.environ.get("TWILIO_AUTH_TOKEN"))
FROM_NUMBER = str(os.environ.get("FROM_NUMBER"))
TO_NUMBER = str(os.environ.get("TO_NUMBER"))


class NotificationManager:

    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, message):
        self.client.messages.create(
            body=message,
            from_=FROM_NUMBER,
            to=TO_NUMBER
        )
        print(message.sid)
