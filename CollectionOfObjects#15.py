class Person:
    def __init__(self,name):
        self.name = name
        print(self.name + " Created")


name = input("Enter a name: ")     
pOne = Person(name)       