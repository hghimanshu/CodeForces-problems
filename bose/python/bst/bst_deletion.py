class BST:
    def __init__(self):
        self.root = None
        self.key = None
    
    def put(self,val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._put(self.root,val)
    
    def _put(self,current_node,val):
        if val > current_node.key:
            if current_node.get_right():
                self._put(current_node.right_child,val)
            else:
                current_node.set_right(TreeNode(val))

        else:
            if current_node.get_left():
                self._put(current_node.left_child,val)
            else:
                current_node.set_left(TreeNode(val))

    def _getSuccessor(self,parent_node,current_node):
        while current_node.get_left():
            parent_node= current_node
            current_node = current_node.left_child
        return parent_node,current_node

    def inorder(self,current_node):
        if not current_node:
            return
        self.inorder(current_node.left_child)
        print(current_node.key)
        self.inorder(current_node.right_child)

    def preorder(self,current_node):
        if not current_node:
            return
        print(current_node.key)
        self.preorder(current_node.left_child)
        self.preorder(current_node.right_child)

    def postorder(self,current_node):
        if not current_node:
            return
        self.postorder(current_node.right_child)
        self.postorder(current_node.left_child)
        print(current_node.key)

    def delete(self,parent_node,current_node,key):
      
        if key > current_node.key:
            parent_node = current_node
            current_node = current_node.right_child
            self.delete(parent_node,current_node,key)
        elif key < current_node.key:
            parent_node = current_node
            current_node = current_node.left_child
            self.delete(parent_node,current_node,key)

        elif current_node.key == key:
            #Case1: Node is leaf node
            if current_node.is_leaf():
                if current_node == parent_node.get_left():
                    current_node = None
                    parent_node.set_left(None)
                else:
                    current_node =None
                    parent_node.set_right(None)
            
            elif current_node.hasBothChildren():
                # find the successor node lying in the right subtree to replace the current node.
                node_to_delete = current_node
                parent_node = current_node
                current_node = current_node.right_child
                succParent,succNode = self._getSuccessor(parent_node,current_node)
                node_to_delete.key = succNode.key
                if node_to_delete  == succParent:
                    node_to_delete.set_right(succNode.get_right())
                    succNode = None
                else:
                    if succNode.get_right():
                        succParent.set_left(succNode.get_right())
                    else:
                        succParent.set_left(None)
                    succNode = None
            else:
                if current_node.get_left():
                    if current_node==parent_node.right_child:
                        parent_node.right_child = current_node.left_child
                        current_node = None
                    elif current_node==parent_node.left_child:
                        parent_node.left_child = current_node.left_child
                        current_node = None
                else:
                    if  current_node==parent_node.right_child:
                        parent_node.right_child = current_node.right_child
                        current_node = None
                    elif current_node==parent_node.left_child:
                        parent_node.left_child = current_node.right_child
                        current_node = None
    

class TreeNode:
    def __init__(self,key,left_child=None,right_child=None):
        self.key = key
        self.left_child = left_child
        self.right_child = right_child

    def get_left(self):
        return self.left_child
    
    def get_right(self):
        return self.right_child

    def set_left(self,left):
        self.left_child = left
    
    def set_right(self,right):
        self.right_child = right
    
    def is_leaf(self):
        return not(self.left_child) and not(self.right_child)

    def hasBothChildren(self):
        return self.left_child and self.right_child



# bst1 = BST()
# print(bst1)
# nodes_to_insert = [8,4,5,6,7,3,2,1,15,11,10,13,12,14,17,16,18]
# # nodes_to_insert = [8,5,6,4,3,2,1]
# for node in nodes_to_insert:
#     bst1.put(node)
# # bst1.put(2)
# # print(bst1.root.key)
# # print(bst1.root.rig1ht_child.key)
# # print(bst1.root.left_child.key)

# # bst1.inorder(bst1.root)

# # print("going to delete 17")
# # bst1.delete(None,bst1.root,17)


# bst1.postorder(bst1.root)


# dummy_node = None
# print(dummy_node.key)