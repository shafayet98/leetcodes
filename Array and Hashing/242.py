
s = "anagram"
t = "nagaram"

def isAnagram(s,t):
    if len(s) != len(t):
        return False
    
    hashTableS, hashTableT = {}, {}
    for i in range(len(s)):
        hashTableS[s[i]] = 1 + hashTableS.get(s[i],0)
        hashTableT[t[i]] = 1 + hashTableT.get(t[i],0)

    for i in hashTableS:
        if hashTableS[i] != hashTableT.get(i):
            return False

    return True

print(isAnagram(s,t))
