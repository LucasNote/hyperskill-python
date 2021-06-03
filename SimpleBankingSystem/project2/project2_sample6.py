# Write your code here
import random
d = {}
def luhn(card_number):
    v = [int(x) for x in str(card_number)]
    for x in range(0,len(v),2):
        if v[x]*2 > 9:
            v[x] = v[x]*2-9
        else:
            v[x] = v[x]*2
    if sum(v)%10 == 0:
        return True
    else:
        return False
while True:
    option = input("1. Create an account\n2. Log into account\n0. Exit\n")
    if option == '1':
        card_number = int(str(400000) + str(random.randint(1111111111, 9999999999)))
        while luhn(card_number) == False:
            card_number = int(str(400000) + str(random.randint(1111111111, 9999999999)))
        pw = int(random.randint(1000, 9999))
        print("Your card has been created\nYour card number:")
        print(int(card_number))
        print("Your card PIN:")
        print(int(pw))
        d.update({card_number:pw})
    elif option == '2':
        login_card_number = input("Enter your card number:")
        login_pw = input("Enter your PIN:")
        if int(login_card_number) not in d or d[int(login_card_number)] != int(login_pw):
            print("Wrong card number or PIN!")
        else:
            print("You have successfully logged in!")
            option_2 = input("1. Balance\n2. Log out\n0. Exit\n")
            if option_2 == '1':
                print("Balance: 0")
            if option_2 == '0':
                option = '0'
                break

    if option == '0':
        print("Bye!")
        break