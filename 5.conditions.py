guess=9 #Guess the Number
i=0
while i<3:
    no = int(input('Guess the Number: '))
    i+=1
    if no == guess:
        print('Correct Guess!')
print('')

# CAR Game WHILE LOOP
started =False
while True:
    a = input(">").lower()

    if a == 'start':
        if started:
            print('Car is already started...')
        else:
            started = True
            print('Car started... Ready to Go')
    elif a == 'stop':
        if not started:
            print('Car is already stopped...')
        else:
            started = False
            print('Car stopped...')
    elif a == 'help':
        print('START - to start the car')
        print('STOP - to stop the car')
        print('QUIT - to quit the game')
    elif a == 'quit':
        break
    else:
        print("I don't understand that...")
#GAP
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
