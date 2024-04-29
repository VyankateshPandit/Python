import os


if __name__ == '__main__':

    print("Hello Im Linux")
    while True :
        x = input("Enter :")
        if x == "q":
            break
        command = f"spd-say {x}"
        os.system(command)