from calculator import count
import unittest

class test(unittest.TestCase):
    
    def setUp(self):
        print('Test start')
    
    def tearDown(self):
        print('Test end')
    
    def add_test(self):
        j = count(3,2)
        self.assertEqual(j.add(),5)
    
    def add_test2(self):
        j = count(11,5)
        self.assertEqual(j.add(),16)
    
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(test('add_test'))
    suite.addTest(test('add_test2'))
    
    runner = unittest.TextTestRunner()
    runner.run(suite)