def menu():
    print("Welcome to the game please select an option:\n c: connect to a server\n s: start server\n q: quit")
    choise = input()
    if choise == "c":
        print("Your choise is: " + choise)
    elif choise == "s":
        print("Your choise is: " + choise)
    elif choise == "q":
        print("Your choise is: " + choise)
    else:
        print("wrong input try again")
        menu()


def main():
    menu()

if __name__ == "__main__":
        main()