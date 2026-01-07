import math
import os
import random
import re
import sys

def rotateLeft(d, arr):
    n = len(arr)
    for j in range(d):
        first = arr[0]
        for i in range(1, n):
            arr[i-1] = arr[i]
        arr[-1] = first
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
