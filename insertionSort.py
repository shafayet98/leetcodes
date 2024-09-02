'''

Implementation of insertion sort


'''

arr = [2,3,4,1,6]

for i in range(1,len(arr)):
    j = i-1
    while j >= 0 and arr[j+1] < arr[j]:
        temp = arr[j+1]
        arr[j+1] = arr[j]
        arr[j] = temp
        j-=1

print(arr)
