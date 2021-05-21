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