# Luhn algorithm
"""
The main purpose of the check digit is to verify that the card number is valid.
Say you're buying something online, and you type in your credit card number incorrectly
by accidentally swapping two digits, which is one of the most common errors.
When the website looks at the number you've entered and applies the Luhn algorithm to the first 15 digits,
the result won't match the 16th digit on the number you entered. The computer knows the number is invalid,
and it knows the number will be rejected if it tries to submit the purchase for approval.

Another purpose of the check digit is to catch clumsy attempts to create fake credit card numbers.

Luhn Algorithm in action
The Luhn algorithm is used to validate a credit card number or other identifying numbers,
such as Social Security. The Luhn algorithm, also called the Luhn formula or modulus 10,
checks the sum of the digits in the card number and checks whether the sum matches the expected result
or if there is an error in the number sequence. After working through the algorithm,
if the total modulus 10 equals zero, then the number is valid according to the Luhn method.

If the received number is divisible by 10 with the remainder equal to zero, then this number is valid;
otherwise, the card number is not valid. When registering in your banking system,
you should generate cards with numbers that are checked by the Luhn algorithm.
You know how to check the card for validity.

First, we need to generate an Account Identifier, which is unique to each card.
Then we need to assign the Account Identifier to our BIN (Bank Identification Number).
As a result, we get a 15-digit number 400000844943340, so we only have to generate the last digit,
which is a checksum.

To find the checksum, it is necessary to find the control number for 400000844943340 by the Luhn algorithm.
It equals 57 (from the example above). The final check digit of the generated map is 57+X,
where X is checksum. In order for the final card number to pass the validity check,
the check number must be a multiple of 10, so 57+X must be a multiple of 10.
The only number that satisfies this condition is 3.

Therefore, the checksum is 3. So the total number of the generated card is 4000008449433403.
The received card is checked by the Luhn algorithm.

You need to change the credit card generation algorithm so that they pass the Luhn algorithm.
"""

from random import randint


class Bank:
    def __init__(self):
        self.accounts = {}

    def operate(self):
        while True:
            self.display_bank_menu()
            customer_selection = input()
            while customer_selection not in ["0", "1", "2"]:
                print()
                self.display_bank_menu()
                customer_selection = input()
            if customer_selection != "0":
                if customer_selection == "1":
                    self.create_an_account()
                else:
                    credentials = self.validate_credentials()
                    if len(credentials) == 0:
                        print("\nWrong card number or PIN!\n")
                    else:
                        if self.access_account(credentials) == "Exit":
                            break
            else:
                break
        print("\nBye!")

    @staticmethod
    def display_bank_menu():
        menu = "1. Create an account\n" + \
               "2. Log into account\n" + \
               "0. Exit"
        print(menu)

    def create_an_account(self):
        account_ids = self.get_account_ids()
        account_id = randint(0, 999999999)
        while account_id in account_ids:
            account_id = randint(0, 999999999)
        new_account = CreditCard(account_id)
        self.add_account(new_account)
        print("\nYour card has been created")
        print("Your card number:")
        print(new_account.get_card_number())
        print("Your card PIN:")
        print(new_account.get_pin())
        print()

    def get_account_ids(self):
        account_ids = list(self.accounts.keys())
        return account_ids

    def add_account(self, credit_card_account):
        self.accounts[credit_card_account.get_account_id()] = \
            credit_card_account

    def get_account(self, account_id):
        account = self.accounts.get(account_id)
        return account

    def validate_credentials(self):
        card_number = input("\nEnter your card number:\n")
        card_pin = input("Enter your PIN:\n")
        credentials = []
        account_id = card_number[6:15]
        account_ids = self.get_account_ids()
        if account_id in account_ids:
            if card_pin == self.get_account(account_id).get_pin():
                credentials = [account_id, card_pin]
        return credentials

    def access_account(self, credentials):
        print("\nYou have successfully logged in!\n")
        account_id = credentials[0]
        card = self.get_account(account_id)
        while True:
            card.display_card_menu()
            customer_selection = input()
            while customer_selection not in ["0", "1", "2"]:
                print()
                card.display_card_menu()
                customer_selection = input()
            if customer_selection != "0":
                if customer_selection == "1":
                    print("\nBalance: {}\n".format(card.get_balance()))
                else:
                    print("\nYou have successfully logged out!\n")
                    log_out_or_exit = "Log out"
                    break
            else:
                log_out_or_exit = "Exit"
                break
        return log_out_or_exit


class CreditCard:
    iin = 400000

    def __init__(self, account_id):
        self.account_id = account_id
        self.check_sum = randint(1, 9)
        self.pin = randint(0, 9999)
        self.balance = 0

    @staticmethod
    def display_card_menu():
        menu = "1. Balance\n" + \
               "2. Log out\n" + \
               "0. Exit"
        print(menu)

    def get_account_id(self):
        account_id = "{}".format(self.account_id).zfill(9)
        return account_id

    def get_card_number(self):
        card_number = "{}".format(CreditCard.iin) \
                      + "{}".format(self.account_id).zfill(9) \
                      + "{}".format(self.check_sum)
        return card_number

    def get_pin(self):
        pin = "{}".format(self.pin).zfill(4)
        return pin

    def get_balance(self):
        balance = self.balance
        return balance


bank = Bank()
bank.operate()

