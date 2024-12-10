
nums = [1,1,1,2,2,3,0,0,0,0]
k = 2

def topKFreq(nums, k):
    hashTable = {}
    for i in nums:
        hashTable[i] = 1 + hashTable.get(i,0)
    
    arr = []
    for num, count in hashTable.items():
        arr.append([count, num])
    
    arr.sort(reverse=True)
    res = []
    for i in range(k):
        res.append(arr[i][1])

    return res


topKFreq(nums, k)