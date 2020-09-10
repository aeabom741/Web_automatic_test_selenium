import unittest

class test(unittest.TestCase):
    
    def setUp(self):
        print('Test start')
    
    def tearDown(self):
        print('Test end')
        
    def test_case(self):
        a = 'Hello'
        b = 'Hello world'
        self.assertIn(a,b,msg = 'a is not in b')

if __name__ == '__main__':
    unittest.main()