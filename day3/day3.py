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

# IMPORTS

# FUNCTION 
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

# 
def 

# MAIN
def main():
    # Var : Sum of all numbers (w/ symbol close to it)
    sum = 0

    # Load file
    file = load_file("input")

    # Load all lines
    # Eventually insert into a while-loop
    lines = load_lines(file)

    # Close file following loading of lines
    close_file(file)

    # Store positions of symbols for last three lines into 2D-array
    positions = store_sym_pos(lines)
    
# TEST BED

# Load the file, load all lines into array
file = load_file("input")
lines = load_lines(file)

# Get position for all symbols into 2D array
symbol_pos = return_symbol_pos(lines)

# Get position of all numbers in array containing dictionaries for each line
number_pos = return_number_pos(lines)



close_file(file)