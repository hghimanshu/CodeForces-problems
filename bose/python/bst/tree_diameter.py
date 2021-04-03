from Tree_latest import BST,BinaryTreeNode

class Diameter:
    def __init__(self):
        self.max_edge = 0

    def getDiameter(self,root):

        def get_edges(root):

            if not root:
                return 0

            left_sum = get_edges(root.left)
            right_sum = get_edges(root.right)

            self.max_edge = max(self.max_edge,left_sum+right_sum)

            return 1 + max(left_sum,right_sum)

        # return get_edges(root)

        x = get_edges(root)
        return self.max_edge
        
if __name__ == "__main__":
    bst = BST() 
    print(bst)
    bst.push(12)
    bst.push(8)
    bst.push(15)
    bst.push(13)
    bst.push(20)
    bst.push(17)
    bst.push(50)
    dia = Diameter()
    print("Diameter is :: {}".format(dia.getDiameter(bst.root)))





