def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

data = {
    "+":add,
    "-":subtract,
    "x":multiply,
    "/":divide,
}

def main(a,b,c):
    if c =='+':
        return data["+"](a,b)
    elif c =='-':
        return data["-"](a,b)
    elif c =='x':
        return data["x"](a,b)
    elif c =='/':
        return data["/"](a,b)
    else:
        print("Invalid inputs! Try again")

def calculator():
    print("Welcome!")
    run = True
    usr_f= float(input("Enter first number :"))
    while run:
        
        usr_op= input("Choose an operation :\n '+' \n '-' \n 'x' \n '/' \n >")
        usr_s= float(input("Enter second number :"))
        
        result= main(a=usr_f,b=usr_s,c=usr_op)
        print(f"Result > {usr_f} {usr_op} {usr_s} = {result}")
        want_to_con=input(f"If you want to continue with {result} type 'yes' or type 'no' \n:")
        
        if want_to_con == 'yes':
                usr_f = result
                
        
        else:
            run = False
            n = "\n"
            print(n*20)
            calculator()
calculator()            
       