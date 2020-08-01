from collections import deque

class Tree:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.q = deque()
        
    def logic(self, root):
        if not root:
            return self.q
        
        current_depth_nodes = [root]
        while current_depth_nodes:
            self.q.append([curr.data for curr in current_depth_nodes if curr]) 
            current_depth_nodes = [
                child for curr in current_depth_nodes if curr for child in (curr.left, curr.right) 
            ]
        
        return list(self.q)


## [10, 2,4, 3,6, 1,5]

root = Tree(10)
root.left = Tree(2)
root.right = Tree(4)
root.left.left = Tree(3)
root.left.right = Tree(6)
root.right.left = Tree(1)
root.right.right = Tree(5)


ans = Solution()
print(ans.logic(root))