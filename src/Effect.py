from copy import copy, deepcopy


class Effect:

    def __init__(self, **kwargs):
        self.__card_color = kwargs.get('color', None)
        self.__card_symbol = kwargs.get('symbol', None)
        self.__extra_cards = int(kwargs.get('extra_cards', 1))
        self.__pause = int(kwargs.get('pause', 0))
        self.__block = kwargs.get('block', False)
        self.__whos_next = int(kwargs.get('whos_next', 1))
        if self.__whos_next == 1:
            self.__direction = "forward"
        else:
            self.__direction = "backward"

    def __str__(self):
        e_str = ''.join([f"card_color_demand: {self.__card_color}\n",
                         f"card_symbol_demand: {self.__card_symbol}\n",
                         f"extra_cards: {self.__extra_cards}\n" f"pause: {self.__pause}\n",
                         f"king_block: {self.__block}\n",
                         f"direction: {self.__direction}\n"])
        return e_str

    def combine_effect(self, e):
        if e.__whos_next == -1:
            self.__whos_next = -1
        else:
            self.__whos_next = 1

        if e.__card_color is not None or e.__card_symbol is not None:
            self.__card_color = e.__card_color
            self.__card_symbol = e.__card_symbol
            self.__extra_cards = 1

        elif self.__block is True:
            self.__extra_cards = 0
        else:
            self.__extra_cards += e.__extra_cards
            self.__block = False
        self.__pause += e.__pause

    def clear(self):
        self.__extra_cards = 0
        self.__pause = 0

    def is_clear(self):
        if self.__extra_cards in [0,
                                  1] and self.__pause == 0 and self.__card_color is None and self.__card_symbol is None:
            return True
        else:
            return False

    @property
    def card_color(self):
        return deepcopy(self.__card_color)

    @card_color.setter
    def card_color(self, card_color):
        self.__card_color = card_color

    @property
    def card_symbol(self):
        return deepcopy(self.__card_symbol)

    @card_symbol.setter
    def card_symbol(self, card_symbol):
        self.__card_symbol = card_symbol

    @property
    def whos_next(self):
        return self.__whos_next

    @whos_next.setter
    def whos_next(self, whos_next: int):
        self.__whos_next = whos_next

    @property
    def extra_cards(self):
        return self.__extra_cards

    @extra_cards.setter
    def extra_cards(self, extra_cards: int):
        self.__extra_cards = extra_cards

    @property
    def pause(self):
        return self.__pause

    @pause.setter
    def pause(self, pause: int):
        self.__pause = pause
