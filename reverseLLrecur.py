def reverseList(self, head):

    if not head:
        return None
    
    newHead = head
    if head.next:
        newHead = reverseList(head.next)
        head.next.next = head
    head.next = None

    return newHead
