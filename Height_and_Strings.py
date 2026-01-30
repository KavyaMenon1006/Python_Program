import math
import os
import random
import re
import sys
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
def designerPdfViewer(h, word):

    Height = map(lambda c: h[ord(c) - ord('a')], word)
    return max(Height) * len(word)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()






