#!/bin/python3
import heapq

def sorted_athletes(arr, k):
    min_heap = []
    for athlete in arr:
        heapq.heappush(min_heap, (athlete[k], athlete))
    sorted_athletes = []
    while min_heap:
        _, athlete = heapq.heappop(min_heap)
        sorted_athletes.append(athlete)
    return sorted_athletes
if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])  
    m = int(nm[1])   
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())  
    result = sorted_athletes(arr, k)
    for athlete in result:
        print(*athlete)
