import hashlib

password = "adminpass"
hashed_password = hashlib.sha1(password.encode()).hexdigest()
print(hashed_password)

password = 'aa3OFF9m'
hashed_password = hashlib.sha1(password.encode()).hexdigest()
print(hashed_password)
