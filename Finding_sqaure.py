def squares(a, b):
    count = 0
    for i in range(a, b + 1):   
        square = int(math.sqrt(i))  
        if sqaure * square == i:      
            count += 1
    return count
