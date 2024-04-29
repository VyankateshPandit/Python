
a=input("Enter First Number :")
operator=input("Enter Operator (+,-,x,/,%):")
b=input("Enter Second Number :")



if operator=='+':
    print(int(a)+int(b))

elif operator=='-':
    print(int(a)-int(b))

elif operator=='x':
    print(int(a)*int(b))

elif operator=='/':
    print(int(a)/int(b))

elif operator=='%':
    print(int(a)%int(b))

else:print("Invalid Operator")


