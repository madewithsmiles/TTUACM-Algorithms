#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    
    # Take d % n because a shift of 6 to the left on an array of length 5 is the same as a shift
    # of 1 to the left because a shift 5 to the left is the same array, then add 1 more shift
    d = d % n
    
    # Pop off the front element and append to back d times
    while d > 0:
        a += [a[0]]
        del a[0]
        d -= 1
    
    print(' '.join(map(str, a)))
