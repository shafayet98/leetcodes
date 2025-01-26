s = "pwwkew"

def findLongestSub(s):
    l = 0
    r = 0
    maxSubStringLength = 0
    charSet = set()

    while r < len(s):

        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1

        charSet.add(s[r])
        maxSubStringLength = max(maxSubStringLength, r-l+1)
        r +=1 

    return maxSubStringLength


res = findLongestSub(s)
print(res)