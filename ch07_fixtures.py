import unittest

def setUpModule():
    print('Test Module start')
    
def tearDownModule():
    print('Test Module end')
    
class test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('Test class start')
        
    @classmethod
    def tearDownClass(cls):
        print('Test class end')
        
    def setUp(self):
        print('Test start')
        
    def tearDown(self):
        print('Test end')
        
    def test_case1(self):
        print('Test1')
        
    def test_case2(self):
        print('Test2')
        
if __name__ == '__main__':
    unittest.main()