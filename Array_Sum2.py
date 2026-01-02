def simpleArraySum(ar):
    
    return sum(ar)

if __name__ == '__main__':
    n = int(input().strip())              
    ar = list(map(int, input().split()))  
    result = simpleArraySum(ar)
    print(result)
