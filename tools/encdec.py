import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generate_enckey(password:str, salt:bytes) -> bytes:
    password = password.encode('ascii')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

def encrypt_encfile(key:bytes, input) -> bytes:
    fernet = Fernet(key)
    return fernet.encrypt(input)

def decrypt_encfile(key:bytes, input) -> bytes:
    fernet = Fernet(key)
    return fernet.decrypt(input)