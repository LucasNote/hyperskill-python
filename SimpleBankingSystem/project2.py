# Work on project. Stage 1/4: Card anatomy

"""
The very first digit is the Major Industry Identifier (MII), which tells you
what sort of institution issued the card.

1 and 2 are issued by airlines
3 is issued by travel and entertainment
4 and 5 are issued by banking and financial institutions
6 is issued by merchandising and banking
7 is issued by petroleum companies
8 is issued by telecommunications companies
9 is issued by national assignment
In our banking system, credit cards should begin with 4.

The first six digits are the Issuer Identification Number (IIN).
These can be used to look up where the card originated from. If you have access to a list
that provides detail on who owns each IIN, you can see who issued the card just by reading the card number.

Here are a few you might recognize:

Visa: 4*****
American Express (AMEX): 34**** or 37****
Mastercard: 51**** to 55****
In our banking system, the IIN must be 400000.

The seventh digit to the second-to-last digit is the customer account number.
Most companies use just 9 digits for the account numbers, but it’s possible to use up to 12.
This means that using the current algorithm for credit cards, the world can issue about a trillion cards
before it has to change the system.

We often see 16-digit credit card numbers today, but it’s possible to issue a card with up to 19 digits
using the current system. In the future, we may see longer numbers becoming more common.

In our banking system, the customer account number can be any, but it should be unique.
And the whole card number should be 16-digit length.

The very last digit of a credit card is the check digit or checksum. It is used to validate
the credit card number using the Luhn algorithm, which we will explain in the next stage of this project.
For now, the checksum can be any digit you like.
"""

# Objectives
"""
Objectives
You should allow customers to create a new account in our banking system.

Once the program starts, you should print the menu:

1. Create an account
2. Log into account
0. Exit
If the customer chooses ‘Create an account’, you should generate a new card number which 
satisfies all the conditions described above. Then you should generate a PIN code that 
belongs to the generated card number. A PIN code is a sequence of any 4 digits. 
PIN should be generated in a range from 0000 to 9999.

If the customer chooses ‘Log into account’, you should ask them to enter their card information. 
Your program should store all generated data until it is terminated so that a user is able to 
log into any of the created accounts by a card number and its pin. You can use an array to store the information.

After all information is entered correctly, you should allow the user to check the account balance; 
right after creating the account, the balance should be 0. It should also be possible to 
log out of the account and exit the program.
"""

import random

id_index = 0
inn = '400000'          # Issuer Identification Number (IIN)
can_length = 9          # Customer Identification Number
checksum = '5'          # any value is okay for now
current_account = None

accounts = []       # card_num, pin, balance, logged_in

def get_new_card_id():
    global inn
    global id_index
    global checksum

    id_index = id_index + 1
    can_str = f"{id_index:09d}"
    new_id = inn + can_str + checksum

    return new_id

def get_new_pin():
    num = random.randint(1000,9999)
    return str(num)

def get_balance(card_id):
    found = find_account(card_id)
    index = found[0]
    account = found[1]

    if index > -1:
        print(f'Balance: {account[2]}')
        print()
        # return account[2]

def create_account():
    global accounts

    new_id = get_new_card_id()
    new_pin = get_new_pin()

    accounts.append([new_id, new_pin, 0, False])

    print('Your card has been created')
    print('Your card number:')
    print(new_id)
    print('Your card PIN:')
    print(new_pin)
    print()

def find_account(card_id):
    global accounts

    for index, row in enumerate(accounts):
        try:
            column = row.index(card_id)
        except ValueError:
            continue
        # return row, index, column
        return [index, row]

    return [-1, -1]

def update_account(index, account):
    global accounts
    accounts[index] = account

def print_menu():
    global current_account

    if current_account is None:
        print('1. Create an account')
        print('2. Log into account')
        print('0. Exit')
    else:
        print('1. Balance')
        print('2. Log out')
        print('0. Exit')

def log_in():
    global current_account

    # find id and pin from the account array
    card_str = input('Enter your card number:')
    pin_str = input('Enter your PIN:')

    found = find_account(card_str)
    index = found[0]
    account = found[1]

    if index > -1 and account[1] == pin_str:
        account[3] = True
        update_account(index, account)
        current_account = account

        print('You have successfully logged in!')
        print()
    else:
        print()
        print('Wrong card number or PIN!')
        print()

    return account

def log_out(card_id):
    global current_account

    found = find_account(card_id)
    index = found[0]
    account = found[1]

    if index > -1:
        account[3] = False
        update_account(index, account)
        current_account = None

        print('You have successfully logged out!')
        print()

choice = -1
while choice != "0":
    print_menu()
    choice = input()
    if choice == '0':
        current_account = None
        print("Bye!")
        break
    else:
        number = int(choice)

        if current_account is None:
            if number == 1:
                create_account()
            elif number == 2:
                log_in()
        else:
            card_id = current_account[0]
            if number == 1:
                get_balance(card_id)
            elif number == 2:
                log_out(card_id)



