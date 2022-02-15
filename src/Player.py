import copy

from Strategy import Strategy


class Player:

    def __init__(self, name, cards: list, strategy: Strategy):
        self.__player_pause = 0
        self.__cards = cards
        self.__strategy = strategy
        self.__player_name = name

    def __repr__(self):
        return f'{self.__player_name}'

    @property
    def cards(self):
        return self.__cards

    def __len__(self):
        return len(self.__cards)

    @property
    def strategy(self):
        return self.__strategy

    @property
    def player_pause(self):
        return self.__player_pause

    @player_pause.setter
    def player_pause(self, player_pause):
        self.__player_pause = player_pause

    @cards.setter
    def cards(self, cards):
        self.__cards = cards

    def take_cards(self, cards):
        for card in cards:
            self.__cards.append(card)

    def play(self, top_card, e):

        self.__player_pause = copy.copy(e.pause)  # copy for safety

        if self.__player_pause != 0:
            self.__player_pause -= 1
            return None

        playable_cards = []
        for card in self.__cards:
            if top_card.can_follow(card, e) == True:
                playable_cards.append(card)
        played_cards = self.__strategy.best_move(playable_cards, e, top_card)

        if played_cards is None:
            return None

        for card in played_cards:
            self.__cards.remove(card)

        return played_cards
