from Deck import Deck
from Effect import Effect

# this is a scratch, at least for now

currently_plays = 0
players = []                # create players here
talia = Deck.generate()     # create a standard deck of 52 cards
used_cards = Deck([])       # table is an empty deck
after_makao = False
used_cards.append(talia.give(1)) # trzeba ogarnąć żeby nie była funkcyjna, więc w pętli trzeba to zrobić
e = Effect()                # start from an empty effect
while not after_makao:
    top_card = used_cards.show_top()
    # Player plays by returning a list of cards, that may be empty ....
    played_cards = players[currently_plays].play(top_card, e)
    # jeśli gracz nie dał żadnej karty to dobiera karty (można dodać zasadę z pierwszą dobraną kartą do zagrania)
    if players[currently_plays].number_of_cards == 0:
        after_makao = True
        print("Player {players[currently_plays]} wins!!!")
        break
    if not played_cards:
        # dopisz stakujący efekt playerowi -> musi wziąć karty lub trzeba mu dopisać pauzy
        if e.extra_cards != 0:
            players[currently_plays].take_cards(talia.give(e.extra_cards()))
        elif e.pause != 0:
            players[currently_plays].pause = e.pause
        e.clear()

    # trzeba przypisać graczowi stakujące się pauzy (jeśli != 0) i wpisać e.clear()
    # trzeba czyścić stakujący się efekt jeśli karty zostały dobrane lub pauzy przypisane do playera
    # trzeba rozwiązać problem króla pik -> gdy zostanie zagrany kolejka się cofa do poprzedniego gracza,
    # ale potem powinna przeskoczyć o 2 do przodu (gracz, który zagrał w ruchu króla pik nie może znów wykonywać ruchu)
    # można np. dać tu zmienną, która gdy whos next = -1 to dolicza sobie 1 i potem przesuwa o tą liczbę kolejek do przodu
    used_cards.extend(played_cards)
    for crd in played_cards:
        e.combine_effect(crd.effect)
    currently_plays = (currently_plays + e.whos_next ) % len(players)
    used_cards.extend(played_cards)
    if talia.cards_left == 0:
        talia = used_cards[:-1].shuffle()
        used_cards = used_cards[-1]
