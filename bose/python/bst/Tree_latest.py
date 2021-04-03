class BinaryTreeNode:
    def __init__(self,left=None,data=None,right=None):
        self.left = left
        self.data = data
        self.right = right

    
    def insert_left(self,node,val):
        if node.left is None:
            node.left = BinaryTreeNode(data=val)
        else:
            node.left.data = val

    def insert_right(self,node,val):
        if node.right is None:
            node.right = BinaryTreeNode(data=val)
        else:
            node.right.data = val
    

class BST:
    def __init__(self):
        self.root = None

    def _push(self,current_node,val):
        if val < current_node.data:
            if current_node.left is None:
                current_node.left = BinaryTreeNode(data=val)
            else:
                current_node = current_node.left
                self._push(current_node,val)
        else:
            if current_node.right is None:
                current_node.right = BinaryTreeNode(data=val)
            else:
                current_node = current_node.right
                self._push(current_node,val)


    def push(self,val):
        if self.root is None:
            self.root = BinaryTreeNode(data=val)
        else:
            self._push(self.root,val)


    def inorder(self,current_node):
        if not current_node:
            return
        self.inorder(current_node.left)
        print(str(current_node.data))
        self.inorder(current_node.right)

    def preorder(self,current_node):
        if not current_node:
            return
        print(str(current_node.data))
        self.preorder(current_node.left)
        self.preorder(current_node.right)

    def postorder(self,current_node):
        if not current_node:
            return

        self.postorder(current_node.right)
        self.postorder(current_node.left)
        print(str(current_node.data))
        


   

if __name__ == '__main__':
    bst = BST() 
    print(bst)
    bst.push(10)
    bst.push(8)
    bst.push(9)
    bst.push(4)
    bst.push(15)
    bst.push(13)
    bst.push(17)
    bst.postorder(bst.root)