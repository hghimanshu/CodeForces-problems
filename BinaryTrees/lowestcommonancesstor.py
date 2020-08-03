from collections import namedtuple

class Tree:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    def lca(self, root, node1, node2):
        def get_depth(root, node):
            d = 0
            while root:
                if root is node:
                    break
                d+=1
                root = root.left
            return d
        
        d1, d2 = get_depth(root, node1), get_depth(root, node2)
        print(d1, d2)

            

    

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
print(ans.lca(root, root.right.left.right.left.right, root.right.left.right.right))