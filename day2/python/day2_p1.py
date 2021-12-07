""" day2_p1.py

Solution to Day 2 Part 1 Puzzle.

Our approach:

The main challenge of this is actually parsing the data file.
We parse the file into tuples of directions.
Then its simply a matter of iterating through the tuples and applying
the appropriate action to the submarine's state

Usage:

```
$ python day2_p1.py ../data/input.txt
Final Horizontal Position:
Final Vertical Position:
Multiplied Position:
```

"""

import sys

def read_input(filename: str) -> list:
    """ Reads the input from filename

    Args:
        filename (str): The path to the input file
    
    Returns:
        A list of ints: The list of integers read into the file
    """
    
    with open(filename) as f:
        return f.readlines()

def parse_commands(l: list) -> list:
    """ Converts a list of commands to a list of 
    (direction, units) tuples (i.e., ("up", 3))

    Args:
        l (list): List of strings
    
    Returns:
        List of command tuples
    """
    # Split each line by spaces
    commands = [cmd.split(" ") for cmd in l]

    # Convert second argument in each line to int
    for i in range(len(commands)):
        commands[i][1] = int(commands[i][1])
    
    return commands

def execute_commands(commands: list):
    """ Execute a list of command tuples (direction, units)
    on a vehicle

    Args:
        l (list): List of command tuples

    Returns:
        List [horizontal, vertical]: final horizontal and vertical position of vehicle
    """

    # vehicle state represented as a list: [horizontal position, vertical position]
    state = [0, 0]

    for direction, units in commands:
        if direction == "forward":
            state[0] += units
        if direction == "up":
            state[1] -= units
        if direction == "down":
            state[1] += units
    
    return state

if __name__ == "__main__":

    filename = str(sys.argv[1])

    commands_raw = read_input(filename)

    commands = parse_commands(commands_raw)

    horizontal, vertical = execute_commands(commands)

    print(f'Final Horizontal Position: {horizontal}')
    print(f'Final Vertical Position: {vertical}')
    print(f'Multiplied Position: {horizontal*vertical}')




    
