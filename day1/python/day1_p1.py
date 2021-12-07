""" day1_p1.py

This file solves the following prompt.

As the submarine drops below the surface of the ocean, 
it automatically performs a sonar sweep of the nearby sea floor. 
On a small screen, the sonar sweep report (your puzzle input) appears: 
each line is a measurement of the sea floor depth as the sweep looks 
further and further away from the submarine.

For example, suppose you had the following report:

199
200
208
210
200
207
240
269
260
263
This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 199, 200, 208, 210, and so on.

The first order of business is to figure out how quickly the depth increases, 
just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

To do this, count the number of times a depth measurement increases from the previous measurement. 
(There is no measurement before the first measurement.) In the example above, the changes are as follows:

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
In this example, there are 7 measurements that are larger than the previous measurement.

How many measurements are larger than the previous measurement?

Solution:
We start with a read_input() function to read the list of integers from the file
We then iterate through the list using find_increase(), counting the number of times they increase/

This could technically be done in a single function/for loop, by doing the counting while
reading the file line by line using `readline()`.

Usage:

```
$ python day1_p1.py ../data/input.txt
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

    


    
