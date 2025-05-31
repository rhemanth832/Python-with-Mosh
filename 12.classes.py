#Class is blueprint of object
#Constructor: It is called when object is created
class point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")
p1=point()
p1.draw()
p1.move()
p1.x=10
p1.y=20
print(p1.x)
#Each class is instance of object
p2=point()
#print(p2.x) , atrribute error
p2.x=25
print(p2.x)

#Constructor with parameter
class points:
    def __init__(self, x, y): #Here x,y are parameters
        self.x = x #Here x is attribute
        self.y = y
        def draw(self): #Here draw() is method
            print("draw")
        def move(self):
            print("move")
points1=points(10,20)
print(points1.x)
points1.x=15
print(points1.x)

# new Exercise
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'{self.name} is talking')
P1=Person('Rahul')
P1.talk()
print(P1.name)