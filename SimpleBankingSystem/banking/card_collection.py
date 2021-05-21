from card_factory import CardFactory


class CardCollection:
    collection = []

    @classmethod
    def add_card(cls):
        new_card = CardFactory.create_new_card()
        cls.collection.append(new_card)

        print("Your card has been created\n"
              "Your card number:\n"
              f"{new_card.get_card_number()}\n"
              "Your card PIN:\n"
              f"{new_card.get_card_pin()}\n")

    @classmethod
    def card_login(cls, card_number, pin):
        for card in cls.collection:
            if (card.get_card_number() == card_number
                    and card.get_card_pin() == pin):
                print("You have successfully logged in!")
                return card

        print("Wrong card number or PIN!")
        return False