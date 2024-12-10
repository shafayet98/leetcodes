

nums = [100,4,200,1,3,2]

def longestSeq(nums):
    numset = set(nums)
    longest = 0

    for item in nums:
        if (item-1) not in numset:
            # start of the sequence
            lengthOfSeq = 0
            while(item + lengthOfSeq) in numset:
                lengthOfSeq = lengthOfSeq + 1
            longest = max(lengthOfSeq, longest)
    
    return longest

res = longestSeq(nums)

print(res)