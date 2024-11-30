import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols=['@','#','$','&','*']
numbers=[1,2,3,4,5,6,7,8,9,0]
password=[]
print("Welcome to password generator!")
in_let=int(input("Enter no of letters :"))
in_sym=int(input("Enter no of symbols :"))
in_num=int(input("Enter no of Numbers :"))
for i in range(0,in_let):
    password+=random.choice(letters)
for i in range(0,in_sym):
    password+=random.choice(symbols)
for i in range(0,in_num):
    password+=random.choice(str(numbers))
random.shuffle(password)
final_password =""
for i in password:
    final_password+=i
print("Your password is generated >",final_password)    