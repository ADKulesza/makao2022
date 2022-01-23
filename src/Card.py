import copy


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
    def __init__(self, card_color, card_value, effect=None):
        super().__init__(card_color, card_value)
        self.__effect = effect

    @property
    def effect(self):
        return copy.copy(self.__effect)


if __name__ == "__main__":
    pass
