class array(object):
    def __init__(self, capacity, fillValue = None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fillValue)
    
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __getItem__(self, index):
        return self.items[index]
    
    def __setItem__(self, index, newItem):
        self.items[index] = newItem
    
    def __iter__(self):
        return iter(self.items)
