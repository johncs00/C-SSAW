# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os


# Your Account Sid and Auth Token from twilio.com/console
# Environment variables should be set to these values for api security.
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="Testing 1.2.3..",
                    from_='+12054488869',
                    to='+14087979462'
                )

print(message.sid)
