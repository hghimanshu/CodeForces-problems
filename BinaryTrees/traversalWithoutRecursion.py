from collections import namedtuple

class Tree:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    def inorderWithoutRecursion(self, root):
        ### Left ---> Root ---> Right
        s, result = [], []

        while s or root:
            if root:
                s.append(root)

                root = root.left
            else:
                root = s.pop()
                result.append(root.data)
                root = root.right
        return result

    def preoderWithoutRecursion(self, root):
        ### Root ---> Left ---> Right
        s, result = [], []

        while s or root:
            if root:
                result.append(root.data)

                s.append(root)

                root = root.left
            else:
                root = s.pop()
                root = root.right
        return result

    # def postorderWithoutRecursion(self, root):
    #     ### Left ---> Right ---> Root
    #     s, result = [], []

    #     while s or root:
    #         if root:
    #             s.append(root)

    #             root = root.left
    #         else:
    #             root = s.pop()
    #             root = root.right
    #             result.append(root.data)
                
    #     return result


            

    

## [1, 0,1,0,1,0,1,None,1,0,None,0,0,None,0,1,0,None, 1,None,0]

root = Tree(1)
root.left = Tree(0)
root.right = Tree(1)
root.left.left = Tree(0)
root.left.right = Tree(1)
root.left.left.left = Tree(0)
root.left.left.right = Tree(1)
root.left.right.right = Tree(1)
root.left.right.right.left = Tree(0)

root.right.left = Tree(0)
root.right.right = Tree(0)
root.right.left.right = Tree(0)
root.right.right.right = Tree(0)
root.right.left.right.left = Tree(1)
root.right.left.right.right = Tree(0)
root.right.left.right.left.right = Tree(1)


ans = Solution()
print("INORDER Traversal :: " + str(ans.inorderWithoutRecursion(root)))
print("PREORDER Traversal :: " + str(ans.preoderWithoutRecursion(root)))
# print("POSTORDER Traversal :: " + str(ans.postorderWithoutRecursion(root)))