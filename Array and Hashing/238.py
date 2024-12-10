
nums = [1,2,3,4]
def proExcept(nums):

    res = []
    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if i == j:
                continue
            prod = prod * nums[j]
        res.append(prod)

    return res

def proExcept2(nums):
    n = len(nums)
    res = [1] * n

    pre = 1
    for i in range(n):
        res[i] = pre
        pre = pre * nums[i]
    
    post = 1
    for i in range(n-1, -1,-1):
        res[i] = res[i] * post
        post = post * nums[i]

    print(res)
    

# res = proExcept(nums)
proExcept2(nums)