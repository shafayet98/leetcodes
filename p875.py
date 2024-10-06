import math

def minEatingSpeed(piles, h):
    left = 1
    right = max(piles)
    res = right

    while left <= right:
        mid = (left + right) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p/mid)
            
        if hours <= h:
            res = min(res, mid)
            right = mid -1
            
        else:
            left = mid + 1
    return res

piles = [30,11,23,4,20]
h = 6

print(minEatingSpeed(piles,h))