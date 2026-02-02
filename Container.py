def organizingContainers(container):
# Write your code here
    Container_Sum = [sum(row) for row in container]
    # Sum of balls of each type
    Sum = [sum(container[i][j] for i in range(len(container))) 
                 for j in range(len(container))]
    # Compare Sorted_List
    if sorted(Container_Sum) == sorted(Sum):
        return "Possible"
    else:
        return "Impossible"
