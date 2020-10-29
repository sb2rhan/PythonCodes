'''
    pip install requests

    Documentation: https://core.telegram.org/bots/api
    Bot: https://api.telegram.org/bot{API}
'''
import requests
import os
from dotenv import load_dotenv
load_dotenv()


API_TOKEN = os.getenv('API_TOKEN')
URL = 'https://api.telegram.org/bot'

#  Parameters of bot
# response = requests.get(f'{URL}{API_TOKEN}/getMe')
# print(response.json())

#  Getting messages from users
response = requests.get(f'{ URL }{ API_TOKEN }/getUpdates')
result = dict(response.json())
print(result)

chat_id = result['result'][0]['message']['chat']['id']
# print(chat_id)


# Sending a message to user
message_text = 'Hello, how are you doing?'
pattern_message = { 'chat_id': chat_id, 'text': message_text }
response = requests.post(f'{ URL }{ API_TOKEN }/sendMessage', data=pattern_message)
print(response.status_code)

# Sending a location to user
# coordinate = { 'chat_id': chat_id, 'latitude': 43.238949, 'longitude': 76.889709 }
# response = requests.post(f'{URL}{API_TOKEN}/sendLocation', data=coordinate)
# print(response.status_code)
