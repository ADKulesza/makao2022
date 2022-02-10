import copy
from Effect import Effect


class Card:
    def __init__(self, card_color, card_value, effect: Effect):
        self._color = card_color
        self._value = str(card_value)
        self._effect = effect

    def __str__(self):
        return self._color + self._value

    def __repr__(self):
        return self._color + self._value

    def can_follow(self, next_card, e: Effect):
        # trzeba sprawdzić czy jest dobrze i czy to dodanie efektu na stosie jest ok
        if self._value == 'Q':
            return True

        elif self.value == next_card.value:
            return True

        elif e.is_clear() and self.color == next_card.color:
            return True

        elif (self._effect.is_clear() or e.is_clear()) and next_card.value == 'Q':
            return True

        elif self._value == '2':
            if next_card.value == '2':
                return True
            elif next_card.value == '3' and self.color == next_card.color:
                return True
            else:
                return False

        elif self._value == '3':
            if next_card.value == '3':
                return True
            elif next_card.value == '2' and self.color == next_card.color:
                return True
            else:
                return False

        elif self._value == '4':
            if next_card.value == '4':
                return True
            else:
                return False

        elif e.card_color is not None and (next_card.color == e.card_color or next_card.value == "A") :
            return True

        elif e.card_symbol is not None and (next_card.value == e.card_symbol or next_card.value == "J") :
            return True

        else:
            return False

    @property
    def color(self):
        return copy.copy(self._color)

    @property
    def value(self):
        return copy.copy(self._value)

    @property
    def effect(self):
        # It's intentionally without copy
        return self._effect


if __name__ == "__main__":
    pass
