import os
from dotenv import load_dotenv
from twilio.rest import Client



load_dotenv()

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
FROM_PHONE = os.environ.get('FROM_PHONE')
TO_PHONE = os.environ.get('TO_PHONE')

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

""""
message = client.messages.create(
    body = 'This is from a python api call',
    from_ = FROM_PHONE,
    to = TO_PHONE
)

print(message.sid)
"""

for msg in client.messages.list():
    print(msg.body)
