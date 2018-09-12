#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.

def minute_to_string(minute):

    minute = str(minute)

    num_as_string = {
        '0' : '',
        '1' : 'one', 
        '2' : 'two', 
        '3' : 'three', 
        '4' : 'four',
        '5' : 'five',
        '6' : 'six',
        '7' : 'seven',
        '8' : 'eight',
        '9' : 'nine',
        '10' : 'ten', 
        '11' : 'eleven',
        '12' : 'twelve',
        '13' : 'thirteen',
        '15' : 'fifteen',
        '18' : 'eighteen'
    }

    if len(minute) == 1:
        return '{} minute'.format(num_as_string[minute])

    tens = {
        '2' : 'twenty',
        '3' : 'thirty',
        '4' : 'forty',
        '5' : 'fifty'
    }

    tens_place = minute[0]
    ones_place = minute[1]
    if tens_place == '1':
        return '{} minutes'.format(num_as_string[minute])
    else:
        return '{} {} minutes'.format(tens[tens_place], num_as_string[ones_place])

def hour_to_string(hour):
    return ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve'][hour - 1]

def time_to_string(hour, minute):
    if minute == 0:
        return '{} o\' clock'.format(hour_to_string(hour))
    if minute in range(1, 15) or minute in range(16, 30):
        return '{} past {}'.format(minute_to_string(minute), hour_to_string(hour))
    if minute == 15:
        return 'quarter past {}'.format(hour_to_string(hour))
    if minute == 30:
        return 'half past {}'.format(hour_to_string(hour))
    if minute == 45:
        return 'quarter to {}'.format(hour_to_string(hour + 1))
    if minute in range(31, 45) or minute in range(46, 60):
        return '{}{} to {}'.format(minute_to_string(60 - minute),'s' if 60 - minute < 10 else '' , hour_to_string(hour + 1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = time_to_string(h, m)

    fptr.write(result + '\n')

    fptr.close()
