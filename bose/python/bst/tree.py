class BinaryTree:
    def __init__(self,root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self,new_node):
        if self.left_child ==None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
    
    def insert_right(self,new_node):
        if self.right_child ==None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t
    
    def get_right_child(self):
        return self.right_child
    
    def get_left_child(self):
        return self.left_child

    def set_root_val(self,obj):
        self.key = obj

    def get_root_val(self):
        return self.key


r= BinaryTree("1")
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(2)
print(r.get_left_child().get_root_val())
r.get_left_child().insert_left(5)
print(r.get_left_child().get_left_child().get_root_val())