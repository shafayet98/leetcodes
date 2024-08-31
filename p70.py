'''
70. Climbing Stairs

'''

def climbStairs(self, n: int) -> int:
    takeOneStep = 1
    takeTwoStep = 1

    for i in range(n-1):
        temp = takeOneStep
        takeOneStep = takeOneStep + takeTwoStep
        takeTwoStep = temp
    
    return takeOneStep