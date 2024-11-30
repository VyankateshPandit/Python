import random
from random_words import words
from hangman_art import stages

# Genrating random word from module >
random_word = random.choice(words)

#  Some important variables >
blanks = ""
lifes = 6 
game_over = True
correct_letters = []
for i in random_word:
    blanks +="_"

print(f"Welcome to HangMan game!\n word:{blanks}")

# Main logic of game >
while game_over:
    display=""
    user_guess = input("Guess word :").lower()
    # Tracking user lifes >
    if user_guess not in random_word:
      lifes-=1 
      print(f"Oops '{user_guess}' is wrong guess! {stages[lifes]}")
      print(f"Lifes remaining > {lifes}/6")
    
     # Checking user input is matching to random word or not > 
    else:  
        for i in random_word:
            if i == user_guess:
                display += i
                correct_letters.append(i)
            elif i in correct_letters:
                display+=i
            else:
                display += "_"
    # Displaying all outputs to user > 
    print(display)            
    if display == random_word:
        print("You won!\n Thank you for playing")
        game_over = False
    elif lifes == 0:
        print(f"Word was {random_word}")
        print("You lose!\nBetter luck next time!")
        game_over = False                
   
    