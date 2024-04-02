import random
name=input("Enter Name To Start The Game :")
print("Hello",name)
target = random.randint(1,100)
while True:
     num=int(input("Enter Number :"))

     if(num == target):
          print("Correct Guess",target,"",name)
          
          break
     elif(num < target):
          print("Guess is Too Small , Please Guess Bigger")
     else:
          print("Guess is Too big , Please Guess Smaller")
print("(----GAME OVER----)")

