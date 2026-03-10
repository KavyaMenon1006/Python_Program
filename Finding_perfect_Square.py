import math
def is_perfect_square(num):
    if num<0:
        print("enter a positive integer")
        return False
    else:
        sqrt=math.isqrt(num)
        return sqrt*sqrt==num
number=int(input("Enter a number:"))
if is_perfect_square(number):
    print("The number is a perfcet square")
else:
    print("The number is not a perfect square")
