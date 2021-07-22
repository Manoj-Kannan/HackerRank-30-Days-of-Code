#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    a = []

    for _ in range(6):
        a.append(list(map(int, input().rstrip().split())))

    num_rows= len(a)
    max_sum = -9999 
    
    for k in range(num_rows-2):         
        for i in range(num_rows-2):     
            max_arr = []
            for j in range(i,i+3):      
                max_arr.append(int(a[k][j]))
                max_arr.append(int(a[k+2][j]))
                if j==i:
                    max_arr.append(int(a[k+1][j+1]))
        
            if sum(max_arr)>max_sum:
                max_sum = sum(max_arr)

    print(max_sum)