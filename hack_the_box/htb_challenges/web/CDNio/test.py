import requests
base_url = "http://localhost:9000"
uri = "/\\localhost:9001"

r = requests.get(f"{base_url}/{uri}")