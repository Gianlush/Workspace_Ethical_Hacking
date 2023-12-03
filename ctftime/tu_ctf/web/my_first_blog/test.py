import requests,string

cookie = {"session":"baff0551-b33d-4c4f-b551-bf2172d32cc1"}


data = {"title":"prova", "content":string.printable}

r = requests.post("https://my-first-blog.tuctf.com/create", cookies=cookie)
print(r)
