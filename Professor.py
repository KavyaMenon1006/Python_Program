#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k, a):
    # Write your code here
    count = 0 
    for arrived in a:
        if arrived <= 0:   
            count += 1
    if count >= k:
        return "NO"   
    else:
        return "YES"  
