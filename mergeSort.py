'''

merge sort

'''

import math

arr = [3,2,4,1,6]
s = 0
e = len(arr)


def mergeSort(arr,s,e):
    if e-s+1 <= 1:
        return arr

    mid = math.floor((e+s)/2)
    # divide the left
    mergeSort(arr,s,mid)
    # divide the right
    mergeSort(arr,mid+1,e)

    merge(arr,s,mid,e)

    return arr

def merge(arr,s,mid,e):
    leftarr = arr[s:mid+1]
    rightarr = arr[mid+1:e+1]

    i = 0 # start of left arr
    j = 0 # start of right arr
    k = s # start original arr

    while i < len(leftarr) and j < len(rightarr):
        if leftarr[i] <= rightarr[j]:
            arr[k] = leftarr[i]
            i+=1
        else:
            arr[k] = rightarr[j]
            j+=1
        k+=1

    while i < len(leftarr):
        arr[k] = leftarr[i]
        i+=1
        k+=1

    while j < len(rightarr):
        arr[k] = rightarr[j]
        j+=1
        k+=1

mergeSort(arr,s,e)
print(arr)