'''

1700. Number of Students Unable to Eat Lunch


1,1,1,1
1,1,0,1
--------
111
101
-------
11
01
------

'''

class Solution:
    def countStudents(self, students: int, sandwiches: int) -> int:
        numberOfStudents = len(students)
        cnt = {}

        for s in students:
            if s not in cnt:
                cnt[s] = 0
            cnt[s] +=1

        for s in sandwiches:
            if cnt[s] > 0:
                cnt[s] -= 1
                numberOfStudents -= 1
            else:
                return numberOfStudents
        
        return numberOfStudents

