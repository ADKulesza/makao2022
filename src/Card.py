import copy


class Card:
    def __init__(self, card_color, card_value):
        self._color = card_color
        self._value = str(card_value)

    def __str__(self):
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
        self._effect = effect

    @property
    def effect(self):
        return copy.copy(self._effect)


# Czy w kartach funkcyjnych wartość powinna być ustalona z góry
# czy mimo wszystko przyjmować wartość karty w konstruktorze?

class Card2(ActionCard):
    # def __init__(self, card_color, effect):
    #     super().__init__(card_color, 2, effect)

    def can_follow(self, next_card):
        if next_card.value == '2':
            return True
        elif next_card.value == '3' and self.color == next_card.color:
            return True
        else:
            return False


class Card3(ActionCard):
    def can_follow(self, next_card):
        if next_card.value == '3':
            return True
        elif next_card.value == '2' and self.color == next_card.color:
            return True
        else:
            return False


class Card4(ActionCard):
    def can_follow(self, next_card):
        if next_card.value == '4':
            return True
        else:
            return False


class CardJack(ActionCard):
    def __init__(self, color, value, effect, requested_value):
        super().__init__(color, value, effect)
        self.__req_value = requested_value

    def can_follow(self, next_card):
        # Zasada dotyczy całej kolejki (według wiki)
        # trzeba będzie nad tym pomyśleć
        if next_card.value == self.__req_value:
            return True
        elif next_card.value == 'J':
            return True
        else:
            return False


class CardQueen(ActionCard):
    # empty efekt do konstruktora
    def can_follow(self, next_card):
        return True


class CardKingOfSpades(ActionCard):
    # Zrobiłam oddzielną klasę, żeby móc skontrować króla
    # (patrz zasady na wiki)
    # ale pewnie trzeba będzie się nad tym zastanowić
    def can_follow(self, next_card):
        if next_card.value == 'K' and next_card.color == 'H':
            return True
        else:
            return False


class CardKingOfHearts(ActionCard):
    def can_follow(self, next_card):
        if next_card.value == 'K' and next_card.color == 'S':
            return True
        else:
            return False


class CardAce(ActionCard):
    def __init__(self, color, value, effect, requested_color):
        super().__init__(color, value, effect)
        self.__req_color = requested_color

    def can_follow(self, next_card):
        if next_card.color == self.__req_color:
            return True
        else:
            return False


if __name__ == "__main__":
    pass
