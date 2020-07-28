# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def calculateSum(self,root, total):
        if root:
            ans = 0

            remainder = total - root.val


            if remainder == 0 and root.left == None and root.right == None:
                return True
            
            ans = ans or self.calculateSum(root.left, remainder)
            ans = ans or self.calculateSum(root.right, remainder)

            return ans

    def hasPathSum(self, root, total):
        if root is None:
            return total == 0
        
        return self.calculateSum(root, total)


ans = Solution()
#  val = [5,4,8,11,None, 13,4,7,2,,None,None,None,1]

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
# root.left.right = TreeNode(4)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right.right.right = TreeNode(1)

print(ans.hasPathSum(root, 22))