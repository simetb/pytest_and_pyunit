class Foo:
    foo = 17
    
    def __init__(self) -> None:
        pass
    
    def bar(self):
        return 543
    
    def baz(self):
        return "blah"
    
    def __add__(self, val2): 
        return (self.foo + val2.foo)