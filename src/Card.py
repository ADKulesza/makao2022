import copy
from Effect import Effect


class Card:
    def __init__(self, card_color, card_value):
        self._color = card_color
        self._value = str(card_value)

    def __str__(self):
        return self._color + self._value

    def __repr__(self):
        return self._color + self._value

    def can_follow(self, next_card):
        if self._color == next_card.color or self.value == next_card.value:
            return True
        elif next_card.value == 'Q':
            # "Dama na wszystko"
            return True
        else:
            return False

    @property
    def color(self):
        return copy.copy(self._color)

    @property
    def value(self):
        return copy.copy(self._value)


class ActionCard(Card):
    def __init__(self, card_color, card_value, effect: Effect):
        super().__init__(card_color, card_value)
        self.__effect = effect

    @property
    def effect(self):
        # It's intentionally without copy
        return self.__effect

    def can_follow(self, next_card):

        # Card value = Queen
        if self._value == "Q":
            # "wszystko na damę"
            return True

        if self._value == '2':
            if next_card.value == '2':
                return True
            elif next_card.value == '3' and self.color == next_card.color:
                return True
            else:
                return False

        if self._value == '3':
            if next_card.value == '3':
                return True
            elif next_card.value == '2' and self.color == next_card.color:
                return True
            else:
                return False

        if self._value == '4':
            if next_card.value == '4':
                return True
            else:
                return False

        # Card value = Ace
        if self.__effect.card_color is not None:
            # Czy asy ograniczają zasadę "dama na wszystko"?
            if next_card.color == self.__effect.card_color:
                return True
            elif next_card.value == 'A':
                return True
            else:
                return False

        # Card value = Jack
        if self.__effect.card_symbol is not None:
            if next_card.value == str(self.__effect.card_symbol):
                return True
            elif next_card.value == 'J':
                return True
            else:
                return False

        # Card value = King
        if self.__effect.extra_cards == 5:
            if self.__effect.whos_next == -1:
                if next_card.value == 'K' and next_card.color == 'H':
                    return True
                else:
                    return False
            else:
                if next_card.value == 'K' and next_card.color == 'S':
                    return True
                else:
                    return False

        # if any of the above conditions is not true
        # act like normal card
        super().can_follow(next_card)


if __name__ == "__main__":
    pass
