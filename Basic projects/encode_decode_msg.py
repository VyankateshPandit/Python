leters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode_decode(encode_or_decode,user_msg,user_shift_amt):
    final_msg = ""    
    for i in user_msg:
        if encode_or_decode =='decode':
            if i not in leters:
                final_msg+=i
            if i in leters:    
                final_msg+=leters[leters.index(i)-user_shift_amt]
        else:
            if i not in leters:
                final_msg+=i
            if i in leters:
                final_msg+=leters[leters.index(i)+user_shift_amt]
    print(final_msg)

restarter = True
while restarter:
    encode_or_decode = input("Enter 'encode' for encryption and 'decode' for decryption :").lower()
    user_msg = input("Enter your msg :").lower()
    user_shift_amt = int(input("Enter shift amount :"))
    encode_decode(encode_or_decode,user_msg,user_shift_amt)

    want_to_go_again = input("Type 'yes' to go again or type 'no' to exit :").lower()
    if want_to_go_again =="no":
        restarter = False
        print("GoodBye thanks for using this service")