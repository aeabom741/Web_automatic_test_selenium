from calculator2 import count     
import unittest                   
                                  
class Sub_case(unittest.TestCase):
    
    def setUp(self):            
        print('Test start')
    def tearDown(self):
        print('Test end')
    def sub_case1(self):
        i = count(5,6)
        self.assertEqual(i.sub(), -1 ,msg =  'None')
    def sub_case2(self):
        i = count(7,3)
        self.assertEqual(i.sub(), 4 ,msg = "None" )

if __name__ == '__main__':
    unittest.main()