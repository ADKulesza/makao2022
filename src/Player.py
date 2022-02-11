from Effect import Effect
from Strategy import Strategy
from Deck import Deck

class Player:

    def __init__(self, name, cards: list, strategy: Strategy):
        self.__player_pause = 0
        self.__cards = cards
        self.__strategy = strategy
        self.__player_name = name

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

    def play(self, top_card, e):
        playable_cards = []
        for _ in self.cards:
            if top_card.can_follow(_) == True:
                playable_cards.append(_)

        if self.player_pause != 0:
            self.player_pause -= 1
            return []

        #        elif playable_cards == 0:
        #           self.__cards.extend(give())
        #        przechodzi do main?

        else:
            return self.strategy.best_move(playable_cards, e, top_card)

# class Cheater(Player):
#    def peek(self):
#        # needed if cheater or other player could see list of cards with small probability
#        pass
#
#    def add_card(self):
#        # for cheater
#        pass
#
#    def hide_card(self):
#        # jeśli więcej niż 2 karty cheater może z pewnym prawdopodobieństwem schować jedną (usunąć z gry)
#        pass
#
#    def cheat(self):
#        pass
#        # if player has pauses to wait (>=2) small probability to trick others
#        # (the bigger no of turns to wait the bigger chance), also for cheater
#        # elif player has cards to take, small probability to trick the number (-1 card to take)
