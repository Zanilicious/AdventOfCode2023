"""
--- Day 7: Camel Cards ---
Your all-expenses-paid trip turns out to be a one-way, five-minute ride in an airship. (At least it's a cool airship!) It drops you off at the edge of a vast desert and descends back to Island Island.

"Did you bring the parts?"

You turn around to see an Elf completely covered in white clothing, wearing goggles, and riding a large camel.

"Did you bring the parts?" she asks again, louder this time. You aren't sure what parts she's looking for; you're here to figure out why the sand stopped.

"The parts! For the sand, yes! Come with me; I will show you." She beckons you onto the camel.

After riding a bit across the sands of Desert Island, you can see what look like very large rocks covering half of the horizon. The Elf explains that the rocks are all along the part of Desert Island that is directly above Island Island, making it hard to even get there. Normally, they use big machines to move the rocks and filter the sand, but the machines have broken down because Desert Island recently stopped receiving the parts they need to fix the machines.

You've already assumed it'll be your job to figure out why the parts stopped when she asks if you can help. You agree automatically.

Because the journey will take a few days, she offers to teach you the game of Camel Cards. Camel Cards is sort of similar to poker except it's designed to be easier to play while riding a camel.

In Camel Cards, you get a list of hands, and your goal is to order them based on the strength of each hand. A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. The relative strength of each card follows this order, where A is the highest and 2 is the lowest.

Every hand is exactly one type. From strongest to weakest, they are:

Five of a kind, where all five cards have the same label: AAAAA
Four of a kind, where four cards have the same label and one card has a different label: AA8AA
Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
High card, where all cards' labels are distinct: 23456
Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.

If two hands have the same type, a second ordering rule takes effect. Start by comparing the first card in each hand. If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each hand have the same label, however, then move on to considering the second card in each hand. If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.

So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger because its first card is stronger. Similarly, 77888 and 77788 are both a full house, but 77888 is stronger because its third card is stronger (and both hands have the same first and second card).

To play Camel Cards, you are given a list of hands and their corresponding bid (your puzzle input). For example:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
This example shows five hands; each hand is followed by its bid amount. Each hand wins an amount equal to its bid multiplied by its rank, where the weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the strongest hand. Because there are five hands in this example, the strongest hand will have rank 5 and its bid will be multiplied by 5.

So, the first step is to put the hands in order of strength:

32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.
T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.
Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with its rank (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5). So the total winnings in this example are 6440.

Find the rank of every hand in your set. What are the total winnings?
"""
# Game: Camel Cards
# Receive list of hands
# Hand: 5 cards
# Strength of cards: A --> 2
# Types: Five of a Kind, Four of a Kind, Full House, Three of a Kind, Two Pair, One Pair, High Card

# Game rules:
# Give order of hands based on types
# If two hands share a type, compare cards in left-to-right order
# Each hand has a bid
# A rank is the position of the hand, when all hands are sorted
# The winnings = bid * rank

# Challenge: Find the sum of all winnings
# My input: 1000 lines

# METHODOLOGY
# 

# DEFINITIONS
RANK_FIVE_OF_A_KIND = 1
RANK_FOUR_OF_A_KIND = 2
RANK_FULL_HOUSE = 3
RANK_THREE_OF_A_KIND = 4
RANK_TWO_PAIR = 5
RANK_ONE_PAIR = 6
RANK_HIGH_CARD = 7
STRENGTH_ORDER = {"A": 0,
                  "K": 1,
                  "Q": 2,
                  "J": 3,
                  "T": 4,
                  "9": 5,
                  "8": 6,
                  "7": 7,
                  "6": 8,
                  "5": 9,
                  "4": 10,
                  "3": 11,
                  "2": 12
                  } # Used for sorting based on cards

# FUNCTIONS
# Parse a line and return a list
# Input: str
# Output: list
def parse_line(line):
    # Split into hand and bid
    line = line.split(" ")

    # Remove newline char at end
    if "\n" in line[1]:
        line[1], _ = line[1].split("\n")

    # Bid from str to int
    line[1] = int(line[1])

    return line

# Read the file
# Input: str
# Output: list
def read_file(filename):
    f = open(filename, "r")
    lines = []

    line = f.readline()
    while line != "":
        line = parse_line(line)
        lines.append(line)
        line = f.readline()
    
    f.close()

    return lines

# Determines the type
# Input: str
# Output: int (Constant)
def determine_type(hand):
    count = 0

    # Check the largest amount of same cards in the set
    for card in hand:
        if hand.count(card) > count: count = hand.count(card)
    
    if count == 0:
        print("Error in determine_type(), count: 0")
    elif count == 1:
        return RANK_HIGH_CARD # All cards are unidentical
    elif count == 2:
        # Check how many pairs there are
        pairs = 0
        for card in hand:
            if hand.count(card) == 2: pairs += 0.5

        if pairs == 1: return RANK_ONE_PAIR # Only one pair found
        elif pairs == 2: return RANK_TWO_PAIR # Two pairs found
    elif count == 3:
        # Determine the last two cards
        for card in hand:
            if hand.count(card) == 2: return RANK_FULL_HOUSE # Last two cards are a pair
        return RANK_THREE_OF_A_KIND # Last two cards are different 
    elif count == 4:
        return RANK_FOUR_OF_A_KIND # Four cards are matching
    elif count == 5:
        return RANK_FIVE_OF_A_KIND # All five cards are matching
    else:
        print("Error in determine_type(), count not in [0-5]")

# Assigns the type to the hand
# Input: list
# Output: list
def assign_type(game):
    # Determine the type of the game
    rank_type = determine_type(game[0])

    # Append the rank to the 
    game.append(rank_type)

    return game

# Sort the cards, based on type
# Input: list
# Output: list
def sort_cards_on_type(games):
    # Append the type rank to the list
    for index, game in enumerate(games):
        game = assign_type(game)
        games[index] = game

    # Sort the games based on the type rank
    games = sorted(games, key = lambda x: x[2])

    return games

# Return shorter list of sorted games
# Input: list
# Output: list
def custom_sort_cards(single_type: list) -> list:
    sorted_single_type = sorted(single_type, key = lambda d: STRENGTH_ORDER[d[2]])

    return sorted_single_type

# Sort the cards, based on card strength
# Input: list
# Output: list
def sort_cards_on_strength(games):
    single_type = []
    new_games = []

    for game in games:
        if (single_type == []): single_type.append(game) # First run for new type

        if (game[2] == single_type[-1][2]): # If current game type matches previous game types
            single_type.append(game)
        else:
            sorted_single_type = custom_sort_cards(single_type)
            new_games.append(sorted_single_type)
            single_type = []

    return games



lines = read_file("input")

games = sort_cards_on_type(lines)

single_type = games[1:96]

sorted_single_type = custom_sort_cards(single_type)

