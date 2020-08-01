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
        
        leftToRight = True
        
        current_depth_nodes = [root]
        while current_depth_nodes:
            nodesAtPresentNode = [curr.data for curr in current_depth_nodes if curr]
            if leftToRight:
                nodesAtPresentNode = nodesAtPresentNode
                leftToRight = False
            else:
                nodesAtPresentNode = nodesAtPresentNode[::-1]
                leftToRight = True
            self.q.append(nodesAtPresentNode)
            current_depth_nodes = [child for curr in current_depth_nodes if curr for child in (curr.left, curr.right)]
        return list(self.q)[:-1]

    def bottomUpApproach(self, root):
        self.q = []        
        if not root:
            return self.q
                
        current_depth_nodes = [root]
        while current_depth_nodes:
            nodesAtPresentNode = [curr.data for curr in current_depth_nodes if curr]
            self.q.append(nodesAtPresentNode)
            current_depth_nodes = [child for curr in current_depth_nodes if curr for child in (curr.left, curr.right)]
        return list(reversed(self.q))[1:]

    def averageAteachDepth(self, root):
        self.q = []        
        if not root:
            return self.q
                
        current_depth_nodes = [root]
        while current_depth_nodes:
            nodesAtPresentNode = [curr.data for curr in current_depth_nodes if curr]
            if len(nodesAtPresentNode) == 0:
                break
            mean = sum(nodesAtPresentNode)/len(nodesAtPresentNode)
            self.q.append(mean)
            current_depth_nodes = [child for curr in current_depth_nodes if curr for child in (curr.left, curr.right)]
        return list(self.q)



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
print(ans.logic(root))
print(ans.bottomUpApproach(root))
print(ans.averageAteachDepth(root))