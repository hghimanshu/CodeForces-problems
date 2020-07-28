class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self,key):
        if self.root:
            self._put(key,self.root)
        else:
            self.root = TreeNode(key)
        self.size+=1

    def _put(self,key,current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key,current_node.left_child)
            else:
                current_node.left_child = TreeNode(key)
        else:
            if current_node.has_right_child():
                self._put(key,current_node.right_child)
            else:
                current_node.right_child = TreeNode(key)

    def __inorder(self,current_node):
        if not current_node:
            return
        self.__inorder(current_node.left_child)
        print(str(current_node.key)+" ")
        self.__inorder(current_node.right_child)

    def __preorder(self,current_node):
        if not current_node:
            return
        print(str(current_node.key)+" ")
        self.__preorder(current_node.left_child)
        self.__preorder(current_node.right_child)
    
    def __postorder(self,current_node):
        if not current_node:
            return
        self.__postorder(current_node.left_child)
        self.__postorder(current_node.right_child)
        print(str(current_node.key)+" ")
        

    def traverse(self,traversal):
        if not self.root:
            return
        if traversal=="in":
            self.__inorder(self.root)
        elif traversal=="pre":
            self.__preorder(self.root)
        else:
            self.__postorder(self.root)
           

    



class TreeNode:
    def __init__(self,key,val=None,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child
    
    def get_root_val(self):
        return self.key

   

    


bst = BST()
bst.put(17)
bst.put(5)
bst.put(2)
bst.put(16)
bst.put(35)
bst.put(29)
bst.put(38)
bst.put(19)
bst.put(33)


# print(bst.root.has_right_child().get_root_val())
bst.traverse("in")
print("\n")
bst.traverse("pre")
print("\n")
bst.traverse("post")
