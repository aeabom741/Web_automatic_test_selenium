import testadd
import testsub
import unittest

suite = unittest.TestSuite()

suite.addTest(testadd.Add_case('add_case2'))
suite.addTest(testsub.Sub_case('sub_case1'))
suite.addTest(testadd.Add_case('add_case1'))
suite.addTest(testsub.Sub_case('sub_case2'))

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)