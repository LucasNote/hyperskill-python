# Write your code here
import random
from typing import List

IIN = '400000'
new_account = None


def update():
    print([str(account) for account in Bank.all_accounts])


class Bank:
    all_accounts = []

    def __init__(self):
        # self.card_pre_luhn = IIN + f'{random.randint(000000000, 999999999):09}'
        # self.card_number = IIN + f'{random.randint(000000000, 999999999):09}'
        self.card_number = self.luhn(IIN + f'{random.randint(000000000, 999999999):09}')
        self.pin = f'{random.randint(0000, 9999):04}'
        self.balance = 0
        Bank.all_accounts.append(self)
        print("\nYour card has been created\n"
              "Your card number:\n"
              + self.card_number +
              "\nYour card PIN:\n"
              + self.pin)
        # print(self.card_number)
        # print(self.pin)

    def __str__(self):
        return self.card_number

    @staticmethod
    def luhn(pre_luhn):
        luhn_list = list(map(int, str(pre_luhn)))
        double_odd_index: list[int] = [n * 2 if i % 2 else n for i, n in enumerate(luhn_list, 1)]
        sub_nine_double_digit: list[int] = [n - 9 if n > 9 else n for n in double_odd_index]
        checksum = sum(sub_nine_double_digit)
        luhn = 10 - (checksum % 10) if checksum % 10 != 0 else 0
        return pre_luhn + str(luhn)


def login():
    return input("\n1. Create an account\n"
                 "2. Log into account\n"
                 "0. Exit\n")


def menu_loop():
    return input("\n1. Balance\n"
                 "2. Log out\n"
                 "0. Exit\n")


def menu(account: Bank):
    while True:
        menu_select = menu_loop()
        if menu_select == '1':
            print(f'\nBalance: {account.balance}')
        elif menu_select == '2':
            main()
        elif menu_select == '0':
            bye()


def password(account: Bank):
    card_input = input('\nEnter your card number:\n')
    pin_input = input('Enter your PIN:\n')
    if card_input == account.card_number and pin_input == account.pin:
        print('\nYou have successfully logged in!')
        menu(account)
    else:
        print('\nWrong card number or PIN!')


def main():
    global new_account
    while True:
        selection = login()
        if selection == '0':
            bye()
        elif selection == '1':
            new_account = Bank()
        elif selection == '2' and new_account is not None:
            password(new_account)


def bye():
    print("Bye!")
    exit("bye")


def test():
    update()
    account_1 = Bank()
    update()
    account_2 = Bank()
    update()
    account_3 = Bank()
    update()


if __name__ == "__main__":
    main()
    # test()