# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        
        def findNode(root1,root2):
            if (root1 == target) and (root1.val==root2.val==target.val):
                return root2
            
            if root1.left:
                left = findNode(root1.left,root2.left)
            else:
                left = None
                
            if root1.right:
                right = findNode(root1.right,root2.right)
            else:
                right = None
                
            if left:
                return left
            
            else:
                return right
        
        return findNode(original,cloned)
            