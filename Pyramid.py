#Pyramid
rows=int(input("Enter the number of rows"))
for i in range(rows):
    for j in range(rows-i-1):
        print(" ",end="")
    for k in range(2*i+1):
            print("*",end="")
    print() 
#inverted pyramid
for i in range(rows,0,-1):
    for j in range(rows-i):
          print(" ",end="")
    for k in range(2*i-1):
            print("*",end="")
    print()
#for diamond shape
if rows%2==0:
      rows+=1
for i in range(rows//2+1):
    for j in range(rows//2-i):
        print(" ",end="")
    for k in range(2*i+1):
        print(" ",end="")
    print()
for i in range(rows // 2 - 1, -1, -1):
    for j in range(rows // 2 - i):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
