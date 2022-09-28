from Operations import Registration, login

def MainMenu():
    choice = input("enter 1 for Registration , enter 2 for Login ")
    if choice == "1":
        print("Registration")
        Registration()

    elif choice == "2":
        print("Login")
        login()

    else:
        print("invalid input")
        return MainMenu()
MainMenu()
