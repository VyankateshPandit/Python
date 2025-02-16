resources = {
    'water':700,
    'milk':1000,
    'coffee':300,
    'money':0,
}
def report(resources):
    print("Water -",resources['water'],"ml\nMilk -",resources['milk'],"ml\nCoffee -",resources['coffee'],"g\nMoney -",resources['money'])

def latte(resources):   
     if resources["water"] >= 200 and resources["milk"]>=100 and resources["coffee"]>=50:
            money = int(input("Insert money 299rs: "))
            if money == 299: 
                print(f"Here is your {user}. Enjoy!")
                resources["water"] = resources["water"] - 200
                resources["milk"] = resources["milk"] - 100
                resources["coffee"] = resources["coffee"] - 50
                resources['money'] = resources['money'] + 299
            elif money > 299:
                money = money - 299
                print(f"Here is change of {money}rs")
                print(f"Here is your {user}. Enjoy!")
                resources["water"] = resources["water"] - 200
                resources["milk"] = resources["milk"] - 100
                resources["coffee"] = resources["coffee"] - 50
                resources['money'] = resources['money'] + 299
            else:
                print(f"Sorry that's not enough money, {money} Refunded!")         
     else:
        print("Dont have resources")

def espresso(resources):
     if resources["water"] >= 300 and resources["milk"]>=250 and resources["coffee"]>=75:
            money = int(input("Insert money 350rs: "))
            if money == 350: 
                print(f"Here is your {user}. Enjoy!")
                resources["water"] = resources["water"] - 300
                resources["milk"] = resources["milk"] - 250
                resources["coffee"] = resources["coffee"] - 75
                resources['money'] = resources['money'] + 350 
            elif money > 350:
                money = money - 350
                print(f"Here is change of {money}rs")
                print(f"Here is your {user}. Enjoy!")
                resources["water"] = resources["water"] - 300
                resources["milk"] = resources["milk"] - 250
                resources["coffee"] = resources["coffee"] - 75
                resources['money'] = resources['money'] + 350 
            else:
                print(f"Sorry that's not enough money, {money} Refunded!")         
     else:
        print("Dont have resources")

def cappuccino(resources):
     if resources["water"] >= 350 and resources["milk"]>=300 and resources["coffee"]>=90:
            money = int(input("Insert money 599rs: "))
            if money == 599: 
                print(f"Here is your {user}. Enjoy!")
                resources["water"] = resources["water"] - 350
                resources["milk"] = resources["milk"] - 100
                resources["coffee"] = resources["coffee"] - 90
                resources['money'] = resources['money'] + 599 
            elif money > 599:
                money = money - 599
                print(f"Here is change of {money}rs")
                print(f"Here is your {user}. Enjoy!")
                resources["water"] = resources["water"] - 350
                resources["milk"] = resources["milk"] - 300
                resources["coffee"] = resources["coffee"] - 90
                resources['money'] = resources['money'] + 599 
            else:
                print(f"Sorry that's not enough money, {money} Refunded!")         
     else:
        print("Dont have resources")
conti = True
while conti:
    user = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user =="off":
        conti = False
        print("Thank you! visit again...")
    elif user == "report": 
        report(resources=resources)
    elif user == "espresso":
       espresso(resources=resources)    
    elif user == "latte":
       latte(resources=resources) 
    elif user == "cappuccino":
       cappuccino(resources=resources)    
