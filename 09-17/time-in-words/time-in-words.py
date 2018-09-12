#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.

def minute_to_string(minute):

    minute = str(minute)

    if minute == '0':
        return ''

    ones = dict(zip('123456789', ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']))

    if len(minute) == 1:
        return '{} minute'.format(ones[minute])

    teens = dict(zip(['10', '11', '12', '13', '15', '18'], ['ten', 'eleven', 'twelve', 'thirteen', 'fifteen', 'eighteen']))
    tens = dict(zip('2345', ['twenty', 'thirty', 'forty', 'fifty']))

    tens_place = minute[0]
    ones_place = minute[1]
    if minute in teens:
        return '{} minutes'.format(teens[minute])
    if tens_place == '1':
        return '{}teen minutes'.format(ones[ones_place])
    if ones_place == '0':
        return '{} minutes'.format(tens[tens_place])
    else:
        return '{} {} minutes'.format(tens[tens_place], ones[ones_place])

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
