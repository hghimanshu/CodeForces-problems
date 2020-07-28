class newNode():  
  
    def __init__(self, data):  
        self.data = data 
        self.left = None
        self.right = None
          
    
    def insert_node(self, pr, ch, pos):
        useLeft = False
        if pos == 'L':
            useLeft = True

        if self.data == pr:
            if useLeft:
                self.left = newNode(ch)
            else:
                self.right = newNode(ch)
        else:
            while self.left.data == pr:
                self.left.insert_node(pr, ch, pos)
                break
            while self.right.data == pr:
                self.right.insert_node(pr, ch, pos)
                break
        


if __name__ == "__main__":
    q = [[1, 2, 'R'],
    [1, 3, 'L'],
    [2, 4, 'R'],
    [2, 5, 'L'],
    [3, 6, 'R'],
    [3, 7, 'L'],
    [5, 8, 'R'],
    [5, 9, 'L'],
    [7 ,10, 'R']]
    v = [2,5,3,6,1,10,9,4]
    root = newNode(1)
    for i in q:
        root.insert_node(i[0], i[1], i[2])
