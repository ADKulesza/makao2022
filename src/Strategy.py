from abc import ABC, abstractmethod
from Card import Card
from Effect import Effect
import random


class Strategy(ABC):
    def __init__(self):
        self._demands = {'J': self._use_jack,
                         'A': self._use_ace}

    def _use_jack(self, jack: Card, card_symbol: str = None):
        if card_symbol is not None:
            jack.effect.card_symbol = card_symbol
        else:
            card_symbol = random.randint(5, 10)
            jack.effect.card_symbol = f"{card_symbol}"

        return card_symbol
        # to ustawia tylko żądanie, ale kartę i tak trzeba przekazać returnem w danej strategii

    def _use_ace(self, ace: Card, card_color: str = None):
        if card_color is not None:
            ace.effect.card_color = card_color
        else:
            card_color = random.choice(["C", "D", "H", "S"])
            ace.effect.card_color = card_color
        return card_color

    def _group_cards(self, card_list: list):
        grouped_cards = {}
        for c in card_list:
            if c.value not in grouped_cards.keys():
                if c not in grouped_cards.keys():
                    grouped_cards[f"{c.value}"] = []
            grouped_cards[f"{c.value}"].append(c)
        return grouped_cards

    @abstractmethod
    def best_move(self, cards: list, e: Effect, top_card: Card):
        pass


class RandomStrategy(Strategy):

    def __str__(self):
        return 'random strategy'

    def best_move(self, playable_cards: list, e: Effect, top_card: Card):
        if len(playable_cards) > 0:
            random_card = random.choice(playable_cards)
            if random_card.value in self._demands.keys():
                demand = self._demands[random_card.value](random_card)
                print(f'{demand} is requested!')
            return [random_card]
        return None


class AggressiveStrategy(Strategy):

    def __str__(self):
        return 'aggressive strategy'

    def best_move(self, playable_cards: list, e: Effect, top_card: Card):
        grouped = self._group_cards(playable_cards)
        if 'K' in [c.value for c in playable_cards] and [c.color == 'C' or c.color == 'H' for c in playable_cards]:
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
            if len(playable_cards) == 0:
                return None
            card_to_play = random.choice(playable_cards)

        if isinstance(card_to_play, Card):
            card_to_play = [card_to_play]

        if card_to_play[-1].value in self._demands.keys():
            demand = self._demands[card_to_play[-1].value](card_to_play[-1])
            print(f'{demand} is requested!')

        return card_to_play


class UpgradedRandomStrategy(Strategy):

    def __str__(self):
        return 'upgrade random strategy'

    def best_move(self, playable_cards: list, e: Effect, top_card: Card):
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
            if len(playable_cards) == 0:
                return None
            return [random.choice(playable_cards)]

        possible_moves = playable_cards + multiple_cards_moves
        card_to_play = random.choice(possible_moves)
        if isinstance(card_to_play, Card):
            card_to_play = [card_to_play]
        return card_to_play


''' Klasa PatientStrategy to odwrotnosc klasy QuickStrategy. Moze wydawac sie to absurdalne, ze schodzimy z
najmniejszej ilosci kart, ale sprawia to, ze zostaja nam w reku karty, ktore z wiekszym prawdopodobienstwem
rzucimy razem w nastepnym ruchu. W QuickStrategy po wyrzuceniu najwiekszej grupy kart zostajemy
z duza iloscia pojedynczych kart, ktorych nie mozemy razem zagrac, w prawdziwej grze w makao dziala dobrze :-)'''


class PatientStrategy(Strategy):

    def __str__(self):
        return 'patient strategy'

    def best_move(self, playable_cards: list, e: Effect, top_card: Card):
        ind = 0
        grouped = self._group_cards(playable_cards)
        min_len = 5
        for c in playable_cards:
            if len(grouped[c.value]) < min_len:
                min_len = len(grouped[c.value])
                ind = c.value
        if ind in grouped.keys():
            group = grouped[ind]
            for c in group:
                if c in playable_cards:
                    ind = group.index(c)
                    group[ind], group[0] = group[0], group[ind]
                card_to_play = group
        else:
            if len(playable_cards) == 0:
                return None
            return [random.choice(playable_cards)]

        if isinstance(card_to_play, Card):
            card_to_play = [card_to_play]
        return card_to_play


class QuickStrategy(Strategy):

    def __str__(self):
        return 'quick strategy'

    def best_move(self, playable_cards: list, e: Effect, top_card: Card):
        ind = 0
        grouped = self._group_cards(playable_cards)
        max_len = 0
        for c in playable_cards:
            if len(grouped[c.value]) > max_len:
                max_len = len(grouped[c.value])
                ind = c.value
        if ind in grouped.keys():
            group = grouped[ind]
            for c in group:
                if c in playable_cards:
                    ind = group.index(c)
                    group[ind], group[0] = group[0], group[ind]
                card_to_play = group
        else:
            if len(playable_cards) == 0:
                return None
            return [random.choice(playable_cards)]

        if isinstance(card_to_play, Card):
            card_to_play = [card_to_play]
        return card_to_play


colors = ["C", "D", "H", "S"]
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
effects = {"2": {"extra_cards": 2}, "3": {"extra_cards": 3}, "4": {"pause": 1},
           "HK": {"extra_cards": 5}, "CK": {"extra_cards": 5, "whos_next": -1}}
player1_cards = [Card("C", "2", Effect(**effects["2"])), Card("C", "8", Effect()),
                 Card("D", "3", Effect(**effects["3"]))]
player2_cards = [Card("S", "2", Effect(**effects["2"])), Card("D", "2", Effect(**effects["2"])),
                 Card("H", "2", Effect(**effects["2"])), Card("D", "10", Effect()),
                 Card("C", "6", Effect()), Card("H", "6", Effect()), Card("C", "K", Effect(**effects["CK"])),
                 Card("H", "K", Effect(**effects["HK"]))]
