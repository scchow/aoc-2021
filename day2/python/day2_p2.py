""" day2_p2.py

Solution to Day 2 Part 2 Puzzle.

Our approach:

We follow almost the same approach, except we need to handle commands
a bit differently as described in the prompt.

Usage:

```
$ python day2_p2.py ../data/input.txt
Final Horizontal Position: 1823
Final Vertical Position: 1012318
Multiplied Position: 1845455714
```

"""

import sys
from day2_p1 import read_input, parse_commands

def execute_commands(commands: list):
    """ Execute a list of command tuples (direction, units)
    on a vehicle

    Args:
        l (list): List of command tuples

    Returns:
        List [horizontal, vertical]: final horizontal and vertical position of vehicle
    """

    # vehicle state represented as a list: [horizontal position, vertical position, aim]
    state = [0, 0, 0]

    for direction, units in commands:
        if direction == "forward":
            state[0] += units
            state[1] += units * state[2]
        if direction == "up":
            state[2] -= units
        if direction == "down":
            state[2] += units
    
    return state[0:2]

if __name__ == "__main__":

    filename = str(sys.argv[1])

    commands_raw = read_input(filename)

    commands = parse_commands(commands_raw)

    horizontal, vertical = execute_commands(commands)

    print(f'Final Horizontal Position: {horizontal}')
    print(f'Final Vertical Position: {vertical}')
    print(f'Multiplied Position: {horizontal*vertical}')




    
