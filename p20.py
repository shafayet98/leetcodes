'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


'''

s = "(]"


'''
first make the hashmap

'''



def solution(s):

    stack = []
    hashmap = {")" : "(", "}" : "{", "]" : "["}
    for chr in s:
        if chr in hashmap:
            if len(stack)>0 and stack[-1]==hashmap[chr]:
                stack.pop()
            else:
                return False
        else:
            stack.append(chr)

    
    if len(stack) == 0:
        return True
    else:
        return False
    

print(solution(s))