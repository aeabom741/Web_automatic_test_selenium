from calculator import count
import unittest

class Test(unittest.TestCase):
  
    def setUp(self):
        print('test start')
        
    def add_test(self):
        j = count(2,3)
        self.assertEqual(j.add(), 5)
        
    def tearDown(self):
        print('test end')    
    
if __name__ == '__main__':
    unittest.main()