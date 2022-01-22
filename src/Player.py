from Effect import Effect


class Player:

    def __init__(self, cards: list, strategy: Strategy):
        self.__player_pause = 0
        self.__cards = cards
        self.__strategy = strategy

    def play(self, top_card, e):
        # można sprawdzić czy osoba przed tobą powiedziała makao (jeśli ma jedną kartę)
        #   - > jak nie powiedziała to bierze 5 kart
        # if self._player_pause != 0 --> next player and self.__player_pause -= 1
        # elif received effect has e.__pause != 0 rzuć 4 lub ruch kolejnego gracza, a ty dopisz sobie
        #   kolejki: self.__player_pause += e.__pause -1
        # elif received effect has e.__extra_cards != 0 spr czy masz jakieś pasujące karty z efektem
        #   biorącym (jak 2, 3 czy król karo lub nawet pik -> wtedy całość bierze poprzednia osoba, chyba
        #   że ma czym się obronić)
        # elif self._requested_color != None --> rzuć ten kolor lub asa i zarządaj koloru który masz -> request_color()
        #   a na końcu zresetuj swoje pole self._requested_color na None
        # elif self._requested_symbol != None --> rzuć tą figurę lub jopka i zarządaj posiadanej figury
        #   niefunkcyjnej -> request_symbol() a na końcu zresetuj swoje pole self._requested_symbol na None
        # else sprawdź które karty możesz rzucić i rzuć kartę(karty) według strategii lub weź jedną ze stosu kart

        # po dobraniu kart lub dopisaniu sobie kolejek wyczyść kumulujący się efekt -> e.clear()
        # jeśli masz jedną kartę powiedz makao
        # jeśli dodajemy jokery to wtedy przyda się funkcja copy_effect w klasie Card albo nawet nowej klasie Joker
        # pomyśleć nad królami do blokowania króli biorących
        pass

    def number_of_cards(self):
        # needed for saying "makao" and stategy
        pass

    def peek(self):
        # needed if cheater or other player could see list of cards with small probability
        pass

    def add_card(self):
        # for cheater
        pass

    def hide_card(self):
        # jeśli więcej niż 2 karty cheater może z pewnym prawdopodobieństwem schować jedną (usunąć z gry)
        pass

    def cheat(self):
        # if player has pauses to wait (>=2) small probability to trick others
        # (the bigger no of turns to wait the bigger chance), also for cheater
        # elif player has cards to take, small probability to trick the number (-1 card to take)