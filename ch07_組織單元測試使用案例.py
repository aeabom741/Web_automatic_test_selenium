import unittest
from calculator2 import count

class add_test(unittest.TestCase):
    
    def setUp(self):
        print('test start')
    
    def tearDown(self):
        print('test end')
        
    def add_test(self):
        j = count(5,6)
        self.assertEqual(j.add() ,11 ,msg = 'Wrong!')       
    def add_test2(self):
        j = count(7,0)
        self.assertEqual(j.add(), 7, msg = 'Wrong!')
        

class sub_test(unittest.TestCase):
    
    def setUp(self):
        print('test start')
        
    def tearDown(self):
        print('test end')
        
    def sub_test(self):
        i = count(7,3)
        self.assertEqual(i.sub() ,4 , msg = "Wrong")
        
    def sub_test2(self):
        i = count(11,5)
        self.assertEqual(i.sub() , 6 , msg = "Wrong")
    
    
if __name__ == '__main__':
    suite = unittest.TestSuite()
    
    suite.addTest(add_test('add_test'))
    suite.addTest(sub_test('sub_test2'))
    suite.addTest(sub_test('sub_test'))
    suite.addTest(add_test('add_test2'))
    
    runner = unittest.TextTestRunner()
    runner.run(suite)