import random


class SimpleBank:
    def __init__(self):
        self.accounts = []
        self.bank_identifier = 400000

    @staticmethod
    def run_luhn(number):
        # Create a list of digits in number
        digits = [int(d) for d in str(number)]
        # Calculate the sum of even indexed digits
        even_indexed_sum = sum(digits[1::2])
        # Multiply odd indexed values by 2
        odd_indexed_digits = [int(2 * digit) for digit in digits[0::2]]
        # Subtract 9 from odd indexed values if value is greater than 9
        odd_indexed_digits = [digit - 9 if digit > 9 else digit for digit in odd_indexed_digits]
        # Sum odd indexed values
        odd_indexed_sum = sum(odd_indexed_digits)
        # Return the combined sums
        return odd_indexed_sum + even_indexed_sum

    def gen_checksum(self, number):
        # Run Luhn algorithm on supplied number
        luhn = self.run_luhn(number)
        # Use modulo to check whether the number returned by run_luhn() is divisible by 10 with no remainders.
        # If a remainder is found, then subtract that value from 10 to get the checksum. If the returned number
        # is divisible by 10 with no remainder, then the checksum is 0.
        return 10 - luhn % 10 if luhn % 10 != 0 else 0

    def verify_luhn(self, number):
        # Uses modulo to check whether the supplied number is divisible by 10. If so, it is valid.
        return self.run_luhn(number) % 10 == 0

    def generate_card(self, account_number):
        # Overly paranoid error checking
        fails = 0
        card_candidate = None
        card_candidate_checksum = None
        while True:
            # Generate a new card number candidate
            card_candidate = int(str(self.bank_identifier) + str(account_number))
            # Generate a checksum
            card_candidate_checksum = self.gen_checksum(card_candidate)
            # Validate generated card number
            if self.verify_luhn(str(card_candidate) + str(card_candidate_checksum)):
                # Passed Luhn check
                break
            else:
                # Failed luhn check, try generating a new card number
                fails += 1
                if fails >= 3:
                    # Failed 3 times, abort process
                    print("Something has gone horribly wrong... cannot create account!")
                    break

        # Return new card number with checksum appended
        return str(card_candidate) + str(card_candidate_checksum)

    def create_account(self):
        # Use a random int for seed
        random.seed(random.randint(1000000, 9999999))
        # Generate account number
        new_account_number = random.randint(100000000, 999999999)
        # Generate card number
        new_card_number = self.generate_card(new_account_number)
        # Create dictionary to hold account data
        acct = dict([
            ('account_number', str(new_account_number)),
            ('card_number', str(new_card_number)),
            ('card_pin', str(random.randint(1000, 9999))),
            ('balance', float(0))
        ])
        # Append new account data to self.accounts - Use account.copy() with append(). Appending
        # account directly would produce a reference instead of a copy of the data
        self.accounts.append(acct.copy())

        # Output summary
        print("Your account has been created", "Your card number:", acct['card_number'],
              "Your PIN:", acct['card_pin'], "Current Balance:", "${:,.2f}".format(acct['balance']), sep="\n")

    def find_account(self, card_num):
        # The next function allows a default value to be specified if no account stored in
        # self.accounts matches the value of card_num. In this case, the default value is None.
        return next((acct for acct in self.accounts if acct['card_number'] == str(card_num)), None)

    def authenticate(self, card_num, pin):
        # Validate card_num
        if not self.verify_luhn(card_num):
            print("The supplied card number was invalid!")
            return False
        # Find account by card_num
        acct = self.find_account(card_num)
        if acct is not None:
            # Validate card_pin
            if str(pin) == str(acct['card_pin']):
                return True
        return False


def terminate():
    print("Bye!")
    quit(0)


main_menu_loop = True
account_menu_loop = False

bank = SimpleBank()


while main_menu_loop:
    # Print main menu and get selection
    print(10 * "-", "Main Menu", 10 * "-")
    print("1. Create an account", "2. Log into account", "0. Exit", sep="\n")
    print(31 * "-")
    main_menu_choice = input()
    if main_menu_choice == '1':
        # Create new account
        bank.create_account()
    elif main_menu_choice == '2':
        # Log into account
        card_number = input("Enter your card number:")
        card_pin = input("Enter card PIN:")
        if bank.authenticate(card_number, card_pin):
            # Authentication successful
            print("You have successfully logged in!")
            while account_menu_loop:
                # Find account
                account = bank.find_account(card_number)
                # Print account menu and get selection
                print(10 * "-", "Account Menu", 10 * "-")
                print("1. Balance", "2. Log out", "0. Exit", sep="\n")
                print(31 * "-")
                account_menu_choice = input()
                if account_menu_choice == '1':
                    # Format balance float to two decimal places
                    print('Balance: ${:,.2f}'.format(account['balance']))
                elif account_menu_choice == '2':
                    # Clear existing data from account, return to main menu
                    account = None
                    print("You have successfully logged out!")
                    account_menu_loop = False
                elif account_menu_choice == '0':
                    # Terminate program
                    terminate()
                else:
                    print("Invalid selection!")
        else:
            # Authentication failed
            print("Wrong card number or PIN!")
    elif main_menu_choice == '0':
        # Terminate program
        terminate()
    else:
        print("Invalid selection!")
