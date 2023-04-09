import Account_Manager

def main_menu():
    
    print("=" * 10 + "Welcome to Cinema Ticket Booking System" + "=" * 10)
    print()
    
    menu = True
    
    while menu:
        print("\n======Select the option=====")
        print("1. Login Account")
        print("2. Register Account")
        print("3. Exit")
        print()
        choice = int(input("Enter the choice : "))

        if choice == 1:
            result = Account_Manager.login()

            if result:
                print("\nSuccessfully login")
            else:
                print("\nAccount not found, username or password is wrong")
            menu = False

        elif choice == 2:
            result = Account_Manager.registerAccount()

            if result:
                print("\nAccount created successfully")
            else:
                print("\nUncessful attempt")

        elif choice == 3:
            menu = False
    
    Account_Manager.closeConnection()

if __name__ == "__main__":
    main_menu()
        
        




