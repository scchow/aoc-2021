""" day1_p2.py

Solution to Day 1 Part 2 Puzzle.

Our approach:

This prompt is actually asking us to perform a convolution on the input. 
We can implement this manually or use numpy's convolution to solve this.
We provide both solutions below.


Usage:

```
$ python day1_p2.py ../data/input.txt
Number of 3 moving window measurement increases (w/o numpy): 1457
Number of 3 moving window measurement increases (w/numpy): 1457
```

"""

import sys
import numpy as np
from day1_p1 import read_input, find_increases

def compute_sliding_window_np(l: list, window_size: int=3) -> list:
    """ Computes the sliding window using numpy

    Args:
        l (list): List of integers
        window_size (int): number of integers in a window
    
    Returns:
        List of sums of every `window_size` windows.
    """
    return list(np.convolve(l, [1,1,1], mode='valid'))

def compute_sliding_window(l: list, window_size: int=3) -> list:
    """ Computes the sliding window without numpy

    Args:
        l (list): List of integers
        window_size (int): number of integers in a window
    
    Returns:
        List of sums of every `window_size` windows.
    """

    windows = []

    ending_index = len(l) - window_size

    for i in range(ending_index+1):
        windows.append(sum(l[i:i+window_size]))

    return windows

if __name__ == "__main__":

    filename = str(sys.argv[1])

    measurements = read_input(filename)

    windows_np = compute_sliding_window_np(measurements)
    windows = compute_sliding_window(measurements)

    increases_np = find_increases(windows_np)
    increases = find_increases(windows)  

    print(f'Number of 3 moving window measurement increases (w/o numpy): {increases}')
    print(f'Number of 3 moving window measurement increases (w/numpy): {increases_np}')



    
