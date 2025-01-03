import requests

req = requests.get('https://api.opendota.com/api/schema')

response = req.json()

