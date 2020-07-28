# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSymmetrix(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        if root1 is not None and root2 is not None:
            return (root1.val == root2.val) and self.findSymmetrix(root1.left, root2.right) and self.findSymmetrix(root1.right, root2.left)

    def isSymmetric(self, root):
        if root is None:
            return True
        
        return self.findSymmetrix(root, root)


ans = Solution()
# val = [3,9,20,None,None,15,7]
# val [1,2,2,3,4,4,3]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(ans.isSymmetric(root))