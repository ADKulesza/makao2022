from Deck import Deck
from Effect import Effect
from Player import Player
from Strategy import RandomStrategy, AggressiveStrategy, UpgradedRandomStrategy, PatientStrategy, QuickStrategy
import random

deck = Deck.generate()  # create a standard deck of 52 cards
players = []  # create players here
number_of_players = 4
strategies = [RandomStrategy, AggressiveStrategy,
              UpgradedRandomStrategy, PatientStrategy, QuickStrategy]

for i in range(1, number_of_players + 1):
    strategy = random.choice(strategies)()
    new_player = Player(str(i), deck.give(5), strategy)
    players.append(new_player)
    print(f'playeer {i} has {strategy}')

used_cards = Deck([])
used_cards.append(deck.get_start_card())
top_card = used_cards.show_top()
after_makao = False
e = Effect()  # start from an empty effect

currently_plays = 0
i = 0
while not after_makao:

    current_player = players[currently_plays]
    print('\n[!] turn:', i, '| player:', current_player, '| left cards:', len(current_player))
    print('active effect:\n', e)
    print('table', used_cards)

    # Checking if there are enough cards in deck
    if deck.cards_left() < e.extra_cards:
        to_deck_cards = used_cards.leave_only_one()
        random.shuffle(to_deck_cards)
        deck.extend(to_deck_cards)
        if deck.cards_left() < e.extra_cards:
            print('Not enough cards in deck!')
            e.extra_cards = deck.cards_left()

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

        # If effect is not clear then combine effects
        if e.is_clear() is False:
            # TU jest coś nie tak
            print('[!!] activate trap card')
            e.combine_effect(top_card.effect)
        # If effect is clear it means the player has been punished
        else:
            e = top_card.effect

    currently_plays += e.whos_next
    currently_plays = currently_plays % number_of_players
    i += 1
