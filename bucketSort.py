'''

Implementation of bucket Sort

'''

arr = [1,0,2,2,0,2]

def bucketSort(arr):
    counts = [0,0,0]

    for itm in arr:
        counts[itm] += 1
    
    pointer = 0

    for i in range(len(counts)):
        for j in range(counts[i]):
            arr[pointer] = i
            pointer +=1



bucketSort(arr)

print(arr)