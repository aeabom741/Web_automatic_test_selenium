import unittest
from prime import is_prime

class test(unittest.TestCase):
    
    def setUp(self):
        print("Test start")
    
    def tearDown(self):
        print('Test end')
        
    def test_case(self):
        self.assertTrue(is_prime(7),msg = 'None')
        
if __name__ == '__main__':
    unittest.main()
    