from twilio.rest import Client
import config

client = Client(config.account_sid,config.auth_token)
call = client.messages.create(
    to="+965 69699625",
    from_="+13602306644",
    body= "This is my first message"
)
