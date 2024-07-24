"""--- Day 4: Scratchcards ---
The gondola takes you up. Strangely, though, the ground doesn't seem to be coming with you; you're not climbing a mountain. As the circle of Snow Island recedes below you, an entire new landmass suddenly appears above you! The gondola carries you to the surface of the new island and lurches into the station.

As you exit the gondola, the first thing you notice is that the air here is much warmer than it was on Snow Island. It's also quite humid. Is this where the water source is?

The next thing you notice is an Elf sitting on the floor across the station in what seems to be a pile of colorful square cards.

"Oh! Hello!" The Elf excitedly runs over to you. "How may I be of service?" You ask about water sources.

"I'm not sure; I just operate the gondola lift. That does sound like something we'd have, though - this is Island Island, after all! I bet the gardener would know. He's on a different island, though - er, the small kind surrounded by water, not the floating kind. We really need to come up with a better naming scheme. Tell you what: if you can help me with something quick, I'll let you borrow my boat and you can go visit the gardener. I got all these scratchcards as a gift, but I can't figure out what I've won."

The Elf leads you over to the pile of colorful cards. There, you discover dozens of scratchcards, all with their opaque covering already scratched off. Picking one up, it looks like each card has two lists of numbers separated by a vertical bar (|): a list of winning numbers and then a list of numbers you have. You organize the information into a table (your puzzle input).

As far as the Elf has been able to figure out, you have to figure out which of the numbers you have appear in the list of winning numbers. The first match makes the card worth one point and each match after the first doubles the point value of that card.

For example:

Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17) and eight numbers you have (83, 86, 6, 31, 17, 9, 48, and 53). Of the numbers you have, four of them (48, 83, 17, and 86) are winning numbers! That means card 1 is worth 8 points (1 for the first match, then doubled three times for each of the three matches after the first).

Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
Card 4 has one winning number (84), so it is worth 1 point.
Card 5 has no winning numbers, so it is worth no points.
Card 6 has no winning numbers, so it is worth no points.
So, in this example, the Elf's pile of scratchcards is worth 13 points.

Take a seat in the large pile of colorful cards. How many points are they worth in total?
--- Part Two ---
Just as you're about to report your findings to the Elf, one of you realizes that the rules have actually been printed on the back of every card this whole time.

There's no such thing as "points". Instead, scratchcards only cause you to win more scratchcards equal to the number of winning numbers you have.

Specifically, you win copies of the scratchcards below the winning card equal to the number of matches. So, if card 10 were to have 5 matching numbers, you would win one copy each of cards 11, 12, 13, 14, and 15.

Copies of scratchcards are scored like normal scratchcards and have the same card number as the card they copied. So, if you win a copy of card 10 and it has 5 matching numbers, it would then win a copy of the same cards that the original card 10 won: cards 11, 12, 13, 14, and 15. This process repeats until none of the copies cause you to win any more cards. (Cards will never make you copy a card past the end of the table.)

This time, the above example goes differently:

Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
Your copy of card 2 also wins one copy each of cards 3 and 4.
Your four instances of card 3 (one original and three copies) have two matching numbers, so you win four copies each of cards 4 and 5.
Your eight instances of card 4 (one original and seven copies) have one matching number, so you win eight copies of card 5.
Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers and win no more cards.
Your one instance of card 6 (one original) has no matching numbers and wins no more cards.
Once all of the originals and copies have been processed, you end up with 1 instance of card 1, 2 instances of card 2, 4 instances of card 3, 8 instances of card 4, 14 instances of card 5, and 1 instance of card 6. In total, this example pile of scratchcards causes you to ultimately have 30 scratchcards!

Process all of the original and copied scratchcards until no more scratchcards are won. Including the original set of scratchcards, how many total scratchcards do you end up with?
"""
# METHOD
# Open file, load all lines --> list, close file
# Loop through all lines
# For each line, separate into two lists: One with winning numbers, one with my numbers
# Loop through my numbers and check if they are winning numbers - apply formula to card sum if true
# Formula: if sum 0, set to 1 - if sum > 0, sum * 2
# Add each card sum to a global sum
# Print sum

