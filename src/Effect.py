from copy import deepcopy


# can follow musi sprawdzać efekty! np. jeśli kolor wymagany to albo as albo joker albo ten kolor
# podobnie z symbolem -> wtedy jopek
# jeśli nie to w playerze by to musiało być
class Effect:

    def __init__(self, **kwargs):
        self.__card_color = kwargs.get('color', None)
        self.__card_symbol = kwargs.get('symbol', None)
        self.__extra_cards = int(kwargs.get('extra_cards', 0))
        self.__pause = int(kwargs.get('pause', 0))
        self.__block = kwargs.get('block', False)
        self.__whos_next = int(kwargs.get('whos_next', 1))

    def combine_effect(self, e: Effect):
        if e.__whos_next == -1:
            self.__whos_next = -1
        else:
            self.__whos_next = 1

        self.__card_color = e.__card_color
        self.__card_symbol = e.__card_symbol

        if self.__block is True:
            self.__extra_cards = 0
        else:
            self.__extra_cards += e.__extra_cards
            self.__block = False
        self.__pause += e.__pause

    def clear(self):
        self.__extra_cards = 0
        self.__pause = 0

    @property
    def card_color(self):
        return deepcopy(self.__card_color)

    @card_color.setter
    def card_color(self, card_color):
        self.__card_color = card_color

    @property
    def card_symbol(self):
        return deepcopy(self.card_symbol)

    @card_symbol.setter
    def card_symbol(self, card_symbol):
        self.__card_symbol = card_symbol

    @property
    def whos_next(self):
        return self.__whos_next

    @whos_next.setter
    def whos_next(self, whos_next):
        self.__whos_next = whos_next
