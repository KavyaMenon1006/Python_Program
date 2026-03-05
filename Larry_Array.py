#!/bin/python3

import os
import sys

def larrysArray(A):
    inversions = 0
    n = len(A)
    # Count inversions
    for i in range(n):
        for j in range(i+1, n):
            if A[i] > A[j]:
                inversions += 1
    # Check parity of inversions
    return "YES" if inversions % 2 == 0 else "NO"


if __name__ == '__main__':
    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        use_file = True
    except KeyError:
        # Running locally, no OUTPUT_PATH
        use_file = False

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        A = list(map(int, input().rstrip().split()))
        result = larrysArray(A)

        if use_file:
            fptr.write(result + '\n')
        else:
            print(result)

    if use_file:
        fptr.close()
