# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDepth(self, root, depth, answer):
        if root:
            if root.left is None and root.right is None:
                return max(depth, answer)
            
            answer = self.findDepth(root.left, depth + 1, answer)
            answer = self.findDepth(root.right, depth +1, answer)
        return answer
        
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            depth = 1
        answer =1
        
        return self.findDepth(root, depth, answer)


ans = Solution()
# val = [3,9,20,None,None,15,7]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(ans.maxDepth(root))