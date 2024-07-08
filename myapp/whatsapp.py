from twilio.rest import Client

account_sid = 'AC673fa1b0c7ce1f44948b192030bcd7fa'
auth_token = 'ea6620dd67616129d083e68af66fdbac'
client = Client(account_sid, auth_token)

def send_whatsapp_message_to_group(group_id, message):
    from_whatsapp_number = 'whatsapp:+14159443885'  
    to_whatsapp_number = f'whatsapp:{group_id}'  

    message = client.messages.create(
        body=message,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )

    print(message.sid)

# Example usage
group_id = 'your_group_id'
message = 'Hello, this is a test message to the group!'
send_whatsapp_message_to_group(group_id, message)
