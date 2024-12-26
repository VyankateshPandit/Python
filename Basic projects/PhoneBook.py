print("Welcome to PhoneBook!")

# dictionary
phonebook = {
    'om':9922553872,
    'vyankatesh':7397963819,
    'tanmay':9922667733,
}
print("- View contact list : 1)\n- Add new contact : 2)\n- Update contact: 3)\n- Delete contact : 4)\n- Search contact : 5)")
while True:
    userInput = int(input("\nChoose option otherwise press CRL+C:"))

# To display all contacts
    if userInput == 1:
        print("Here is your contact list >\n",phonebook)

# To add new contact
    elif userInput == 2:
        name = input("Enter name :").lower()
        number = int(input("Enter contact :"))
        if number in phonebook.values():
            print("This contact is already exist!")
        else:    
           phonebook.update({name:number})
           print("Contact has been added!")  

# To update contact
    elif userInput == 3:
          option = input("Do you want to update name? Yes/ No :").lower()
          if option == "yes":
              name = input("Enter name you wanna update :")
              if name in phonebook:  
                 Newname = input("Enter new name :")              
                 phonebook[Newname] = phonebook.pop(name)
                 print(f"Name {name} has been updated to {Newname}")
              else:
                  print("This contact does not exist!")
              option = input("Do you want to update contact number? Yes/No :").lower()
              if option == "yes":
                  number = input("Enter name you wanna update :")
                  if number in phonebook:
                    Newnumber = input("Enter new number :")
                    phonebook[number] = Newnumber
                    print("Contact has been updated!")
                  else:
                     print("This contact does not exist!")   
              else:
                    print("Contact has been updated!")
          else:
              option = input("Do you want to update contact number? Yes/No :").lower()
              if option == "yes":
                  number = input("Enter name you wanna update :")
                  if number in phonebook:
                    Newnumber = input("Enter new number :")
                    phonebook[number] = Newnumber
                    print("Contact has been updated!")
                  else:
                     print("This contact does not exist!")   

# To delete contact
    elif userInput == 4:
        name = input("Enter name :").lower()
        if name in phonebook:
            phonebook.pop(name)
            print(f"Contact {name} has been deleted!")    
        else:
            print("This contact does not exist in phonebook!")  

# To search for contact   
    elif userInput == 5:
        name = input("Enter name :")
        if name in phonebook:
            print("Contact no :",phonebook.get(name))
        else:
            print("This contact does not exist in phonebook!")            