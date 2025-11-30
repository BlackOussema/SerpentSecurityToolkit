import unittest
from src.modules.lan_messenger import Messenger

class TestLanMessenger(unittest.TestCase):

    def setUp(self):
        self.messenger = Messenger()

    def test_key_generation(self):
        public_key, private_key = self.messenger.generate_keys()
        self.assertIsNotNone(public_key)
        self.assertIsNotNone(private_key)

    def test_encryption_decryption(self):
        message = "Hello, secure world!"
        encrypted_message = self.messenger.encrypt_message(message)
        decrypted_message = self.messenger.decrypt_message(encrypted_message)
        self.assertEqual(message, decrypted_message)

    def test_send_receive_message(self):
        message = "Test message"
        recipient = "recipient_address"
        response = self.messenger.send_message(recipient, message)
        self.assertTrue(response)

        received_message = self.messenger.receive_message()
        self.assertEqual(message, received_message)

if __name__ == '__main__':
    unittest.main()