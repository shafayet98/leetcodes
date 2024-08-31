'''

225. Implement Stack using Queues
Easy

Topics
Companies
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.



'''
from collections import deque 


class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        for item in range (len(self.queue)-1):
            self.push(self.queue.popleft())
        return self.queue.popleft()
        
    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False
    def printq(self):
        for i in range(len(self.queue)-1):
            print(self.queue[i])

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(4)
obj.push(2)
obj.push(9)
obj.printq()
# print(obj.pop())
'''
0 1 2
------
4 2 9
'''