import unittest

class test(unittest.TestCase):
    
    def setUp(self):
        number = int(input('Enter a number:'))
        self.number = number
    
    def tearDown(self):
        pass
    
    def test_case(self):
        self.assertEqual(self.number ,10 , msg = 'Not enter 10!')
        
if __name__ == '__main__':
    unittest.main()