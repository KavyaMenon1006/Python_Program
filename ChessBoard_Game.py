def chessboardGame(x, y):
  #Grid consists of (1,1) and (8,8)
    if (x % 4 == 1 or x % 4 == 2) and (y % 4 == 1 or y % 4 == 2):
        return "Second"
    else:
        return "First"