# METHOD PART 2
# First pass calculates score for all unique cards, store in list
# One list with all cards, iteratively increment all cards following using score-list

# IMPORTS
# Helps in splitting process
import re
# Helps in copying dict
import copy

# DEFINITIONS

# FUNCTIONS
# Load file
# Return file
def load_file(filename):
    f = open(filename, "r")

    return f

# Load all lines from file into a list
# Return list
def load_lines(file):
    lines = []

    line = file.readline()
    while (line != ""):
        lines.append(line)
        line = file.readline()

    return lines

# Close file
def close_file(file):
    file.close()

# Helper function
# Split a line into only words ("Card") and numbers
def split_line(line):
    line = re.split(":|\||\n", line)
    # Removes empty char at end of list
    if line[2] == "":
        line.pop()

    # Handle card ID
    card_id = ""
    for i in line[0]:
        if i in "0123456789":
            card_id += i

    # Handle winning numbers
    winning_numbers = []
    for i in line[1].split(" "):
        if i != "":
            winning_numbers.append(i)
    
    # Handle my numbers
    my_numbers = []
    for i in line[2].split(" "):
        if i != "":
            my_numbers.append(i)
            
    temp_dict = {"id" : card_id,
                 "winning_numbers" : winning_numbers,
                 "my_numbers" : my_numbers}
    
    return temp_dict
    

# Parse lines into list that contains dictionaries
# Keys: 
#   card_id
#   winning_numbers
#   my_numbers
# Values:
#   int: Card ID
#   List: Winning numbers
#   List: My numbers
# Returns list with dictionaries 
def parse_lines(lines):
    dict_list = []
    
    # Loop through all lines (which were loaded from input file)
    for line in lines:
        temp_dict = split_line(line)
        dict_list.append(temp_dict)
        
    return dict_list

# Helper function
# Calculate score based on how many of my numbers can be found in the winning numbers
# Follows formula as outlined in text
def calc_score(dictionary):
    score = 0

    for i in dictionary["my_numbers"]:
        if i in dictionary["winning_numbers"]:
            if score == 0:
                score += 1
            else:
                score *= 2
    
    return score

# Calculates the total score
def total_score(dict_list):
    total_score = 0

    for dict in dict_list:
        total_score += calc_score(dict)

    return total_score


# Consider only finding the "score" for each unique card, then multiplying with an array of amount of cards
# For each entry, it will automatically multiply the next amounts as well


# Creates the list which contains the amount of cards for each ID
# Initially only one card per ID
# Element position + 1 == card ID
# Returns list
def create_card_list(dict_list):
    card_list = []

    for _ in dict_list:
        card_list.append(1)

    return card_list


# Create a list with every card's scores
# Returns list
def create_score_list(dict_list):
    score_list = []

    for dict in dict_list:
        score = calc_score(dict)
        score_list.append(score)

    return score_list

# TOUGH
# Adds copies to cards below current card, based on the score
# Returns card_list
def recalc_cards(card_list, score_list):
    for index in range(len(card_list)):
        if score_list[index] > (len(card_list) - index):
            for inc in range(index + 1, len(card_list)):
                card_list[inc] += 1
        else:
            for inc in range(index + 1, score_list[index]):
                card_list[inc] += 1

    return card_list



# MAIN
def main():
    f = load_file("input")

    lines = load_lines(f)

    close_file(f)

    dict_list = parse_lines(lines)
    
    score = total_score(dict_list)

    print("Score (pt1):", score)

    card_list = create_card_list(dict_list)

    score_list = create_score_list(dict_list)

    card_list = recalc_cards(card_list, score_list)

    print(card_list)






main()
