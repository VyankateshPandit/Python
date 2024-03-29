



a=input("Do you Want to Make Your License : Yes / No ")

if a =='yes':
       age=int(input("Enter Your Age :"))
       if age < 18:
           print("You Are Under Age Now , Plz Apply After 18 :")

       else:
           print("You Can Apply For License :")
           name = input("Enter Your Name :")
           city = input("Enter City Name :")

           print("Your Details :")
           print(name)
           print(age)
           print(city)
else:
       print("Visit Again You Want License :")
