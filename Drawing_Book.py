def pageCount(n, p):
    # Write your code here
    front_page = p//2
    back_page = n//2 - p//2
    return min(front_page, back_page)
