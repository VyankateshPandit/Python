import data
import random
score = 0
print("Welcome to Higher / Lower -")

def answer(guess):
     """Takes guess as input and check answer and return that answer"""
     if guess == 'a':
          global A_fol
          global B_fol
          A_fol = A_choice['followers']
          B_fol = B_choice['followers']
          if A_fol > B_fol:
               A_fol = A_choice
               return A_fol 
     else:  
          A_fol = A_choice['followers']
          B_fol = B_choice['followers']
          if B_fol > A_fol:
               B_fol = B_choice
               return B_fol 
def choices():
     """Print data"""
     print(f"Name - {A_choice['name']} , {A_choice['description']} from {A_choice['country']}")
     print("------------VS------------")
     print(f"Name - {B_choice['name']} , {B_choice['description']} from {B_choice['country']}")

A_choice = random.choice(data.data)
B_choice = random.choice(data.data)
if A_choice == B_choice:
     B_choice = random.choice(data.data)
gameover = True
while gameover:
     choices()
     guess = input("Who has more followers? Type 'A' or 'B' :").lower()
     New_choice = answer(guess) 
     A_choice = New_choice
     B_choice = random.choice(data.data)
     if A_choice == B_choice:
        B_choice = random.choice(data.data)
     print("\n"*5)
     if New_choice:
          score+=1
          print(f"Thats correct, Current score {score}")
          
     else:
          print(f"Sorry that's wrong, Final score {score}")
          gameover = False