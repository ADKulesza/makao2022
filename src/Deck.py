from copy import deepcopy
# from Card import Card
import random


# I will change card representation to Card (from str) after the class is written
# is it necessary to change shuffle to my own method?


class Deck:

    def __init__(self, list_of_cards: list = []):
        self.__list_of_cards = list_of_cards
        # for i in self.__list_of_cards:
        #    if not isinstance(i, Card):
        #        print(f"{i} is not an object Card!")

    @staticmethod
    def generate():
        # C - clubs, D - diamonds, H - hearts, S - spades
        colors = ["C", "D", "H", "S"]
        symbols = ["A", "K", "Q", "J"]
        for i in reversed(range(2, 11)):
            symbols.append(str(i))
        deck = []
        for c in colors:
            for s in symbols:
                # deck.append(Card(c, s))
                deck.append(c + s)
        random.shuffle(deck)
        print(deck)
        return Deck(deck)

    def shuffle(self):
        random.shuffle(self.__list_of_cards)

    def peek(self):
        print(self.__list_of_cards)

    def give(self, number: int = 1):
        # is this possible to return unpacked list of cards?
        give_cards = []
        for i in range(number):
            give_cards.append(self.__list_of_cards.pop())
        return give_cards

    def extend(self, c_list: list):
        self.__list_of_cards.extend(reversed(c_list))

    # def append(self, card: Card):
    def append(self, card):
        self.__list_of_cards.append(card)

    def show_top(self):
        return deepcopy(self.__list_of_cards[-1])

"""
    @property #check what talia.cards_left does!
    def remaining_cards(self):
        return deepcopy(self.__remaining_cards)
"""

if __name__ == "__main__":
    talia = Deck.generate()
    talia.shuffle()
    talia.peek()
    cards = talia.give(3)
    print(cards)
    talia.peek()
    talia.extend(cards)
    # talia.append(Card(S, 10))
    talia.append("S10")
    print(talia.show_top())
