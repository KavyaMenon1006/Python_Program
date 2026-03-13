def staircase(n):
    arr = [[" " for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n - i - 1, n):
            arr[i][j] = "#"
    for row in arr:
        print("".join(row))
