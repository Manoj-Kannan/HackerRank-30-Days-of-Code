#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())

    if N%2 != 0 or 5<N<21:
        print('Weird')
    elif 1<N<6 or N>21:
        print('Not Weird')
