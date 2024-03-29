
# # input

# super_hero=input("What Is Your Super Hero Name :")
# print("Hello "+ super_hero)


# ---------------------------------------------------------------------



# # addition

# first=input("Enter First Number :")
# second =input("Enter Second Number :")
# sum=int(first) + int(second)

# print(sum)


# ---------------------------------------------------------------------




# # Some String Functions

# name="Vyankatesh Pandit"
# print(name.upper())

# print(name.find('k'))

# print(name.replace("Vyankatesh Pandit","Om Pandit"))




# ---------------------------------------------------------------------






# Even And Odd 


# num = int(input("Enter Number :"))

# if num%2==0:
#     print("Your Entered",num,"\nAnd Number Is Even :")
# else :
#     print("Your Entered",num,"\nAnd Number Is Odd :")    


# ---------------------------------------------------------------------




# greatest Number Out of 3 Numbers 

# a = int(input("Enter 1st Number :"))
# b = int(input("Enter 2nd Number :"))
# c = int(input("Enter 3rd Number :"))

# print("You Entered Numbers :",a , b , c)

# if a>b and a>c :
#     print(a,"is Greater Number")
# elif b>a and b>c :
#     print(b,"is Greater Number")
# else :
#      print(c,"is Greater Number")        



# ---------------------------------------------------------------------



# check Number Is Multiple of given Number or not (Means number is present in that given numbers mult.table)

# value = int(input("Enter Value You Want :"))
# num = int(input("Enter No You Want To Check :"))

# if num % value == 0 :
#     print(num,"is Multiple Of",value)
# else:
#     print(num,"is not Multiple of",value)    




# ---------------------------------------------------------------------

# Loops


# name = input("Enter Your Name :")

# value = int(input("Enter How Many Times You Want To Print Your Name :"))
# i=1
# while i <= value :
#     print(i,")",name)
#     i=i+1


# examples


# 1) 1 to 100
# num = int(input("Enter Number :"))
# i = 1
# while i <= num :
#     print(i)
#     i=i+1

# 2) 100 1 to 
# num = int(input("Enter Number :"))
# i = num
# while i >= 1 :
#     print(i)
#     i=i-1


# 3) multiplication Table

# num = int(input("Enter Number :"))
# i = 1
# while i <= 10 :
#       print(num,"X",i,"=",num*i) 
#       i = i + 1


# 4) Print elements of list 


# nums = [1,2,4,6,8,9,5]

# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx = idx +1


# 5) search number in tuple



# list = (1,2,3,4,5,6,7)
# i = 0
# x = int(input("Enter Number :"))
# while i < len(list):
#     if(list[i] == x):
#       print("Found At Index",i)
#       break
#     i = i+1



# break and continue keyword

# i = 0
# while i<=10:
#     if (i == 3):
#      i=i+1
#      continue
#     print(i)
#     i +=1 








# ---------------------------------------------------------------------

# list and tuple 


