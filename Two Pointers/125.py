
import re 

# input = "amanaplanacanalpanama"
# input = "raceacar"
input = " "

def validPalindrom(str):
    str = re.sub(r'[^a-zA-Z0-9]', '', str).lower()
    left = 0
    right = len(str)-1

    if str == " ":
        return False

    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    
    return True

res = validPalindrom(input)
print(res)

# raceacar