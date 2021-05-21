class Card:
    BIN = '400000'

    def __init__(self, iin, checksum, pin, balance=0):
        self.iin = iin
        self.checksum = checksum
        self.pin = pin
        self.balance = balance

    def get_card_number(self):
        return f'{self.BIN}{self.iin}{self.checksum}'

    def get_card_pin(self):
        return self.pin

    def get_balance(self):
        return self.balance