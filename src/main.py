# this is a scratch, at least for now

currently_plays = 0
players = []                # create players here
talia = Deck.generate(players)     # create a standard deck of 52 cards
used_cards = Deck([])       # table is an empty deck
after_makao = False
used_cards.append(talia.give(1))
e = Effect()                # start from an empty effect
while not after_makao:
    top_card = used_cards.show_top()
    # Player plays by returning a list of cards, that may be empty ....
    played_cards = players[currently_plays].play(top_card, e)
    # .... and puts cards on a table
    used_cards.extend(played_cards)
    for crd in played_cards:
        e.combine(crd.effect)
    currently_plays = (currently_plays+e.whos_next ) % len(players)


used_cards.extend(played_cards)

if talia.cards_left == 0:
    talia = used_cards[:-1].shuffle()
    used_cards = used_cards[-1]