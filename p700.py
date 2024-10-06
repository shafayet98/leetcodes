

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def searchTree(self, root, target):
        if not root:
            return None

        if target > root.val:
            self.searchTree(root.right, target)
        elif target < root.val:
            self.searchTree(root.left, target)
        else:
            return root




