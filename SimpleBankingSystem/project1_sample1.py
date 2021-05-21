import random


def generate_card_number(iin):
    account_number = str(random.randrange(999_999_999)).ljust(9, '0')
    check_digit = str(random.randint(0, 9))
    return iin + account_number + check_digit


def generate_pin():
    return str(random.randrange(9_999)).ljust(4, '0')


def print_options(options):
    for option in options:
        print(option)


class BankingSystem:
    IIN = '400000'

    def __init__(self):
        self.accounts = {}
        self.current_account = None

    def create_account(self):
        card_number = generate_card_number(BankingSystem.IIN)
        pin = generate_pin()
        self.accounts[card_number] = Account(card_number, pin)
        print('Your card has been created')
        print('Your card number:')
        print(card_number)
        print('Your card PIN:')
        print(pin)

    def login(self):
        card_number = input('Enter your card number:')
        pin = input('Enter your PIN:')
        current_account = self.accounts.get(card_number)
        if current_account is None or current_account.pin_incorrect(pin):
            print('Wrong card number or PIN!')
            return
        self.current_account = current_account
        self.account_menu()

    @staticmethod
    def exit():
        print('Bye!')
        exit(0)

    @staticmethod
    def invalid_option(options):
        print('Invalid option! Choose:')
        print_options(options)

    def balance(self):
        print(f'Balance: {self.current_account.balance}')

    def logout(self):
        self.current_account = None
        print('You have successfully logged out!')

    def account_menu(self):
        options = ['1. Balance', '2. Log out', '0. Exit']
        print('You have successfully logged in!')
        print('')
        print_options(options)

        option = ''
        while option != '0':
            option = input().strip()
            if option == '1':
                self.balance()
            elif option == '2':
                self.logout()
            elif option == '0':
                self.exit()
            else:
                self.invalid_option(options)

    def main_menu(self):
        options = ['1. Create an account', '2. Log into account', '0. Exit']
        print_options(options)

        option = ''
        while option != '0':
            option = input().strip()
            if option == '1':
                self.create_account()
            elif option == '2':
                self.login()
            elif option == '0':
                self.exit()
            else:
                self.invalid_option(options)


class Account:

    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        self.balance = 0

    def pin_incorrect(self, pin):
        return self.pin != pin

    def __repr__(self):
        return f'Card: {self.card_number}, PIN: {self.pin}'


banking_system = BankingSystem()
banking_system.main_menu()