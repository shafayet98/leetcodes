
arr = [1,3,4,5,7,10,11]
target = 9

def twoSumSorted(arr,target):
    left = 0
    right = len(arr)-1

    while True:
        res = arr[left] + arr[right]
        if res > target:
            right = right -1
        if res < target:
            left = left + 1
        if res == target:
            return [left+1, right+1]
        

print(twoSumSorted(arr,target))