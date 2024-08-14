class atm1:

    def __init__(self, pin=None, balance=0):
        self.__pin = pin
        self.__balance = balance
        self.__menu()

    def __get_pin(self):
        pin = input("Enter a 4 digit pin: ")

        if len(pin) != 4 or not pin.isdigit():
            print("Invalid pin, make sure your pin is 4 digits")
            print(" ")
            return self.__get_pin()

        else:
            self.__pin = pin

    def __verify_pin(self):
        pin = input("Reenter your 4 digit pin: ")

        if pin == self.__pin:
            print("Pin verified and/or set")
            print(" ")

        else:
            print(" ")
            print("Incorrect pin, try again")
            print(" ")
            self.__verify_pin()
            
    def __generate_pin(self):
        if self.__pin is None:
            self.__get_pin()
            self.__verify_pin()

        else:
            print("Your pin is already set")
            return self.__menu()

    def __change_pin(self):
        if self.__pin is not None:

            old_pin = input("Enter your current pin: ")

            if self.__pin == old_pin:

                self.__get_pin()
                self.__verify_pin()
                
          
                    
            else:
                print("The pin is incorrect")
                return self.__change_pin()
        else:
            self.__get_pin()
            self.__verify_pin()

    def __check_balance(self):
        if self.__pin is None:
            self.__generate_pin()
        else:
            self.__verify_pin()
            print("Your balance is: " + str(self.__balance))
            print(" ")

    def __withdraw(self):
        if self.__pin is None:
            self.__generate_pin()
        else:
            self.__verify_pin()
            withdraw = int(input("How much would you like to withdraw? "))

            if withdraw % 100 != 0 or withdraw > self.__balance:
                print("Must be a multiple of 100 and less than your balance of " + 
                      str(self.__balance))
                print(" ")
                print(" ")
                return self.__menu() 
            else:
                self.__balance -= withdraw
                print("Withdrawal successfull")
                print(" ")

    def __deposit(self):
        if self.__pin is None:
            self.__generate_pin()
        else:
            self.__verify_pin()
            deposit = int(input("How much would you like to deposit? "))

            if deposit % 100 != 0 or deposit < 0:
                print("Must be a multiple of 100 and greater than 0 ")
                print(" ")
                return self.__menu() 
            else:
                self.__balance += deposit
                print("Deposit successfull")
                print(" ")
        
    def __menu(self):
        running = True

        while running:

            print("ATM Menu")
            print("1. Generate Pin")
            print("2. Change Pin")
            print("3. Check Balance")
            print("4. Withdraw")
            print("5. Deposit")
            print("6. Exit")
            choice = int(input("Enter your choice: "))
            print(" ")

            if choice == 1:
                self.__generate_pin()
            elif choice == 2:
                self.__change_pin()
            elif choice == 3:
                self.__check_balance()
            elif choice == 6:
                print("Exiting...")
                running = False
                
            elif choice == 4:
                self.__withdraw()
            elif choice == 5:
                self.__deposit()

            else:
                print("Invalid choice. Please try again.")
                self.__menu()
