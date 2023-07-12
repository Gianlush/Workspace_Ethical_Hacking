import requests
import rstr
import time

while True:
    try:
        s = requests.Session()

        data = {'username': 'admin', 'password':'admin'}
        s.post("http://localhost:8080/api/users/login", json=data)

        product = {'name':'nome','price':1000,'secret':rstr.xeger('^[A-Z0-9]{31}=$')}
        s.post("http://localhost:8080/api/products/create", json=product)
    except:
        time.sleep(3)
    finally:
        time.sleep(3)