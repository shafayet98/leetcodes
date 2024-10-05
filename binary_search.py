arr = [1, 3, 3, 4, 5, 6, 7, 8]

def bsearch(arr, target):

    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left+right)//2

        if target > arr[mid]:
            left = mid +1
        elif target < arr[mid]:
            right = mid -1
        else:
            return mid
    return -1

print(bsearch(arr,1))