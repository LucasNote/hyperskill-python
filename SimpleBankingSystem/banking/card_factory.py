import random
from card import Card


class CardFactory:
    @staticmethod
    def create_new_card():
        return Card(CardFactory._generate_iin(),
                    CardFactory._generate_checksum(),
                    CardFactory._generate_pin())

    @staticmethod
    def _generate_iin():
        return ''.join([str(random.randint(0, 9)) for _ in range(9)])

    @staticmethod
    def _generate_pin():
        return ''.join([str(random.randint(0, 9)) for _ in range(4)])

    @staticmethod
    def _generate_checksum():
        return str(random.randint(0, 9))