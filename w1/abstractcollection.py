class AbstractCollection(object):
    
    def __init__(slef, SourceCollection = None):
        self.size = 0
        if sourceCollection:
            for item in SourceCollection:
                self.add(item)
        
        def isEmmpty(self):
            return len(self) == 0
        
        def __len__(self):
            return self.size
        
        def __str__(self):
            return "["+",".join(map(str,self)) +"]"
        
        def __add__(self, other):
            result = type(self)(self)
            for item in other:
                result.add(item)
                return result
        
        def __eq__(self, other):
            if self is other:
                return True
            if type(self) != type(other)or len(self) !=len(other):
                return False
            otherIter = iter(other)
            for item in self:
                if item != next(otherIter):
                    return False
            return True