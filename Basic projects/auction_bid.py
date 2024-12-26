print("Welcome to auction bid!")
auction_data = {}
starter = True
while starter:
    user_name = input("What is your name? :").lower()
    user_bid = int(input("What's your bid? Rs :"))
    auction_data[user_name]=user_bid
    print("\n"*100) 
    user_decision = input("Are there any one bidders? Type 'yes' or 'no' :").lower()

    if user_decision == 'no':
        starter = False
        n = auction_data[user_name]
        winner = ""
        for i in auction_data.values():
            if i > n:
                n = i
        for usr , bid in auction_data.items():
            if bid == n:
                winner = usr      
        print(f"The winner is {winner} bidded RS : {n}")