from cryptography.fernet import Fernet 
import hashlib 
import base64
KEY_FILE="secret.key"

def  password_to_key(password:str):
    key=hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key) 

def encrypt_files(data:bytes,password:str):
    key=password_to_key(password)
    cipher=Fernet(key)
    return cipher.encrypt(data)

def decrypt_files(data:bytes,password:str):
    key=password_to_key(password)
    cipher=Fernet(key)
    return cipher.decrypt(data)
