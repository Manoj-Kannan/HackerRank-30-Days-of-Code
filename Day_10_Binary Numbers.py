#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    binary = bin(n).replace('0b','')
    cur_count = 0
    max_count = 0                       # maximum number of consecutive 1's before 0
    for char in binary:
        if char == '1':
            cur_count+=1
        else:                           # if 0 is found, then past consecutuve 1's = max_count and cur_count = 0
            if cur_count > max_count:                          
                max_count = cur_count
            cur_count = 0
    print(max(max_count,cur_count))     # prints the maximum number among max_count and cur_count

# eg: bin(13) - 1101
# iter 1: cur_count = 1
# iter 2: cur_count = 2
# iter 3: 0 found, so max_count = 2, cur_count = 0
# iter 3: cur_count = 1
# print: maximum among max_count and cur_count