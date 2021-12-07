""" day1_p1.py

Solution to Day 1 Part 1 Puzzle.

Our approach:

We start with a read_input() function to read the list of integers from the file
We then iterate through the list using find_increase(), counting the number of times they increase/

This could technically be done in a single function/for loop, by doing the counting while
reading the file line by line using `readline()`.

Usage:

```
$ python p1.py ../data/input.txt
Number of measurement increases: 1390
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
        raw_output = f.readlines()
    
    return list(map(int, raw_output))

def find_increases(l: list) -> int:
    """ Counts the number of measurement increases in a list

    Args:
        l (list): List of integers
    
    Returns:
        The number of times the measurment increases as an int.
    """

    increases = 0

    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            increases += 1
    
    return increases

if __name__ == "__main__":

    filename = str(sys.argv[1])

    measurements = read_input(filename)

    increases = find_increases(measurements)

    print(f'Number of measurement increases: {increases}')

    


    
