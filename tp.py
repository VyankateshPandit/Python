# num = input("Enter Number: ")
# sum = 0

# for i in num:
#     sum = sum + int(i)
    
# print(sum)


# my_tup=(1,2)
# car=('a','b','c')
# new=my_tup*2
# print(2 in new)

# print(len(new))

# print(new[3])

# print(new.count(2))

# print(car.index('c'))

# d=new+car
# print(d)






# my_set={3,4,5,6,8}

# print(min(my_set))
# print(max(my_set))
# print(len(my_set))


# t=(12,3,5,33,2)

# print(max(t),min(t))



# def count_vol(inp):
#     vo="aeiouAEIOU"

#     count=0
#     for char in inp:
#         if char in vo:
#          count+=1
#     return count 


# inp=input("Enter :")


# numofvo=count_vol(inp)
# print(numofvo)



def sum_of_natural_numbers(n):
      sum = 0
      for i in range(1, n+1):
         sum += i
      return sum
# Input number from user
n = int(input("Enter a number: "))
# Calculate and print the sum of natural numbers up to n
result = sum_of_natural_numbers(n)
print("Sum of natural numbers from 1 to", n, "is:", result)
