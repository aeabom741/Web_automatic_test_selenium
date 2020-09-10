from calculator import count

class TestCount:
    
    def test_add(self):
        try:
            j = count(2,3)
            add = j.add()
            assert (add == 6),'Result error'
        
        except AssertionError as msg:
            print(msg)
        
        else:
            print('Test Pass')

mytest = TestCount()
mytest.test_add()