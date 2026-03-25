import random 

name1 = input("enter player1:")
name2 = input("enter player2:")

d1=random.randint(1,25)
d2=random.randint(1,25)

s1 = 25
s2 = 25

print('__player1 has to guess__')

while(True):
    g1 = int(input("enter your guess:"))
    if(d1==g1):
        break
    elif(d1>g1):
        print("your guess is low")
    else:
        print("your guess is high")
        s1 = s1 - 1

print('__player2 has to guess__')

while(True):
    g2 = int(input("enter your guess:"))
    if(d2==g2):
        break
    elif(d2>g2):
        print("your guess is low")
    else:
        print("your guess is high")
        s2 = s2 - 1
        
if(s1>s2):
    print("player1 won!!!")
else:
    print("player2 won!!!")