from Deck import Deck
from Effect import Effect
from Player import Player
from Strategy import RandomStrategy
import random


currently_plays = 0
deck = Deck.generate()  # create a standard deck of 52 cards
players = []  # create players here
number_of_players = 2
for i in range(1, number_of_players + 1):
    # TODO losowa strategia
    new_player = Player(str(i), deck.give(5), RandomStrategy())
    players.append(new_player)

used_cards = Deck([])
used_cards.append(deck.get_start_card())
top_card = used_cards.show_top()
after_makao = False
e = Effect()  # start from an empty effect

i = 0
while not after_makao:

    current_player = players[currently_plays]
    print('\n[!] turn:', i, ', player:', current_player)
    print('active effect:\n', e)
    print('table', used_cards)

    # Checking if there are enough cards in deck
    if deck.cards_left() < e.extra_cards:
        to_deck_cards = used_cards.leave_only_one()
        random.shuffle(to_deck_cards)
        deck.extend(to_deck_cards)

    # Checking what a player can do
    play_card = current_player.play(top_card, e)
    if play_card is None:

        if current_player.player_pause == 0:
            cards_to_take = deck.give(e.extra_cards)
            current_player.take_cards(cards_to_take)  # give
            print(f'player {current_player} takes {e.extra_cards} cards')

        else:
            print(f'player {current_player} is waiting!')

        e = Effect()

    else:
        print(f'player {current_player} has played a {play_card}')
        used_cards.extend(play_card)
        top_card = used_cards.show_top()

        # Checking if current player has any cards
        if len(current_player) == 0:
            after_makao = True
            print(f"!!! player {current_player} wins !!!")
            break

        # If any effect is clear then combine effects
        if e.is_clear() is False:
            print('[!!] activate trap card')
            e.combine_effect(top_card.effect)
        # If effect is not clear it means the player has been punished
        else:
            e = top_card.effect

    currently_plays += e.whos_next
    currently_plays = currently_plays % number_of_players
    i += 1
