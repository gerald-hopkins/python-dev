import secrets
import string

def generate_secret(length=32):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for i in range(length))

# Generate and print a secure random secret
secret = generate_secret()
print(secret)

# pRYyVG./(6WUW[P1T,+xBaIRU5%45P0.
