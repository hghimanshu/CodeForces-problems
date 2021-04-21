from Tree_latest import BST,BinaryTreeNode

class Solution:

    def __init__(self):
        self.nodeList =[]
        self.parents = {}

    def createParentDict(self,root,parent): #creating a graph from the tree by mapping to parent

        self.parents[root] = parent

        if root.left:
            self.createParentDict(root.left,root)
        
        if root.right:

            self.createParentDict(root.right,root)

    def bfsOnTree(self,target,k):
        seen = {target:1}
        queue = [(target,0)]
        while queue:
            data = queue.pop(0)
            node = data[0]
            curr_level = data[1]

            if curr_level == k:
                self.nodeList.append(node.data)
            
            if node.left and node.left not in seen:
                queue.append((node.left,curr_level+1))
                seen[node.left] = 1

            if node.right and node.right not in seen:
                queue.append((node.right,curr_level+1))
                seen[node.right] = 1

            if self.parents[node] and self.parents[node] not in seen:
                queue.append((self.parents[node],curr_level+1))
                seen[self.parents[node]] = 1
            

    def distanceK(self, root, target, K):
        self.createParentDict(root,None)

        self.bfsOnTree(target,K)
        # print("Parent dict is ::{}".format(self.parents))

        return self.nodeList




if __name__ == "__main__":
    bst = BST() 
    print(bst)
    bst.push(15)
    bst.push(10)
    bst.push(4)
    bst.push(25)
    bst.push(17)
    bst.push(35)
    bst.push(30)
    bst.push(40)
    bst.push(12)
    bst.push(11)
    bst.push(14)
    # bst.inorder(bst.root)
    soln = Solution()
    print(soln.distanceK(bst.root,bst.root.left,2))