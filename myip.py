import requests
import json

response = requests.get('https://ipinfo.io')
data = json.loads(response.text)
print data['data']['quotes']['USD']['price']