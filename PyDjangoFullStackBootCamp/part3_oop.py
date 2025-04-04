#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print('Create ordered deck')
        self.allcards = [(s, r) for s in SUITE for r in RANKS]
        # stvaranje objekta/liste u kojem se nalaze sve karte

    def shuffle(self):
        print('Shuffling cards')
        shuffle(self.allcards)
        # mjesanje svih karata

    def split_in_half(self):
        return self.allcards[:26], self.allcards[26:]
        # podjela karata po pola, svakom igracu jedna polovica

class Hand:
    """
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    """
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))
        # koliko karata imam u ruci

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        draw_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, draw_card))
        print("\n")
        return draw_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards

    def still_has_cards(self):
        """
        :return: True if player still has cards left
        """
        return len(self.hand.cards) != 0

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Create a new deck an split it in half:
d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()

# Create both players
comp = Player('computer', Hand(half1))
name = input('What is your name? ')
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print('Time for a new round. Here are the current standings')
    print(user.name + ' has the count: ' + str(len(user.hand.cards)))
    print(comp.name + ' has the count: ' + str(len(comp.hand.cards)))
    print('Play a card!')
    print('\n')

    table_cards = []
    c_card = comp.play_card()
    p_card = user.play_card()
    table_cards.append(c_card)
    table_cards.append(p_card)

    # usporedjujem ranking koji se nalazi na indexu 1 izmedju igraca, jer po pravilu igre
    # ako oba imaju istu jacinu karte onda zapocinje war
    if c_card[1] == p_card[1]:
        war_count += 1
        print('War!')
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        # posto je RANKS poredana lista onda mogu usporediti na kojem se indeksu nalazi karta pojedinog igraca
        # i tako odrediti tko ima vecu kartu. U ovom slucaju ako conputer ima manju kartu, igrac dobiva karte
        # u suprotnom dobiva ih computer i ako je izjednaceno isto ih dobiva computer, trebalo bi za ovaj zadnji slucaj
        # osmisliti dodatnu logiku
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:
        # nemam war situaciju pa je dovoljna samo usporedba tko ima koju kartu
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print('Game over, number of rounds: ' + str(total_rounds))
print('A war happened ' + str(war_count) + ' times.')
print('Does the computer still have cards? ' + str(comp.still_has_cards()))
print('Does the human still have cards? ' + str(user.still_has_cards()))
