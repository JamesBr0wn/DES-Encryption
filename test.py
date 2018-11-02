import unittest
import algorithm


class TestAlgorithm(unittest.TestCase):
    def setUp(self):
        self.key = 'A secret key'
        self.data = 'This is a simple test of encryption and decryption algorithm.'
        self.wrapper = algorithm.DESWrapper(self.key.encode())

    def test_key(self):
        self.assertFalse(self.key == '')

    def test_data(self):
        self.assertFalse(self.data == '')

    def test_algorithm(self):
        initial_data = self.data.encode()
        encrypt_data = self.wrapper.encrypt(initial_data)
        decrypt_data = self.wrapper.decrypt(encrypt_data)
        self.assertEqual(initial_data.decode(), decrypt_data.decode()[:len(initial_data.decode())])


if __name__ == '__main__':
    unittest.main()
