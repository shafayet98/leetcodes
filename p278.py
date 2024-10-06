
def firstBadVersion(n):
    left = 1
    right = n

    while left < right:
        mid = (left+right)//2
        badver = isBadVersion(mid) # true
    
        if badver == False:
            left = mid +1
        elif badver == True:
            right = mid 
    return left
        

def isBadVersion():
    pass