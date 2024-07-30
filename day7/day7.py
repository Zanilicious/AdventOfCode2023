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
# Open file, load lines into list (1: Cards, 2: bid), close file
# Assign type to every hand and put in list (3: Type)
# First sorting: Sort all hands based on type
# Second sorting: Sort all hands based on card strengths (Assume no hand duplicates)
# Create list with all ranks
# Create list with all winnings, using ranks-list and bids from hands-list
# Print the sum of the winnings

# DEFINITIONS
# Ranks
RANK_FIVE_KIND = 7
RANK_FOUR_KIND = 6
RANK_FULL_HOUSE = 5
RANK_THREE_KIND = 4
RANK_TWO_PAIR = 3
RANK_ONE_PAIR = 2
RANK_HIGH_CARD = 1
# Card types
FIVE_KIND = 5
FOUR_KIND = 4
FULL_OR_THREE = 3
TWO_OR_ONE_PAIR = 2
HIGH_CARD = 1
# Order to use for sorting cards
SORT_ORDER = {"A" : 0,
              "K" : 1,
              "Q" : 2,
              "J" : 3,
              "T" : 4,
              "9" : 5,
              "8" : 6,
              "7" : 7,
              "6" : 8,
              "5" : 9,
              "4" : 10,
              "3" : 11,
              "2" : 12,
              }

# FUNCTIONS
# Helper: Parse line into list
# Input: str: line from file
# Returns: list: [Hand, Bid]
def parse_line(line):
    game = []

    game = line.split(" ")

    game[1] = int(game[1])

    return game

# File open, load hands-list, close file
# Input: filename
# Returns: list [[Hand, Bid], [Hand, Bid],...]
def load_file(filename):
    games = []

    f = open(filename, "r")

    line = f.readline()
    while line != "":
        game = parse_line(line)
        games.append(game)
        line = f.readline()

    f.close()

    return games

# Helper: Finds the type of a hand 
# Input: Str: Hand
# Returns: Str: Type
def find_type(hand: str) -> str:
    max_amount = 0

    for card in hand:
        if (hand.count(card) > max_amount): max_amount = hand.count(card)
    
    if max_amount == HIGH_CARD:
        hand_type = RANK_HIGH_CARD
    elif max_amount == TWO_OR_ONE_PAIR:
        hand_count = 0
        for card in hand:
            if hand.count(card) == 2: hand_count += 1
            if hand_count == 2: hand_type = RANK_ONE_PAIR
            elif hand_count == 4: hand_type = RANK_TWO_PAIR
    elif max_amount == FULL_OR_THREE:
        for card in hand:
            if hand.count(card) == 2:
                hand_type = RANK_FULL_HOUSE
                break
            hand_type = RANK_THREE_KIND
    elif max_amount == FOUR_KIND:
        hand_type = RANK_FOUR_KIND
    elif max_amount == FIVE_KIND:
        hand_type = RANK_FIVE_KIND
    else:
        print("Error in find_type()")

    return hand_type

# Assigns type to hand
# Uses helper function, appends the type from the return value to the list
# Input: list [Hand, Bid]
# Returns: list [Hand, Bid, Type]
def assign_type(game: list) -> list:
    hand_type = find_type(game[0])

    game.append(hand_type)

    return game

# Sort on type
# Use the definitions of the types to sort all hands based on their types
# Input: list [[Hand, Bid, Type], [Hand, Bid, Type]...]
# Returns: list [[Hand, Bid, Type], [Hand, Bid, Type]...]
def sort_on_type(games: list) -> list:
    # Sorts the all the games using the type
    games.sort(key = lambda x: x[2])

    # Reverses the list to ensure FoaK first, HC last
    games.reverse()

    return games

# Sort on hand
# Compares the cards from two hands that are neighbours in the list to find if they need to be replaced
# Input: list [[Hand, Bid, Type], [Hand, Bid, Type]...]
# Returns: list [[Hand, Bid, Type], [Hand, Bid, Type]...]
def sort_on_hand(games: list) -> list:
    type_indices = []
    cur_type = 0

    # Gives indices for all new types
    for game_index, game in enumerate(games):
        if game[2] != cur_type: 
            cur_type = game[2]
            type_indices.append(game_index)
    type_indices.append(len(games) - 1)

    print(type_indices)
    
    # Sort part of the list
    for index in range(len(type_indices)):
        if index < len(games): 
            temp_list = games[type_indices[index]:type_indices[index+1]]
            print(temp_list)
        
            # Sort based on our custom sort order
            temp_list.sort(key = lambda val: SORT_ORDER[val[1]])

            games.append(temp_list)
    
    # Remove original set of games
    for _ in range(type_indices[-1] + 1):
        games.pop(0)

    return games
    

# Create ranks-list
# Creates a list of all the ranks, from 1 to len(hands-list)
# Input: list [[Hand, Bid], [Hand, Bid]...]
# Returns: list [len(hands-list), ..., 3, 2, 1]

# Create winnings-list
# Creates a list with the winnings from each hand
# Requires the hands to be sorted
# Input: list [[Hand, Bid, Type], [Hand, Bid, Type]...] , list [len(hands-list), ..., 3, 2, 1]
# Returns: int: sum of winnings

def main():
    winnings_sum = 0

    # Load the lines from input file
    games = load_file("input")
    
    # Assign types to each game
    # A game consists of the hand and the bid
    for game in games:
        game = assign_type(game)
    
    # Sort the games based on their type
    games = sort_on_type(games)

    # Sort the games further based on their cards
    # Only sorts within the type domain
    games = sort_on_hand(games)









    
    print("The sum of winnings from part 1 is:", winnings_sum)

main()