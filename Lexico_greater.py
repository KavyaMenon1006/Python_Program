def biggerIsGreater(w):
    # Write your code here
     #find pivot
    i = len(w) - 2
    while i >= 0 and w[i] >= w[i+1]:
        i -= 1
    if i == -1:
        return "no answer"
    #find successor
    j = len(w) - 1
    while w[j] <= w[i]:
        j -= 1
    #swap pivot and successor
    w = list(w)
    w[i], w[j] = w[j], w[i]
    #reverse suffix
    w[i+1:] = reversed(w[i+1:])
    return ''.join(w)
