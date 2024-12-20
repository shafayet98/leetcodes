
height = [8,7,2,1]

def maxContainer(height):
    maxSize = 0
    l = 0
    r = len(height) - 1

    while l < r:
        area = (r-l) * min(height[l], height[r])
        maxSize = max(maxSize, area)

        if height[l] < height[r]:
            l += 1
        elif height[l] > height[r]:
            r -= 1
        elif height[l] == height[r]:
            l += 1

    return maxSize 


res = maxContainer(height)
print(res)