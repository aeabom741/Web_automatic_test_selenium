from calculator2 import count     
import unittest                   
                                  
class Add_case(unittest.TestCase):
         
    def setUp(self):
        print('Test start')
         
    def tearDown(self):
        print('Test end')
         
    def add_case1(self):
        i = count(3,3)
        self.assertEqual(i.add() ,6 ,msg = 'None')
         
    def add_case2(self):
        i = count(5,9)
        self.assertEqual(i.add() ,14 ,msg = "None")
         
if __name__ == "__main__":
    unittest.main()