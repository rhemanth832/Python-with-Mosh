import random
for i in range(0,3):
    print(random.random())

for i in range(0,3):
    print(random.randint(1,10))

a =['Kohli','Rohit','Rahul','MS.Dhoni']
print(random.choice(a))

b =[1,2,3,4,5,6]
print(random.sample(b,2))