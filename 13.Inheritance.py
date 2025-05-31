class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")
class Cat(Mammal):
    pass
M1=Mammal()
M1.walk()
D1=Dog()
D1.walk()
D1.bark()

