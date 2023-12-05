from animal import Animal

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        
    def getName(self):
        print( self.name)

dog = Dog("Rocky")
dog.makesSound()
dog.eat()
dog.getName()