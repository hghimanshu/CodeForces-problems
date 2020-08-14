class Tree:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def generateMirrorTree(root1, root2):
    if root1:
        if root1.right:
            root2.left = Tree(root1.right.data)
        
        if root1.left:
            root2.right = Tree(root1.left.data)
        
        generateMirrorTree(root1.left, root2.right)
        generateMirrorTree(root1.right, root2.left)
        
        return root2


def mirrorTree(root):
    if root is None:
        return None
    
    root2 = Tree(root.data)
    root2 = generateMirrorTree(root, root2)
    return root2



root = Tree(10)
root.left = Tree(20)
root.right = Tree(30)
# root.left.left = Tree(40)
# root.left.right = Tree(60)
print(mirrorTree(root))