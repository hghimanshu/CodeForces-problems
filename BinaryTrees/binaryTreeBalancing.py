class Tree:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    def calculateDepthatANode(self, root, ht):
        if root:
            if root.left is None and root.right is None:
                return ht
            ht +=1
            ht = self.calculateDepthatANode(root.left, ht)
            ht = self.calculateDepthatANode(root.right, ht)
        return ht
    
    
    def checkTreeisBalanced(self, root):
        if root:
            left_depth = self.calculateDepthatANode(root.left, 0)
            right_depth = self.calculateDepthatANode(root.right, 0)

            if abs(left_depth - right_depth) <= 1:
                self.checkTreeisBalanced(root.left)
                self.checkTreeisBalanced(root.right)
            else:
                return "NOT Balanced !! "
        return "Balanced !! "


    

## [314, 6,6,271,561,28,0,None,3,17,None,2,271,None,1,None,28,401,257,None,641]

root = Tree(314)
root.left = Tree(6)
root.right = Tree(6)
root.left.left = Tree(271)
root.left.right = Tree(561)
root.left.left.left = Tree(28)
root.left.left.right = Tree(0)
root.left.right.right = Tree(3)
root.left.right.right.left = Tree(17)

root.right.left = Tree(2)
root.right.right = Tree(271)
root.right.left.right = Tree(1)
root.right.right.right = Tree(28)
root.right.left.right.left = Tree(401)
root.right.left.right.right = Tree(257)
root.right.left.right.left.right = Tree(641)


ans = Solution()
print(ans.checkTreeisBalanced(root))