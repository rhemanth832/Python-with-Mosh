import math
a=2.9
print(round(a))

a=-2.9
print(abs(a)) # abs removes negative val

print(math.ceil(2.5))
print(math.ceil(2.2))
print(math.ceil(2.8)) # ceil prints high next int value

print(math.floor(2.9)) # floor prints  small previous int value


a=int(input('Enter no: '))
b=int(input('Enter no: '))
print(math.factorial(a))
print(math.gcd(a,b))
print(math.trunc(a))
print(math.lcm(a,b))
