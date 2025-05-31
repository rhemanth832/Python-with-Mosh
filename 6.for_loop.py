price=[10,20,30]
tot=0
for i in price:
    tot=tot+i
print(tot)

#nested for loops (Example of coordinates of x,y)
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")

print()
print('')

#F structure
f=[5,2,5,2,2]
for i in f:
    for j in range(i):
        print("*",end='')
    print()