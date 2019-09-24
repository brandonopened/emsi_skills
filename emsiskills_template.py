import requests

headers = {'Content-Type': 'application/x-www-form-urlencoded'}
url = "https://auth.emsicloud.com/connect/token"

payload = "client_id=<CLIENTID>&client_secret=<SECRET>&grant_type=client_credentials&scope=emsi_open"
response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
