import random
class Bank:
    def __init__(self, card=0, pin=0):
        self.card = card
        self.pin = pin

    def luhn(self, number):
        suma = 0
        for i in range(15):
            x = int(number[i])
            if i % 2 == 0:
                x *= 2
                if x > 9:
                    x -= 9
            suma += x
        limit = ((suma // 10) + 1) * 10
        check = (limit - suma) % 10
        return '{}{}'.format(number[:15], check)

    def generate(self):
        self.card = int(self.luhn('%d' % random.randint(4*10**15, 4000009999999999)))
        self.pin = int('%04d' % random.randint(0, 9999))



def login_menu():
    global menu
    menu1 = ""
    while menu1 != "0":
        menu1 = input("""
1. Balance
2. Log out
0. Exit
""")
        if menu1 == "1":
            print("Balance: 0")
        elif menu1 == "2":
            print("You have successfully logged out!\n")
            menu1 = "0"
        elif menu1 == "0":
            menu = "0"


def login(account):
    user_card = int(input("Enter you card number: "))
    user_pin = int(input("Enter your PIN: "))
    if account.card == user_card and account.pin == user_pin:
        print("You have successfully logged in!")
        login_menu()
    else:
        print("Wrong card number or PIN!")


def create_account(account):
    account.generate()
    print(f"""Your card has been created
Your card number:
{account.card}
Your card PIN:
{account.pin}""")

def menu1():
    global menu
    menu = ""
    account = Bank()
    while menu != "0":
        menu = input("""
1. Create an account
2. Log into account
0. Exit
""")

        if menu == "1":
            create_account(account)
        elif menu == "2":
            login(account)
    print("Bye!")
if __name__=='__main__':
    menu1()