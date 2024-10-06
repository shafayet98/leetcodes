


def guessNumber(n):
    left = 1
    right = n

    while left <= right:
        mid = (left+right)//2
        g = guess(mid)
    
        if g == -1:
            right = mid -1 
        elif g == 1:
            left = mid +1 
        else:
            return mid


def guess(num):
    pass




