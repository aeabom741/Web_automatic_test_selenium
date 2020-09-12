import unittest

class MyTest(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    @unittest.skip("直接跳過測試")
    def test_skip(self):
        print('test aaa')
        
    @unittest.skipIf(3 > 2,"當條件為True時跳過測試")
    def test_skip_if(self):
        print('test bbb')
        
    @unittest.skipUnless(3 > 2,'當條件為True時執行測試')
    def test_skip_unless(self):
        print('test ccc')
    
    @unittest.expectedFailure
    def test_expectedFailure(self):
        self.assertEqual(2,3)

if __name__ == '__main__':
    unittest.main()
            