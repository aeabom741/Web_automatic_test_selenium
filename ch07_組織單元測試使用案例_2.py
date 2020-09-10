import unittest
from calculator2 import count

class test_start(unittest.TestCase):
    
    def setUp(self):
        print('Test start')
        
    def tearDown(self):
        print('Test end')
        
class add_test(test_start):
    
    def add_test1(self):
        i = count(5,6)
        self.assertEqual(i.add() , 11, msg = 'Wrong')
        
    def add_test2(self):
        i = count(1,5)
        self.assertEqual(i.add() , 6, msg = 'Wrong')
        
class sub_test(test_start):
    
    def sub_test1(self):
        j = count(7,2)
        self.assertEqual(j.sub() , 5, msg = 'Wrong')
    
    def sub_test2(self):
        j = count(8,2)
        self.assertEqual(j.sub(), 6, msg = 'Wrong')
        
if __name__ == "__main__":
   
    #建立測試集
    suite = unittest.TestSuite()
    suite.addTest(add_test('add_test1'))
    suite.addTest(sub_test('sub_test2'))
    suite.addTest(add_test('add_test2'))
    suite.addTest(sub_test('sub_test1'))
    #執行測試集
    
    runner = unittest.TextTestRunner()
    runner.run(suite)