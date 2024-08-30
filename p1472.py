
'''

1472. Design Browser History

You have a browser of one tab where you start on the homepage and you can visit another url, 
get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

- BrowserHistory(string homepage) Initializes the object with the homepage of the browser.

- void visit(string url) Visits url from the current page. It clears up all the forward history.

- string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, 
you will return only x steps. Return the current url after moving back in history at most steps.

- string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, 
you will forward only x steps. Return the current url after forwarding in history at most steps.
 



'''

class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.pev = None
        self.next = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.startNode = ListNode(homepage)

    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.startNode
        self.startNode.next = node
        self.startNode = node
        node.next = None

    def back(self, steps: int) -> str:
        cur = self.startNode
        count = steps
        while cur.prev and count != 0:
            cur = cur.prev
            count -= 1
        self.startNode = cur
        return self.startNode.val 

    def forward(self, steps: int) -> str:
        cur = self.startNode
        count = 0
        while cur.next and count != steps:
            cur = cur.next
            count += 1
        self.startNode = cur
        return self.startNode.val 
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)