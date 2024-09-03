'''

Quick Sort Implementation

'''

arr = [6,2,4,1,3]

def quickSort(arr, s, e):
    if e-s+1 <=1:
        return arr

    pivot = arr[e]
    left = s

    for i in range(s,e):
        if arr[i] < pivot:
            temp = arr[left]
            arr[left] = arr[i]
            arr[i] = temp
            left+=1


    arr[e] = arr[left]
    arr[left] = pivot

    # recursive call to the left
    quickSort(arr,s,left-1)
    # recursive call to the right
    quickSort(arr,left+1,e)

    return arr

quickSort(arr,0,len(arr)-1)
print(arr)