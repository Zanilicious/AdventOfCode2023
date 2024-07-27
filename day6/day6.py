"""--- Day 6: Wait For It ---
The ferry quickly brings you across Island Island. After asking around, you discover that there is indeed normally a large pile of sand somewhere near here, but you don't see anything besides lots of water and the small island where the ferry has docked.

As you try to figure out what to do next, you notice a poster on a wall near the ferry dock. "Boat races! Open to the public! Grand prize is an all-expenses-paid trip to Desert Island!" That must be where the sand comes from! Best of all, the boat races are starting in just a few minutes.

You manage to sign up as a competitor in the boat races just in time. The organizer explains that it's not really a traditional race - instead, you will get a fixed amount of time during which your boat has to travel as far as it can, and you win if your boat goes the farthest.

As part of signing up, you get a sheet of paper (your puzzle input) that lists the time allowed for each race and also the best distance ever recorded in that race. To guarantee you win the grand prize, you need to make sure you go farther in each race than the current record holder.

The organizer brings you over to the area where the boat races are held. The boats are much smaller than you expected - they're actually toy boats, each with a big button on top. Holding down the button charges the boat, and releasing the button allows the boat to move. Boats move faster if their button was held longer, but time spent holding the button counts against the total race time. You can only hold the button at the start of the race, and boats don't move until the button is released.

For example:

Time:      7  15   30
Distance:  9  40  200
This document describes three races:

The first race lasts 7 milliseconds. The record distance in this race is 9 millimeters.
The second race lasts 15 milliseconds. The record distance in this race is 40 millimeters.
The third race lasts 30 milliseconds. The record distance in this race is 200 millimeters.
Your toy boat has a starting speed of zero millimeters per millisecond. For each whole millisecond you spend at the beginning of the race holding down the button, the boat's speed increases by one millimeter per millisecond.

So, because the first race lasts 7 milliseconds, you only have a few options:

Don't hold the button at all (that is, hold it for 0 milliseconds) at the start of the race. The boat won't move; it will have traveled 0 millimeters by the end of the race.
Hold the button for 1 millisecond at the start of the race. Then, the boat will travel at a speed of 1 millimeter per millisecond for 6 milliseconds, reaching a total distance traveled of 6 millimeters.
Hold the button for 2 milliseconds, giving the boat a speed of 2 millimeters per millisecond. It will then get 5 milliseconds to move, reaching a total distance of 10 millimeters.
Hold the button for 3 milliseconds. After its remaining 4 milliseconds of travel time, the boat will have gone 12 millimeters.
Hold the button for 4 milliseconds. After its remaining 3 milliseconds of travel time, the boat will have gone 12 millimeters.
Hold the button for 5 milliseconds, causing the boat to travel a total of 10 millimeters.
Hold the button for 6 milliseconds, causing the boat to travel a total of 6 millimeters.
Hold the button for 7 milliseconds. That's the entire duration of the race. You never let go of the button. The boat can't move until you let go of the button. Please make sure you let go of the button so the boat gets to move. 0 millimeters.
Since the current record for this race is 9 millimeters, there are actually 4 different ways you could win: you could hold the button for 2, 3, 4, or 5 milliseconds at the start of the race.

In the second race, you could hold the button for at least 4 milliseconds and at most 11 milliseconds and beat the record, a total of 8 different ways to win.

In the third race, you could hold the button for at least 11 milliseconds and no more than 19 milliseconds and still beat the record, a total of 9 ways you could win.

To see how much margin of error you have, determine the number of ways you can beat the record in each race; in this example, if you multiply these values together, you get 288 (4 * 8 * 9).

Determine the number of ways you could beat the record in each race. What do you get if you multiply these numbers together?"""

# METHODOLOGY
# Read all lines
# Parse lines into lists, one for time and one for distance
# Calculate distance a boat can travel given various charging times, with race record as upper bound
#   For charging times that give a traveled distance > record, store charging time in list

# Functions should be generalized, not specific to four races (as input shows)
#   Allows for example input to be used

# IMPORTS
import re

# DEFINITIONS
RACES = 4

# FUNCTIONS
# Read lines
# Open file, read lines, close file
# Returns all lines from input
def read_lines(filename):
    f = open(filename, "r")

    lines = []
    line = f.readline()
    while line != "":
        lines.append(line)
        line = f.readline()
    
    f.close()

    return lines

# Parse lines
# Reads line, if it starts with time then appends all values to times-list
#   If it starts with distance, appends all values to records-list
def parse_lines(lines):
    race_times = []
    records = []

    for line in lines:
        line = re.split(":|\s+", line)
        
        # If the line contained times, append all values to times-list
        for index in range(1, len(line)):
            if line[index] != "":
                if line[0] == "Time":
                    race_times.append(int(line[index]))
                elif line[0] == "Distance":
                    records.append(int(line[index]))

    return race_times, records

# Calculate travel distance
# Calculates the distance a boat travels for a given charging time
# Speed: x mm/ms == Charging time: x ms
# Distance: x * (time limit - x) mm
# Returns travel distance
def calc_travel_distance(charging_time, race_time):
    speed = charging_time

    travel_distance = speed * (race_time - charging_time)

    return travel_distance

# Compare traveled distance to record
# Compares the calculated traveled distance for a given charging time to the current record for a given race
# If the traveled distance > record, then the charging time is added to a list
# Length of list corresponds to winning options for a specific race
# Returns list with charging times
def find_charging_times(race_time, record):
    charging_times = []

    # Checks all charging times from 1 to one less than the race time
    # If the traveled distance > record, the charging time is added to the list
    for charging_time in range(1, race_time):
        travel_distance = calc_travel_distance(charging_time, race_time)

        if travel_distance > record:
            charging_times.append(charging_time)

    return charging_times

# Find amount of options for a race
# Calculates the amount of charging times in the list to find how many options there are to beat the record
# Returns integer with amount of possible winning options for a race
def find_options(race_index, race_times, records):
    # Set the time and record for a race given the specific race index
    race_time = race_times[race_index]
    record = records[race_index]

    # Find all charging times that give a further traveled distance than the record
    charging_times = find_charging_times(race_time, record)

    # Calculate the amount of winning options from the charging times
    winning_options = len(charging_times)

    return winning_options

# Main 
# Main function with all global variables and functions running
# Finds the winning options for each race, multiplies and prints the product of all possible options
def main():
    total_winning_options = 1

    # Read the file and save the lines
    lines = read_lines("input")
    
    # Parse the lines into a list for the race times and one for the race records
    race_times, records = parse_lines(lines)

    # Go through all the races, find the winning options for each, multiply and add to the global var
    for race_index in range(RACES):
        winning_options = find_options(race_index, race_times, records)

        total_winning_options *= winning_options

    print("The product of all winning options is:", total_winning_options)

main()