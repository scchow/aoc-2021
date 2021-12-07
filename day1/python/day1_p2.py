""" day1_p2.py

This file solves the following prompt.

Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window. Again considering the above example:

199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H
Start by comparing the first and second three-measurement windows. 
The measurements in the first window are marked A (199, 200, 208); 
their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. 
The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. 
So, compare A with B, then compare B with C, then C with D, and so on. 
Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:

A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)
In this example, there are 5 sums that are larger than the previous sum.

Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

Solution:

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



    
