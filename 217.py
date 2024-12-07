nums = [1,2,3,4]

def res(nums):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

def res2(nums):
    n = len(nums)
    setn = len(set(nums))
    if n != setn:
        return True
    return False 

print(res2(nums))


