
print('Calculate Weight to LB or in KG')
a=int(input('Weight: '))
b=input("(L)bs or (K)g:")
if b.lower()=="l":
    b=a*2.22
    print(b)
elif b.lower()=="k":
    b=a*0.45
    print(b)
print("")
print(" ")

