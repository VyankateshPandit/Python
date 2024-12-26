import random
random_num = random.randint(0,100)
print(random_num)
EASY_ATTEMPT = 10
HARD_ATTEMPT = 5
print("Welcome to guess the number game!")

def check_guess(user_guess,random_no,attempt_left):
     if user_guess > random_no:
          print("Too high!")
          return attempt_left - 1
     elif user_guess < random_no:
          print("Too low!")
          return attempt_left - 1
     else:
          print(f"You won right guess! {user_guess}") 
                   

def set_difficulties():
    level = input("Type 'easy' or type 'hard'\nChoose level > ").lower()
    if level == 'easy':
         return EASY_ATTEMPT
    else:
         return HARD_ATTEMPT
    
def game():
    attempts = set_difficulties()
    guess = 0
    while guess!=random_num:
        print(f"You have {attempts} left...")
        guess = int(input("Make a guess :"))
        attempts = check_guess(guess,random_num,attempts)

        if attempts == 0:
            print("No attempts left! you lose...")
            return
game()