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

# Imports

# Functions
# Load the file
def load_file(filename):
    f = open(filename, "r")

    return f

# Close the file
def close_file(file):
    file.close()

# Load three lines into array
def load_lines(file):
    lines = []

    for i in range(0, 3):
        line = file.readline()
        # Remove \n at end of line
        if "\n" in line:
            line = line[0:-1]
        lines.append(line)

    return lines

# Store all symbols' positions in latest three lines in a 2D-array
def store_sym_pos(lines):
    positions = [[],
                 [],
                 []]
    
    for line_count, line in enumerate(lines):
        for char_count, char in enumerate(line):
            if char not in ".0123456789":
                positions[line_count].append(char_count)


    return positions



# Main
def main():
    # Var : Sum of all numbers (w/ symbol close to it)
    sum = 0

    # Load file
    file = load_file("input")

    # Load three lines 
    # Eventually insert into a while-loop
    lines = load_lines(file)

    # Store positions of symbols for last three lines into 2D-array
    positions = store_sym_pos(lines)
    



    # Close file prior to program termination
    close_file(file)

file = load_file("input")
lines = load_lines(file)
#for i in lines:
#    print(i)

positions = store_sym_pos(lines)
#print(positions)
#for j in positions[1]:
#    print(lines[1][j])

close_file(file)