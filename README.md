# Encryption Decryption Module
This project provides a module for encrypting and decrypting text using the AES-256-CBC algorithm in both Node.js and Python. The module ensures secure data handling by utilizing a robust encryption standard, making it suitable for various applications requiring data confidentiality.

# Features
- AES-256-CBC Encryption: Utilizes the AES-256-CBC algorithm for strong encryption.
- Random IV Generation: Generates a unique initialization vector (IV) for each encryption to enhance security.
- Environment Variable for Key Management: Uses an environment variable for storing the encryption key, ensuring that the key is not hard-coded in the source code.
- Cross-Platform Support: Provides implementation in both Node.js and Python, allowing for flexibility in different development environments.
- Data Padding: Implements proper padding techniques to ensure compatibility with the block cipher requirements of AES.
# Prerequisites
## Node.js
- Node.js (version 10 or later).
## Python
- Python 3.6 or later.
- cryptography library (installable via pip).
# Usage
Set the ENCRYPTION_KEY environment variable with your 32-byte encryption key.
Use the provided functions to encrypt and decrypt text in your Node.js or Python applications.
