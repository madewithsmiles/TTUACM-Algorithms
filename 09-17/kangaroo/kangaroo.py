#!/bin/python3

import math
import os
import random
import re
import sys

'''
Complete the kangaroo function below.
The kangaroos will meet if there exists an integer j such that j = (x1 - x2) / (v2 - v1).
This equation is derived from the following:
We know that the position of any given kangaroo can be represented by the formula x = x0 + v0j where x is their current position,
x0 is their initial position, v0 is their meters per jump, and j is the amount of jumps they have made
Since we want to know if the two kangaroos will meet up, we want to know if there exists an amount of jumps j such that the distance x
for each kangaroo equals
x1 + v1j = x2 + v2j
x1 - x2 = v2j - v1j
x1 - x2 = j(v2 - v1)
(x1 - x2) / (v2 - v1) = j
'''
def kangaroo(x1, v1, x2, v2):
    velDiff = v2 - v1
    posDiff = x1 - x2
    # If you divide by 0 then j is undefined
    if velDiff != 0:
        # If j is a positive integer (no negative or partial jumps)
        if posDiff % velDiff == 0 and posDiff / velDiff > 0:
            return 'YES'
    # Otherwise there is no j that satisfies our conditions
    return 'NO'
