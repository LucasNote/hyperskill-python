import random


class SimpleBank:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        # Use a random int for seed
        random.seed(random.randint(1000000, 9999999))
        # Generate new account number
        new_account_number = random.randint(100000000, 999999999)
        # Create dictionary to hold account data
        acct = dict([
            ('account_number', str(new_account_number)),
            ('card_number', "400000" + str(new_account_number) + "9"),
            ('card_pin', str(random.randint(1000, 9999))),
            ('balance', float(0))
        ])
        # Append new account data to self.accounts - Use account.copy() with append(). Appending
        # account directly would produce a reference instead of a copy of the data
        self.accounts.append(acct.copy())
        # Print a summary
        print("Your card has been created", "Your card number:", f"{acct['card_number']}", "Your card PIN:",
              f"{acct['card_pin']}", sep="\n")

    def find_account(self, card_num):
        # The next function allows a default value to be specified if no account stored in
        # self.accounts matches the value of card_num. In this case, the default value is None.
        return next((acct for acct in self.accounts if acct['card_number'] == str(card_num)), None)

    def authenticate(self, card_num, pin):
        # Find account by card_num
        acct = self.find_account(card_num)
        if acct is not None:
            # Validate card_pin
            if str(pin) == str(acct['card_pin']):
                return True
        return False


def print_main_menu():
    print(10 * "-", "Main Menu", 10 * "-")
    print("1. Create an account", "2. Log into account", "0. Exit", sep="\n")
    print(31 * "-")


def print_account_menu():
    print(10 * "-", "Account Menu", 10 * "-")
    print("1. Balance", "2. Log out", "0. Exit", sep="\n")
    print(31 * "-")


def terminate():
    print("Bye!")
    quit(0)


main_menu_loop = True
account_menu_loop = False
bank = SimpleBank()

while main_menu_loop:
    # Print main menu and get selection
    print_main_menu()
    main_menu_choice = int(input())
    if main_menu_choice == 1:
        # Create new account
        bank.create_account()
    elif main_menu_choice == 2:
        # Log into account
        card_number = input("Enter your card number:")
        card_pin = input("Enter card PIN:")
        if bank.authenticate(card_number, card_pin):
            # Authentication successful
            print("You have successfully logged in!")
            account_menu_loop = True
            while account_menu_loop:
                # Find account
                account = bank.find_account(card_number)
                # Print account menu and get selection
                print_account_menu()
                account_menu_choice = int(input())
                if account_menu_choice == 1:
                    # Format balance float to two decimal places
                    print('Balance: ${:,.2f}'.format(account['balance']))
                elif account_menu_choice == 2:
                    # Clear existing data from account, return to main menu
                    account = None
                    account_menu_loop = False
                    print("You have successfully logged out!")
                elif account_menu_choice == 0:
                    # Terminate program
                    terminate()
                else:
                    print("Invalid selection!")
        else:
            # Authentication failed
            print("Wrong card number or PIN!")
    elif main_menu_choice == 0:
        # Terminate program
        terminate()
    else:
        print("Invalid selection!")
