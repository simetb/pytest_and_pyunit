#PyUnit
import unittest
from foobarbaz import Foo

class SimpletTestCase(unittest.TestCase):
    
    def setUp(self):
        """Call before every test case"""
        print("Call before every test case")
        self.foo = Foo()

    def tearDown(self):
        """Call after every test case"""
        print("Call after every test case")
    
    def testA(self):
        assert self.foo.bar() == 543, "bar() not calculating values correctly" 
        
    def testB(self):
        assert self.foo + self.foo, "cant add Foo instances"
        
    def testC(self):
        assert self.foo.baz() == "blah", "baz() not returning blah correctly"
        
if __name__ == '__main__':
    unittest.main() # run all test