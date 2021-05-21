from card_collection import CardCollection


class BankingSystemProcessor:
    MAIN_MENU_COMMANDS = ("1. Create an account\n"
                          "2. Log into account\n"
                          "0. Exit\n")

    LOGIN_ACTIONS = ("1. Balance\n"
                     "2. Log out\n"
                     "0. Exit\n")

    program_run = True

    @classmethod
    def run_main_menu(cls):
        while cls.program_run:
            user_command = input(cls.MAIN_MENU_COMMANDS)

            if user_command == '0':
                cls.program_run = False

            elif user_command == '1':
                CardCollection().add_card()

            elif user_command == '2':
                cls._login_validation()

        print("Bye!")

    @classmethod
    def _card_login_actions(cls, card):
        while True:
            user_command = input(cls.LOGIN_ACTIONS)

            if user_command == '0':
                cls.program_run = False
                return None

            elif user_command == '1':
                print(card.get_balance())

            elif user_command == '2':
                return None

    @classmethod
    def _login_validation(cls):
        card = CardCollection.card_login(input("Enter your card number:\n"),
                                         input("Enter your PIN:\n"))
        if card:
            cls._card_login_actions(card)