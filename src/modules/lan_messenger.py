from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import base64
import json

class LANMessenger:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.load_or_generate_keys()

    def load_or_generate_keys(self):
        if os.path.exists('private_key.pem') and os.path.exists('public_key.pem'):
            with open('private_key.pem', 'rb') as f:
                self.private_key = serialization.load_pem_private_key(
                    f.read(),
                    password=None,
                    backend=default_backend()
                )
            with open('public_key.pem', 'rb') as f:
                self.public_key = serialization.load_pem_public_key(
                    f.read(),
                    backend=default_backend()
                )
        else:
            self.generate_keys()

    def generate_keys(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

        with open('private_key.pem', 'wb') as f:
            f.write(self.private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=None
            ))

        with open('public_key.pem', 'wb') as f:
            f.write(self.public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))

    def encrypt_message(self, message):
        # Generate a random AES key
        aes_key = os.urandom(32)
        cipher = Cipher(algorithms.AES(aes_key), modes.CFB(os.urandom(16)), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_message = encryptor.update(message.encode()) + encryptor.finalize()

        # Encrypt the AES key with the public RSA key
        encrypted_aes_key = self.public_key.encrypt(
            aes_key,
            rsa.OAEP(
                mgf=rsa.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return base64.b64encode(encrypted_aes_key).decode(), base64.b64encode(encrypted_message).decode()

    def decrypt_message(self, encrypted_aes_key_b64, encrypted_message_b64):
        encrypted_aes_key = base64.b64decode(encrypted_aes_key_b64)
        encrypted_message = base64.b64decode(encrypted_message_b64)

        # Decrypt the AES key with the private RSA key
        aes_key = self.private_key.decrypt(
            encrypted_aes_key,
            rsa.OAEP(
                mgf=rsa.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        cipher = Cipher(algorithms.AES(aes_key), modes.CFB(encrypted_message[:16]), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_message = decryptor.update(encrypted_message[16:]) + decryptor.finalize()

        return decrypted_message.decode()