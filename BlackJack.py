import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:  # individual card

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):  # adds every card into deck
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):  # prints name of every card still in deck
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle(self):  # shuffle deck
        random.shuffle(self.deck)

    def deal(self):  # returns one card from deck
        single_card = self.deck.pop()
        return single_card


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):  # adds card to hand
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':  # keeps track of aces in hand
            self.aces += 1

    def adjust_for_ace(self):  # chekcs if hand can be valid if ace value is lowered to 1
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self, total):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):  # adds bet to total if win
        self.total += self.bet

    def lose_bet(self):  # takes bet from total if lose
        self.total -= self.bet


def take_bet(chips):  # sees how much player wants to bet
    while True:
        try:
            chips.bet = int(input('How much would you like to bet: '))
        except ValueError:
            print('Bet must be a whole number')
        else:
            if chips.bet > chips.total:
                print(f'Sorry, you\'re bet cant exceed {chips.total}')
            else:
                break


def hit(deck, hand):  # hits player
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):  # asks player to hit or stand
    global playing
    while True:
        choice = str(input("Would you like to Hit('H') or Stand('S'): "))

        if choice.lower() == 'h':
            hit(deck, hand)
        elif choice.lower() == 's':
            print('Player stands. Dealer is playing')
            playing = False
        else:
            print('Sorry, please try again.')
            continue
        break


def show_some(player, dealer):  # shows player's hand and one of dealer's cards
    print('\nDealer: ')
    print('<hidden card>')
    print(dealer.cards[1])
    print('\nYou:')
    for card in player.cards:
        print(card)
    print('Your Hand  = ', player.value)
    print('----------------\n')


def show_all(player, dealer):  # shows all cards
    print('\nDealer: ')
    for card in dealer.cards:
        print(card)
    print('Dealer\'s Hand  = ', dealer.value, '\n')
    print('\nYou:')
    for card in player.cards:
        print(card)
    print('Your Hand  = ', player.value, '\n')


def player_busts(chips):
    print('You bust!')
    chips.lose_bet()


def player_wins(chips):
    print('You win!')
    chips.win_bet()


def dealer_busts(chips):
    print('Dealer busts!')
    chips.win_bet()


def dealer_wins(chips):
    print('Dealer wins!')
    chips.lose_bet()


# GAME LOGIC
running = True
playing = True
bust = False
user_chip_total = 100
while running:
    playing = True
    print('Welcome to BlackJack!')
    print('You have ', user_chip_total, ' chips')

    game_deck = Deck()
    game_deck.shuffle()

    user = Hand()
    computer = Hand()

    user.add_card(game_deck.deal())
    computer.add_card(game_deck.deal())
    user.add_card(game_deck.deal())
    computer.add_card(game_deck.deal())

    user_chips = Chips(user_chip_total)
    take_bet(user_chips)

    show_some(user, computer)

    while playing:
        hit_or_stand(game_deck, user)
        show_some(user, computer)
        if user.value > 21:
            player_busts(user_chips)
            bust = True
            playing = False

    if not bust:
        while computer.value < 17:
            hit(game_deck, computer)
        show_all(user, computer)
        if computer.value > 21:
            dealer_busts(user_chips)
        elif computer.value > user.value:
            dealer_wins(user_chips)
        elif computer.value < user.value:
            player_wins(user_chips)
        else:
            print('Push!')

    print('You have ', user_chips.total, ' chips')  # Tell player chip total
    user_chip_total = user_chips.total
    if user_chip_total == 0:
        print('You a broke boi!')
        break
    else:
        pass

    while True:
        replay = str(input("Would you like to play again('Y' or 'N')"))

        if replay.lower() == 'y':
            print('Okay')
        elif replay.lower() == 'n':
            running = False
        else:
            print('Sorry, please try again.')
            continue
        break
