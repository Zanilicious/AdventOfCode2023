"""
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""

# Need to figure out numbers exactly 1 d.u. (distance unit) away from a symbol

# There are numbers, periods, and other symbols
# Symbols can be treated as anything != periods | numbers

# Exactly 140 characters per line (+1 \n for all but last line)
# 140 lines

# Method : Scanning 3 lines at a time
# Possible to check in all directions
# First pass, store all symbols position (array with 2d?)
# Second pass, for each encountered number, peek around it in all directions to see if symbol has been stored
# If found, add number to global array
# At the end of a run, sum all numbers in global array

# FUNCTIONS
# Open and read file
# Close file
# Load 3 lines at a time
# Store all symbols' positions of current 3 lines
# Check if number has symbol around it, sum number into global var if true

# DEFINITIONS
GEAR = "*"

# FUNCTIONS
# Load the file
def load_file(filename):
    f = open(filename, "r")

    return f

# Close the file
def close_file(file):
    file.close()

# Load all lines from input file into array
def load_lines(file):
    lines = []

    line = file.readline()
    while (line != ""):
        # Remove \n at end of line
        if "\n" in line:
            line = line[0:-1]
        lines.append(line)

        line = file.readline()

    return lines

# Store all symbols' positions in a 2D array
# Inner array tells which line the symbol was found on, the value in the inner array tells which position the symbol was on
def return_symbol_pos(lines):
    # List comprehension
    # Using multiplication "[[]] * 10" will result in 10 inner lists that are the same object - incorrect for our situation!
    symbol_pos = [[] for _ in range(0, len(lines))]

    # If the element in a line is a symbol, add the position of that element to the inner list whose position correspond to the line position
    for line_count, line in enumerate(lines):
        for char_count, char in enumerate(line):
            if char not in ".0123456789":
                symbol_pos[line_count].append(char_count)

    return symbol_pos

# Helper function reads and returns the number when encountering a digit during scanning of line
def read_num(line, char_count):
    digits = ""

    # Go through all digits in sequence and combine them
    while (line[char_count] in "0123456789"):
        digits = digits + line[char_count]
        if char_count < 139:
            char_count += 1
        else:
            break

    # Convert the num from str to int
    try:
        num = int(digits)
    except:
        "read_num() incorrect input"

    return num

# Store all numbers' positions
# Level 1 array, element correspond to line position
# Dict / line, key corresponds to initial char position, val corresponds to number
def return_number_pos(lines):
    # Level-1 array
    number_pos = []
    # Used to not add redundant digits when encountering them once
    recent_num = 0

    # On digit encounter, add number to dict
    # On newline, append dict to array
    # Process all lines in this manner
    for line_count, line in enumerate(lines):
        dictionary = {}
        recent_num = 0

        for char_count, char in enumerate(line):
            if char in "0123456789" and recent_num <= 0:
                num = read_num(line, char_count)
                dictionary[char_count] = num
                # The length of the number is the amount of digits the function will skip
                recent_num = len(str(num))
            recent_num -= 1
        # Once a line is read, the dict is filled with all num from that line and thus added to the L1 array
        number_pos.append(dictionary)

    return number_pos

# Helper function, takes dict key and val
# Returns array with all indices to look for symbol
# Return all the indices which should be searched for symbols
# All indices searched in upper and lower lines, only edge indices searched in the same line
def get_search_indices(key, num):
    search_indices = []

    # Len of num
    num_len = len(str(num))

    temp_key = key
    # Starting index at one step "left" of value
    if key > 0:
        temp_key -= 1
    
    if key > 0:
        for i in range(temp_key, temp_key+num_len+2):
            search_indices.append(i)
    else:
        for i in range(temp_key, temp_key+num_len+1):
            search_indices.append(i)

    return search_indices

# Finds if a number is a "part number"
# Returns 0 if not, otherwise returns the number
# pt2: Everytime a part_number is found, it is checked if it is a gear
# If true, then the "gear's" position ("line:index") is added as a key to a dictionary
# The current number is added as a value
# If a new number is found connected to the gear, it will check if the dict contains a part number for the given key, if true then the numbers are mult and added to a global sum
def get_part_number(dictionary, key, line_index, symbol_pos, lines):
    part_number = 0
    gear_dict = {}
    gear_ratios = 0

    number = dictionary[key]
    # Returns all the indices +1 in each direction, which the number covers
    search_indices = get_search_indices(key, number)

    # If it's the first line, only check edges of line_index and all indices of line below
    if line_index == 0:
        for index in search_indices:
            if index in (symbol_pos[line_index] or symbol_pos[line_index+1]):
                part_number = number
                # Adding the gear to the gear dict
                if lines[line_index][index] == GEAR:
                    key = str(line_index) + ":" + str(index)
                elif lines[line_index+1][index] == GEAR:
                    key = str(line_index+1) + ":" + str(index)

                # If true, then there already is a value in the dict
                if key in gear_dict.keys():
                    gear_ratios += number * gear_dict[key]
                else:
                    gear_dict[key] = number
        
    # If it's the last line, only check edges of line_index and all indices of line above
    elif line_index == len(symbol_pos)-1:
        for index in search_indices:
            if index in (symbol_pos[line_index-1] or symbol_pos[line_index]):
                part_number = number
                # Adding the gear to the gear dict
                if lines[line_index][index] == GEAR:
                    key = str(line_index) + ":" + str(index)
                elif lines[line_index-1][index] == GEAR:
                    key = str(line_index+1) + ":" + str(index)

                # If true, then there already is a value in the dict
                if key in gear_dict.keys():
                    gear_ratios += number * gear_dict[key]
                else:
                    gear_dict[key] = number

    # Otherwise, check all indices in lines above and below as well as edges of line_index
    else:
        for index in search_indices:
            if index in symbol_pos[line_index-1] or index in symbol_pos[line_index] or index in symbol_pos[line_index+1]:
                part_number = number
                # Adding the gear to the gear dict
                if lines[line_index][index] == GEAR:
                    key = str(line_index) + ":" + str(index)
                elif lines[line_index+1][index] == GEAR:
                    key = str(line_index+1) + ":" + str(index)
                elif lines[line_index-1][index] == GEAR:
                    key = str(line_index+1) + ":" + str(index)

                # If true, then there already is a value in the dict
                if key in gear_dict.keys():
                    gear_ratios += number * gear_dict[key]
                else:
                    gear_dict[key] = number

    return part_number, gear_ratios

# MAIN
def main():
    # Var : Sum of all numbers (w/ symbol close to it)
    sum = 0

    # Var : Sum of all gear ratios
    gear_ratio_sum = 0

    # Load file
    file = load_file("input")

    # Load all lines
    # Eventually insert into a while-loop
    lines = load_lines(file)

    # Close file following loading of lines
    close_file(file)

    # Get position for all symbols into 2D array
    symbol_pos = return_symbol_pos(lines)

    # Get position of all numbers in array containing dictionaries for each line
    number_pos = return_number_pos(lines)

    # Go through all numbers and add to sum if it's a part number
    for line_index, dictionary in enumerate(number_pos):
        for key in dictionary:
            part_number, gear_ratios = get_part_number(dictionary, key, line_index, symbol_pos, lines)
            sum += part_number
            gear_ratio_sum += gear_ratios
    
    print("The sum of all part numbers is:", sum)
    print("The sum of all gear ratios is:", gear_ratio_sum)


main()

# Answer input_5: 16073