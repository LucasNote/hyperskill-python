# Write your code here
import random
class Banking():

    def __init__(self):
        self.iin = 400000
        self.balance = 0
        self.out = False
        self.out2 = False

    def menu(self):
        while True:
            if self.out2 == True:
                return
            print(" ")
            print("1. Create an account")
            print("2. Log into account")
            print("0. Exit")

            self.decide = int(input())
            if self.decide == 1:
                Banking.create(self)
            elif self.decide == 2:
                Banking.checkCard(self)
            elif self.decide == 0:
                self.out2 = True
                print("Bye!")
                return

    def card(self):
        self.y = 0
        self.x = ""
        self.card1 = ""
        self.realcard = ""
        self.pincard = ""
        self.iin2 = str(self.iin)
        for i in range(10):
            self.y = random.randint(0, 9)
            self.x = str(self.y)
            self.card1 = self.card1 + self.x
        self.realcard = self.iin2 + self.card1
        for i in range(4):
            self.x = random.randint(0, 9)
            self.y = str(self.x)
            self.pincard = self.pincard + self.y

    def login(self):
        while True:
            if self.out == True:
                return
            print(" ")
            print("1. Balance")
            print("2. Log out")
            print("0. Exit")

            self.decide = int(input())
            if self.decide == 1:
                print(" ")
                print("Balance:",self.balance)
            elif self.decide == 2:
                print(" ")
                print("You have successfully logged out!")
                self.out = True
                Banking.menu(self)
            elif self.decide == 0:
                print("Bye!")
                self.out2 = True
                break

    def create(self):
        Banking.card(self)
        print(" ")
        print("Your card has been created")
        print("Your card number:")
        print(self.realcard)
        print("Your card PIN:")
        print(self.pincard)

    def checkCard(self):
        print(" ")
        print("Enter your card number:")
        self.tempcard = input()
        print("Enter your PIN:")
        self.temppin = input()

        if self.tempcard == self.realcard and self.temppin == self.pincard:
            print(" ")
            print("You have successfully logged in!")
            Banking.login(self)
        else:
            print(" ")
            print("Wrong card number or PIN!")
            Banking.menu(self)

card1 = Banking()
card1.menu()