from abc import abstractmethod
from Card import Card
from Effect import Effect
import random


class Strategy:
    def __init__(self):
        pass

    def _use_jack(self, jack: Card, card_symbol: str = None):
        if card_symbol is not None:
            jack.card_symbol = card_symbol
        else:
            num = random.randint(5, 10)
            jack.card_symbol = f"{num}"
        # to ustawia tylko żądanie, ale kartę i tak trzeba przekazać returnem w danej strategii

    def _use_ace(self, ace: Card, card_color: str = None):
        if card_color is not None:
            ace.card_symbol = card_color
        else:
            ace.card_symbol = random.choice(["C", "D", "H", "S"])

    def _group_cards(self, card_list: list):
        grouped_cards = {}
        for c in card_list:
            if c.value not in grouped_cards.keys():
                if c not in grouped_cards.keys():
                    grouped_cards[f"{c.value}"] = []
            grouped_cards[f"{c.value}"].append(c)
        return grouped_cards

    def _random_card(self):
        pass

    @abstractmethod
    def best_move(self, cards: list, e: Effect, top_card: Card):
        playable_cards = [c for c in cards if c.can_follow(top_card, e)]
        random_card = random.choice(playable_cards)
        return random_card
        # można wpisać tu metodę random i nie pisać klasy RandomStrategy :))
        # wtedy wystarczy linia return random_card(cards)


class AggressiveStrategy(Strategy):
    def best_move(self, cards: list, e: Effect, top_card: Card):
        playable_cards = [c for c in cards if c.can_follow(top_card, e)]
        strat = Strategy()
        ind = 0
        grouped = strat._group_cards(cards)
        if 'K' in [c.value for c in playable_cards]:
            group = grouped['K']
            for c in group:
                if c in playable_cards:
                    ind = group.index(c)
                    group[ind], group[0] = group[0], group[ind]
            card_to_play = group            
        elif '3' in [c.value for c in playable_cards]:
            group = grouped['3']
            for c in group:
                if c in playable_cards:
                    ind = group.index(c)
                    group[ind], group[0] = group[0], group[ind]
            card_to_play = group
        elif '2' in [c.value for c in playable_cards]:
            group = grouped['2']
            for c in group:
                if c in playable_cards:
                    ind = group.index(c)
                    group[ind], group[0] = group[0], group[ind]
            card_to_play = group
        elif '4' in [c.value for c in playable_cards]:
            group = grouped['4']
            for c in group:
                if c in playable_cards:
                    ind = group.index(c)
                    group[ind], group[0] = group[0], group[ind]
            card_to_play = group
        elif 'J' in [c.value for c in playable_cards]:
            group = grouped['J']
            for c in group:
                if c in playable_cards:
                    ind = group.index(c)
                    group[ind], group[0] = group[0], group[ind]
            card_to_play = group
        else:
            card_to_play = random.choice(playable_cards)
        return card_to_play


class RandomStrategy(Strategy):
    def best_move(self, cards: list, e: Effect, top_card: Card):
        playable_cards = [c for c in cards if c.can_follow(top_card, e)]
        card_to_play = random.choice(playable_cards)
        return card_to_play

class UpgradedRandomStrategy(Strategy):
    def best_move(self, cards: list, e: Effect, top_card: Card):
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
                    multiple_cards_moves.append(
                        [multiple_cards[0], multiple_cards[1], multiple_cards[2], multiple_cards[3]])
        else:
            return random.choice(playable_cards)

        possible_moves = playable_cards + multiple_cards_moves
        return random.choice(possible_moves)


''' Klasa PatientStrategy to odwrotnosc klasy QuickStrategy. Moze wydawac sie to absurdalne, ze schodzimy z
najmniejszej ilosci kart, ale sprawia to, ze zostaja nam w reku karty, ktore z wiekszym prawdopodobienstwem
rzucimy razem w nastepnym ruchu. W QuickStrategy po wyrzuceniu najwiekszej grupy kart zostajemy
z duza iloscia pojedynczych kart, ktorych nie mozemy razem zagrac, w prawdziwej grze w makao dziala dobrze :-)'''
    
class PatientStrategy(Strategy):
    def best_move(self, cards: list, e: Effect, top_card: Card):
        playable_cards = list([c for c in cards if c.can_follow(top_card, e)])
        strat = Strategy()
        ind = 0
        grouped = strat._group_cards(cards)
        min_len = 5
        for c in playable_cards:
             if len(grouped[c.value]) < min_len:
                 min_len = len(grouped[c.value])
                 ind = c.value
        group = grouped[ind]
        for c in group:
            if c in playable_cards:
                    ind = group.index(c)
                    group[ind], group[0] = group[0], group[ind]
            card_to_play = group  
        return card_to_play


class QuickStrategy(Strategy):
    def best_move(self, cards: list, e: Effect, top_card: Card):
        playable_cards = list([c for c in cards if c.can_follow(top_card, e)])
        strat = Strategy()
        ind = 0
        grouped = strat._group_cards(cards)
        max_len = 0
        for c in playable_cards:
             if len(grouped[c.value]) > max_len:
                 max_len = len(grouped[c.value])
                 ind = c.value
        group = grouped[ind]
        for c in group:
            if c in playable_cards:
                    ind = group.index(c)
                    group[ind], group[0] = group[0], group[ind]
            card_to_play = group  
        return card_to_play


colors = ["C", "D", "H", "S"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
effects = {"2": {"extra_cards": 2}, "3": {"extra_cards": 3}, "4": {"pause": 1}
    , "HK": {"extra_cards": 5}, "CK": {"extra_cards": 5, "whos_next": -1}}
player1_cards = [Card("C", "2", Effect(**effects["2"])), Card("C", "8", Effect()),
                 Card("D", "3", Effect(**effects["3"]))]
player2_cards = [Card("S", "2", Effect(**effects["2"])), Card("D", "2", Effect(**effects["2"])),
                 Card("H", "2", Effect(**effects["2"])), Card("D", "10", Effect()),
                 Card("C", "6", Effect()), Card("H", "6", Effect()), Card("C", "K", Effect(**effects["CK"])),
                 Card("H", "K", Effect(**effects["HK"]))]

# s = UpgradedRandomStrategy()
#s = Strategy()
# s = UpgradedRandomStrategy()
s = QuickStrategy()
# bm1 = s.best_move(player1_cards, Effect(**effects["2"]), Card("D", "2", Effect(**effects["2"])))
# print(bm1)
bm2 = s.best_move(player2_cards, Effect(), Card("D", "6", Effect()))
print(bm2)


if __name__ == "__main__":

    from Deck import Deck
    talia = Deck.generate([])
    talia.shuffle()
    player1_cards = talia.give(5)
    #print(player1_cards)
    karta_do_usuniecia = player1_cards[0]
    #print(karta_do_usuniecia)
    player1_cards.remove(karta_do_usuniecia)
    #print(player1_cards)
    