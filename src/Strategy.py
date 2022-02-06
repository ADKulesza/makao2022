from abc import abstractmethod
from Card import Card 
from Effect import Effect
import random

class Strategy:
    def __init__(self):
        pass

    @abstractmethod
    def best_move(self, cards: list[Card], e: Effect, top_card: Card):
        pass


class AggressiveStrategy(Strategy):
    def best_move(self, cards: list[Card], e: Effect, top_card: Card):
        playable_cards = [c for c in cards if c.can_follow(top_card, e)]
        print(playable_cards)
        if 'HK' or 'CK' in [c.value for c in playable_cards]:
            card_to_play = [c for c in playable_cards if c.value == 'HK' or 'CK']
        elif '3' in [c.value for c in playable_cards]:
            card_to_play = [c for c in playable_cards if c.value == '3']
        elif '2' in [c.value for c in playable_cards]:
            card_to_play = [c for c in playable_cards if c.value == '2']
        elif '4' in [c.value for c in playable_cards]:
            card_to_play = [c for c in playable_cards if c.value == '4']
        elif 'J' in [c.value for c in playable_cards]:
            card_to_play = [c for c in playable_cards if c.value == 'J']
        else:
            card_to_play = random.choice(playable_cards)

        return card_to_play


class RandomStrategy(Strategy):
    def best_move(self, cards: list[Card], e: Effect, top_card: Card):
        playable_cards = list([c for c in cards if c.can_follow(top_card, e)])
        multiple_cards = [c for c in playable_cards if c.value == top_card.value]
        if len(multiple_cards) > 1:
            multiple_cards_moves = [multiple_cards[0]]
            for c in multiple_cards:
                if len(multiple_cards_moves) == 1 and len(multiple_cards) >= 2:
                    multiple_cards_moves.append([multiple_cards[0], multiple_cards[1]])
                elif len(multiple_cards_moves) == 2 and len(multiple_cards) >= 3:
                    multiple_cards_moves.append([multiple_cards[0], multiple_cards[1], multiple_cards[2]])
                elif len(multiple_cards_moves) == 3 and len(multiple_cards) >= 4:
                    multiple_cards_moves.append([multiple_cards[0], multiple_cards[1], multiple_cards[2], multiple_cards[3]])

        possible_moves = playable_cards + multiple_cards_moves
        print(possible_moves)
        print(playable_cards)
        return random.choice(possible_moves)


colors = ["C", "D", "H", "S"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
effects = {"2": {"extra_cards": 2}, "3": {"extra_cards": 3}, "4": {"pause": 1}
           , "HK": {"extra_cards": 5}, "CK": {"extra_cards": 5, "whos_next": -1}}

player1_cards = [Card("C", "2", Effect(**effects["2"])), Card("C", "8", Effect()), Card("D", "3", Effect(**effects["3"]))]
player2_cards = [Card("S", "2", Effect(**effects["2"])), Card("D", "2", Effect(**effects["2"])), Card("H", "2", Effect(**effects["2"])), Card("D", "10", Effect())]

#s = RandomStrategy()
s = AggressiveStrategy()
# bm1 = s.best_move(player1_cards, Effect(**effects["2"]), Card("D", "2", Effect(**effects["2"])))
# print(bm1)
bm2 = s.best_move(player2_cards, Effect(**effects["2"]), Card("C", "2", Effect(**effects["2"])))
print(bm2)