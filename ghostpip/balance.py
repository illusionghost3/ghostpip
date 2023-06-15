import requests
import json

def get_account_balance(api_key, phone_number):
    url = 'https://ghost.toxinum.xyz/api/v1/balance'
    headers = {'Content-Type': 'application/json'}
    payload = {
        'apiKey': api_key,
        'number': phone_number
    }
    data = json.dumps(payload)

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.text
    else:
        return response.text