
nums = [2,7,11,15]
target = 9

# { 2 : 0 }
# 
# 

def twoSum(nums, target):
    hashMap = {}

    for i, n in enumerate(nums):
        diff = target-n
        if diff in hashMap:
            return [hashMap[diff],i]
        hashMap[n] = i


print(twoSum(nums,target))

