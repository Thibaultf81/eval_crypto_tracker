import unittest
from api import get_crypto

class TestApp(unittest.TestCase):
    
    def get_crypto(self):
        self.assertEqual(get_crypto(), dict)
        
if __name__ == '__main__':
    unittest.main()