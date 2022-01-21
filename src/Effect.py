from copy import deepcopy


class Effect:

    def __init__(self, **kwargs):
        self.__card_color = kwargs.get('color',
                                       None)  # dopisać funkcję request_color() do Card zmieniającą to pole - wywołanie tylko gdy to as?
        self.__card_symbol = kwargs.get('symbol',
                                        None)  # dopisać funkcję request_symbol() do Card zmieniającą to pole - wywołanie tylko gdy to jopek?
        self.__extra_cards = int(kwargs.get('extra_cards', 0))
        self.__pause = int(kwargs.get('pause', 0))
        self.whos_next = int(kwargs.get('whos_next', 1))
        self.__players_list = kwargs.get('players', None)

    def combine_effect(self, e: Effect):
        if e.whos_next == -1:
            self.whos_next = -1
        else:
            self.whos_next = 1

        if self.__players_list is None:
            self.__players_list = e.__players_list

        if e.card_color != None:
            for p in self.__players_list:
                p.requested_color = e.__card_color
        elif e.card_symbol != None:
            for p in self.__players_list:
                p.requested_symbol = e.__card_symbol

        self.__extra_cards += e.__extra_cards
        self.__pause += e.__pause
        # self.__players_list = None  - czy jest sens czyścić listę playerów?

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
