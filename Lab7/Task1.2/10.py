#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.

def time_delta(t1, t2):
    
    format_str = "%a %d %b %Y %H:%M:%S %z"
    date_t1 = datetime.strptime(t1, format_str)
    date_t2 = datetime.strptime(t2, format_str)
    
    difference = abs(date_t1 - date_t2)
    diff_seconds = difference.total_seconds()
    return(str(int(diff_seconds)))       
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
