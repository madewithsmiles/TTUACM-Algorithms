#!/bin/python3

import sys
import string
import os

def caesarCipher(s, k):
    alpha = dict(zip(string.ascii_lowercase, range(len(string.ascii_lowercase))))
    encrypted = ""
    for c in range(len(s)):
        lo = s[c].lower()
        if lo in alpha:
            index = (k + alpha[lo]) % 26
            char = string.ascii_lowercase[index]
            encrypted += (char if s[c].islower() else char.upper())
        else: encrypted += s[c]
    return encrypted
