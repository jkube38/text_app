from twilio.rest import Client
from decouple import config

account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body='Whats up Jordan, you da man',
                    from_=config('TWILIO_PHONE_NUM'),
                    to='+17012126352'
                )

print(message)
