# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getRootFromPost(self, postorder):
        return postorder.pop()
    
    def getIndexofParentNode(self, inorder, root_val):
        try:
            ind = inorder.index(root_val)
            return inorder[:ind], inorder[ind+1:]
        except Exception:
            return None, None
    
    def executeTreeHalf(self, ino, post):
        if ino:
            val = self.buildTree(ino, post)
        else:
            return val 

    def buildTree(self, inorder, postorder):

        root_node = self.getRootFromPost(postorder)
        left_child, right_child = self.getIndexofParentNode(inorder, root_node)
        root = TreeNode(root_node)
        root.left = TreeNode(self.executeTreeHalf(left_child, left_child))
        root.right = TreeNode(self.executeTreeHalf(right_child, right_child))
        
        return root
    
ans = Solution()
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]


print(ans.buildTree(inorder, postorder))