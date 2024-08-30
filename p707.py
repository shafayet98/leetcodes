'''

707. Design Linked List


Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.


'''

class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.left = ListNode(0)

    def get(self, index: int) -> int:
       count = 0
       cur = self.left.next
       while cur:
            if count == index:
                return cur.val
            cur = cur.next
            count += 1
       return -1


    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        cur = self.left
        if cur.next == None:
            cur.next = node
            node.next = None
        else:
            temp = cur.next
            cur.next = node
            node.next = temp

    
    def addAtTail(self, val: int) -> None:
        cur = self.left
        while cur.next:
            cur = cur.next
        node = ListNode(val)
        cur.next = node
        node.next = None

    def addAtIndex(self, index: int, val: int) -> None:
        '''
        void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list.
        If index equals the length of the linked list, the node will be appended to the end of the linked list. 
        If index is greater than the length, the node will not be inserted.
        '''

        if index < 0:
            return
        
        if index == 0:
            self.addAtHead(val)
        
        cur = self.left
        count = 0
        while cur:
            if count == index:
                temp = cur.next
                node = ListNode(val)
                cur.next = node
                node.next = temp
                return
            cur = cur.next
            count +=1 
        
        if count==index:
            self.addAtTail(val)

    def addAtIndex(self, index: int, val: int) -> None:
        '''
        void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list.
        If index equals the length of the linked list, the node will be appended to the end of the linked list. 
        If index is greater than the length, the node will not be inserted.
        '''

        if index < 0:
            return
        
        if index == 0:
            self.addAtHead(val)
        
        cur = self.left.next
        count = 0
        while cur:
            if count == index-1:
                temp = cur.next
                node = ListNode(val)
                cur.next = node
                node.next = temp
                return
            cur = cur.next
            count +=1 
        
        if count+1 == index:
            self.addAtTail(val)
        else:
            return
        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left
        count = 0
        while cur.next:
            if count == index:
                cur.next = cur.next.next
                return
            count+=1
            cur = cur.next


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtHead(3)
# obj.addAtHead(9)
# obj.addAtHead(7)
# obj.addAtTail(12)
# param_1 = obj.get(2)
obj.addAtIndex(0,10)
obj.addAtIndex(0,20)
obj.addAtIndex(1,30)
print( obj.get(0))
# obj.addAtIndex(6,1)
# obj.deleteAtIndex(0)