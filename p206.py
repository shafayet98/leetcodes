# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode):
        prev = None
        curr = head

        while curr.next:
            temp = curr
            curr.next = prev
            prev = curr
            curr = temp.next
    