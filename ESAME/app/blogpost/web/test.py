import requests,time,json,rstr,re,base64;
from datetime import datetime;

flags = requests.get(f"http://10.1.3.10:5000/flagIds").json()
print(flags['help']['service']['values'])
