import os
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random

ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY')  # Must be 256 bits (32 characters)
IV_LENGTH = 16  # For AES, this is always 16 bytes

def pad(s):
    # Pads the text to be a multiple of 16 bytes
    return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

def unpad(s):
    # Removes padding from the decrypted text
    return s[:-ord(s[len(s)-1:])]

def encrypt(text):
    iv = Random.new().read(IV_LENGTH)
    cipher = AES.new(ENCRYPTION_KEY.encode('utf-8'), AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(text).encode('utf-8'))
    return base64.b64encode(iv + encrypted).decode('utf-8')

def decrypt(encrypted_text):
    encrypted_text = base64.b64decode(encrypted_text)
    iv = encrypted_text[:IV_LENGTH]
    encrypted_text = encrypted_text[IV_LENGTH:]
    cipher = AES.new(ENCRYPTION_KEY.encode('utf-8'), AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted_text))
    return decrypted.decode('utf-8')

# Example usage
if __name__ == "__main__":
    ENCRYPTION_KEY = 'thisisaverysecretkey123456789012'  # Example key for testing
    text_to_encrypt = "Hello, World!"
    encrypted_text = encrypt(text_to_encrypt)
    print(f"Encrypted: {encrypted_text}")
    decrypted_text = decrypt(encrypted_text)
    print(f"Decrypted: {decrypted_text}")
